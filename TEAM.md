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

...

### Bằng chứng

...

### Exit ticket

...

## PhamQuangDung-2A202603896

### Phần việc phụ trách

Kỹ sư cổng B; pair `guards.py`; `lab10/monitors.py`; Phiếu B 2.7–2.8; hỗ trợ Phiếu C.

### Đóng góp cụ thể

...

### Bằng chứng

...

### Exit ticket

...

## NguyenMinhPhuc-2A202603894

### Phần việc phụ trách

Vận hành và pháp lý; HAZOP/checklist; `operations`/`legal`; runbook; `submission/`.

### Đóng góp cụ thể

...

### Bằng chứng

...

### Exit ticket

...
