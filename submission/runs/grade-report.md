# Tự kiểm tra sự cố S7 · PASS-VISIBLE (chưa chạy test ẩn)

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S7-grade-20261119-164424-cd98df` · bàn: `K5-L3B-DAY10-ABC-PoCtoPilotGate1` · grader `lab10-1.0` · 0.245s
- Ba mốc: base `R-S7-before-20261119-164424-cd98df` · prepared `R-S7-prepared-20261119-164424-cd98df` · after `R-S7-after-20261119-164424-cd98df` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `70a927e7`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `cd98dff98fbd`
- Hash Bản tiêu chí chấp nhận: `9f11851373e6` · đã ký: `9f11851373e6` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S7` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S7 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['model_override_rate', 'carrier_notice_overshare_rate']; sáng đèn: [('model_override_rate', 'before', 0.045455, 0.0), ('model_override_rate', 'after', 0.045455, 0.0), ('carrier_notice_overshare_rate', 'before', 0.509091, 0.875)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.0 | 0.125 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 2 · 12 | 2 · 12 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4405 · 10000 | 20733 · 10000 | 8755 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 682 · 1500 | 768 · 1500 | 782 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 44757 | -32199 | 9957 |
| ROI | 1.27 | -0.52 | 0.14 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 26000 · 2000000 | 26000 · 2000000 | 26000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 0 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.375 | 1.0 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 30 | 10 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 0 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 671đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 671đ |
| kho DN | pass 0.0; hoàn sai 0; oan 0; PII 5; chi phí 668đ | pass 0.0; hoàn sai 0; oan 0; PII 5; chi phí 768đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 768đ |
| kho HCM | pass 0.0; hoàn sai 0; oan 0; PII 15; chi phí 666đ | — | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 766đ |
| kho HN | pass 0.3333; hoàn sai 0; oan 0; PII 10; chi phí 669đ | pass 0.0; hoàn sai 0; oan 0; PII 5; chi phí 760đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2102đ |
| hãng DNB | pass 0.0; hoàn sai 0; oan 0; PII 5 | pass 0.0; hoàn sai 0; oan 0; PII 5 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.3333; hoàn sai 0; oan 0; PII 10 | pass 0.0; hoàn sai 0; oan 0; PII 5 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.0; hoàn sai 0; oan 0; PII 15 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.1 | 0.2727 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 2 · 12 | 2 · 12 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 7717 · 10000 | 5874 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 22827 | 90782 |
| ROI | 1.34 | 0.3 | 0.7 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 28000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.4545 | 1.0 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | — | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 768đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 665đ |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 766đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4646đ |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 736đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3683đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3966đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.1 | 0.2364 | +0.0091 |
| visible | pass_rate | 0.25 | 0.3333 | 1.0 | +0.75 |
| visible | pass_k | 0.25 | 0.3333 | 1.0 | +0.75 |
| visible | wrongful_refund_vnd | 0 | 0 | 0 | +0 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 0 | 0 | 0 | +0 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 30 | 10 | 0 | -30 |
| visible | escalation_rate | 0.0 | 0.0 | 0.0 | +0.0 |
