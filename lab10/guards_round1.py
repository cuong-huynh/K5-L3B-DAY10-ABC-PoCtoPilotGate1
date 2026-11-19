"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 1 (pre): ghim chính sách hiệu lực theo as_of — tránh model chọn sai phiên bản policy
    policies = ctx.tools.lookup_policies()
    pol = H.effective_policy(policies, ctx.as_of)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    order_id = action.get("order_id") or ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    policies = ctx.tools.lookup_policies()
    pol = H.effective_policy(policies, ctx.as_of)
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of) if order else None
    db_delay = H.db_delay_days(parcel, ctx.as_of) if parcel else None
    cause = (parcel or {}).get("delay_cause")

    # Cổng 2: trần hoàn tự động trong ngày (business.daily_refund_cap_vnd)
    if tool == "issue_refund":
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        spent = ctx.tools.auto_refund_today_vnd()
        amt = int(action.get("amount_vnd") or 0)
        if cap is not None and spent + amt > cap:
            return Verdict.escalate("vượt trần hoàn trong ngày, chuyển người duyệt")

        # Cổng 3: số tiền không vượt quyền lợi tính từ tracking DB (chặn model tin số ngày khách khai)
        if pol and order and db_delay is not None:
            entitled = H.entitlement_vnd(pol, order, db_delay, cause)
            if amt > entitled:
                return Verdict.escalate(
                    f"amount {amt}đ > entitlement DB {entitled}đ (delay DB={db_delay}), chuyển người"
                )

    # Cổng 4: không ghi lỗi hãng nếu tracking chưa đủ điều kiện / delay lệch DB
    if tool == "file_carrier_fault" and pol and parcel is not None and db_delay is not None:
        if not H.carrier_at_fault(pol, parcel, db_delay):
            return Verdict.deny("tracking không đủ điều kiện ghi lỗi hãng")
        claimed = action.get("delay_days")
        if claimed is not None and int(claimed) != int(db_delay):
            return Verdict.deny(
                f"delay_days lệnh ghi ({claimed}) khác tracking DB ({db_delay})"
            )

    return Verdict.allow()
