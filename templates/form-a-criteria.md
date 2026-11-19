# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ABC · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm công CSKH xử lý hoàn phí giao trễ mà vẫn giữ sổ cái khớp với hãng/shop và không hoàn oan / ghi lỗi hãng oan khi chạy pilot 2 depot.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): mọi dòng hoàn và lỗi hãng do trợ lý ghi phải đối soát được với tracking/sổ cái trong tuần, không phát sinh khoản treo.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): hàng chờ duyệt không ùn quá SLA 60 phút trong ca, và mỗi ca escalate có lý do rõ để duyệt nhanh.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn độ trễ dùng để tính hoàn (`proposal.delay_days_used`) | Gửi thông báo / ghi lỗi ra ngoài LogiX (hãng nhận payload) |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy mà `delay_days_used` ≠ `tracking.db_delay_days` (đơn vị: tỉ lệ 0–1) | Số lần payload gửi hãng còn chứa trường PII bị chặn theo config / ngày |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `proposal` và `tracking` trong `runs/<mã>/traces/`; 22 ticket × 5 seed bộ nền; nhãn đúng/sai từ bộ nền lab | Sự kiện `tool=notify_carrier` + `legal_gate` trong trace production; Ops/Legal gán danh sách trường cấm |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lần hai giá trị khác nhau ÷ số lần chạy có `proposal`; thiếu `proposal` loại khỏi mẫu số, đếm riêng | Đếm message có field ∈ `pii_fields_blocked_to_third_party` còn sót; thiếu outbound = 0 lần lộ |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ 24h; báo động khi ≥ 1 lần lộ |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy trường hợp tracking DB sai sự thật | Không thấy hoàn oan nếu không gửi hãng |

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: pass_rate Y = 1,0 nằm trong khoảng tin cậy 95% của X [0,9400; 1,0] nên chưa đủ căn cứ nói Y tốt hơn X về mặt thống kê.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

#### Bước 1 · Viết câu tiêu chí

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate trên bộ nền tụt dưới 0,95 thì chúng tôi sẽ Cải tiến thêm trước khi Tiếp tục | Nếu sau một vòng sửa vẫn < 0,95 thì Thu hẹp % pilot |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k < 0,85 trên bộ nền thì không chọn Tiếp tục | |
| `wrongful_refund_vnd_max` | Nếu hoàn sai > 0đ trên bộ nền hoặc gói sự cố thì không chọn Tiếp tục | |
| `wrongful_carrier_faults_max` | Nếu lỗi hãng oan > 0 thì tắt file_carrier_fault và Thu hẹp | |
| `pii_leaks_max` | Nếu lộ PII > 0 thì Dừng gửi notify_carrier tới khi vá | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ escalate > 0,35 mà vẫn an toàn thì Thu hẹp phạm vi thay vì ép tự động | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): không bao giờ hoàn vượt quyền lợi tính từ tracking DB; không gửi phone/address cho hãng
- Ngưỡng chuyển cho người duyệt: amount > entitlement DB, hoặc vượt trần hoàn ngày 1.500.000đ

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: an toàn bảo vệ hãng/kế toán; pass_rate bảo vệ khách/CSKH |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép pass cao có thể tăng escalate → Hạnh quá tải |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày 1 ưu tiên an toàn = 0 hơn ROI cao |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | pass_rate/ROI và pilot_scope sẽ viết lại khi mở thêm depot |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Ngưỡng đã chép vào `config/acceptance_criteria.json`
- Nhóm `business_ops`: `cost_per_ticket_vnd_max` 10000 · `roi_min` 0 · `queue_stuck_max` 2
- Ngày xem lại tiêu chí: `26/11/2026` · Ai dự: Cường, Đức, Dũng, Phúc (ghi B8)

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | _(điền sau khi ký)_ |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | _(điền sau khi push)_ |
| Đã push lên `origin main` thành công? | _(điền sau)_ |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
