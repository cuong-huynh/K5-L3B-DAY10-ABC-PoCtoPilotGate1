# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `ABC`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-ABC-PoCtoPilotGate1`
- URL: https://github.com/cuong-huynh/K5-L3B-DAY10-ABC-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): _(chưa — repo thẻ GitHub 404 / chờ Lab Coach mở)_

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý.

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Huỳnh Văn Cường | 2A202603866 | Kỹ sư cổng A (lead kỹ thuật) | x |
|   2 | Nguyễn Phan Tuấn Đức | 2A202603818 | Sản phẩm và kinh doanh | |
|   3 | Phạm Quang Dũng | 2A202603896 | Kỹ sư cổng B | |
|   4 | Nguyễn Minh Phúc | 2A202603894 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công nhanh (4 người)

| Người | Vai | File / phiếu chính |
|-------|-----|-------------------|
| **Cường** | Kỹ sư cổng A + trưởng nhóm repo | Lệnh eval/gate/trace/checkpoint/grade; `lab10/guards.py` (`pre_guard`, `write_gate`); vòng 2 sửa theo thẻ; Phiếu B: 2.1–2.2, 2.6; Phiếu C: trace + sửa |
| **Đức** | Sản phẩm và kinh doanh | Phiếu **A** (chủ bút); `config/acceptance_criteria.json` + ký; `operating_gates.json` → `business`; quyết định v1/v2 (B8, C12) |
| **Dũng** | Kỹ sư cổng B | Pair `guards.py`; `lab10/monitors.py` (≥1 chỉ số vòng 2); test/`--adhoc`; Phiếu B: 2.7–2.8; hỗ trợ phân tích ticket Phiếu C |
| **Phúc** | Vận hành và pháp lý | HAZOP + checklist 9 nhóm (B4–B5); `operating_gates.json` → `operations`/`legal` + runbook; `submission/submission.json`; lệnh 7 gom nộp (C11) |

Cả bàn: pre-mortem (2.5), chốt quyết định v1/v2, demo, mỗi người mục cá nhân bên dưới.

---

## Cá nhân

Mỗi thành viên tự viết mục của mình trước khi nộp (điền MSSV vào tiêu đề).

## HuynhVanCuong-2A202603866

### Phần việc phụ trách

Kỹ sư cổng A · trưởng nhóm repo; câu 2.1–2.2, 2.6; file `lab10/guards.py`; chạy lệnh lab; Phiếu B/C phần kỹ thuật.

### Đóng góp cụ thể

Trưởng nhóm repo; git identity MSSV; câu 1.3 Phiếu A; chạy eval/gate/trace base; bảng soát lỗi T-002@55; code 2–3 cổng `guards.py` (pin policy, trần hoàn + entitlement DB, deny fault lệch DB); checkpoint vòng 1; hỗ trợ B8 v1; thêm `model_override_rate` monitor; chuẩn bị vòng 2 chờ thẻ.

### Bằng chứng

- Commit ký: `e170383` · checkpoint `70a927e7`
- Runs: `R-base-before-20261119-152257-e58096`, `R-base-after-20261119-152310-e58096`, `R-base-prepared-20261119-152317-e58096`
- Adhoc O-1002: escalate khi khai delay > DB

### Exit ticket

Gate 1 v1 chọn Tiếp tục trên prepared vì mọi ngưỡng required đạt; còn thiếu gói sự cố để chốt v2. Bài học: ký tiêu chí trước eval và neo cổng vào tracking DB, không vào chữ khách.

## NguyenPhanTuanDuc-2A202603818

### Phần việc phụ trách

Sản phẩm và kinh doanh; Phiếu A; `config/acceptance_criteria.json`; cổng `business`; quyết định v1/v2.

### Đóng góp cụ thể

Chủ bút Phiếu A (mục tiêu, tiêu chí 1.6, câu 1.5 chọn b); điền và ký `acceptance_criteria.json` (team đúng tên repo, an toàn = 0, business_ops neo ops_facts); đặt cổng `business` (trần hoàn ngày 1.5tr, cost budget, pilot_scope, roi_min); tham gia B3 drift + B8 quyết định v1 = Tiếp tục trên prepared; chuẩn bị C12/v2 khi có thẻ.

### Bằng chứng

- Commit ký tiêu chí: `e170383` · hash tiêu chí `9f118513…`
- `config/operating_gates.json` mục `business` (vòng 1 percent 50 đã chốt; vòng 2 mở all)
- Phiếu A A1–A5 và Phiếu B B3/B7.4/B8 đã điền; gate prepared mọi required [ĐẠT]

### Exit ticket

Ngày 1 Gate 1 nên ưu tiên an toàn = 0 trước ROI; ký tiêu chí trước eval buộc bàn đặt luật khi chưa nhìn số. Còn thiếu thẻ sự cố để chốt v2.

## PhamQuangDung-2A202603896

### Phần việc phụ trách

Kỹ sư cổng B; pair `guards.py`; `lab10/monitors.py`; Phiếu B 2.7–2.8; hỗ trợ Phiếu C.

### Đóng góp cụ thể

Pair thiết kế cổng với Cường (entitlement DB, deny fault lệch DB, trần ngày); viết/đăng ký `model_override_rate` trong `monitors.py`; điền B7.2 (hai bước tránh overfit bộ nền) và B7.3 behavioral test `--adhoc` trên O-1002 (escalate khi khai delay cao hơn DB; denied khi trust thấp); sẽ hỗ trợ trace ticket thẻ ở Phiếu C.

### Bằng chứng

- `lab10/monitors.py` có `model_override_rate` trong `MONITORS`
- Adhoc: “Đơn trễ 9 ngày…” → escalate; “Giao chậm 5 ngày…” → denied, sổ cái rỗng
- unittest 13 OK sau cổng vòng 1

### Exit ticket

Monitor phải “sáng đèn” khác nền khi có sự cố; adhoc giúp chứng minh tính chất cổng trước demo. Chờ thẻ để kiểm monitor trên gói Sx.

## NguyenMinhPhuc-2A202603894

### Phần việc phụ trách

Vận hành và pháp lý; HAZOP/checklist; `operations`/`legal`; runbook; `submission/`.

### Đóng góp cụ thể

Điền Phiếu A câu 1.2/1.4 (góc Oanh/Hạnh + telemetry PII); HAZOP B4 (≥3 dòng + ngoài kỹ thuật) và checklist 9 nhóm có PIC (B5); điền `operations` (PIC NV-PHUC, approver NV-HANH, 2 reviewer, stop_conditions, alert_channel) và `legal` (block PII + carrier_fault_requires_recorded_cause); runbook 1–3 + giờ cao điểm B7.5–B7.6; điền `submission.json` members 4 người; theo dõi lệnh collect.

### Bằng chứng

- `config/operating_gates.json` mục `operations`/`legal` không còn trống
- Phiếu B B4–B5, B7.5–B7.6 đã điền; `submission/submission.json` members khớp TEAM
- Collect: cổng con người [ĐỦ]; còn thiếu incident/v2/Phiếu C khi chưa có thẻ

### Exit ticket

Cổng người + pháp lý phải khớp runbook (ai bấm dừng, SLA chờ). Bài học: PIC có tên từng dòng checklist. Còn C11/C3 theo thẻ khi Coach mở Sx.
