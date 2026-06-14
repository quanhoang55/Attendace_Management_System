# Kế Hoạch Làm Bài Tập Lớn: Hệ Thống Quản Lý Điểm Danh

## 1. Tóm Tắt Hướng Làm

Xây dựng chương trình console bằng Python, điều khiển bằng menu. Dữ liệu lưu trong file text. Không dùng `list`, `dict`, `set`, hàm `sort`, hay thư viện tìm kiếm/sắp xếp có sẵn.

Chọn hướng cài đặt chính:

- Dùng **danh sách liên kết đơn tự cài đặt** để lưu lớp học, sinh viên, lịch học, buổi điểm danh.
- Dùng **tìm kiếm tuyến tính** tự viết.
- Dùng **sắp xếp chọn** hoặc **sắp xếp nổi bọt** tự viết cho báo cáo sinh viên vắng nhiều nhất.
- Lưu dữ liệu bằng file text dạng dễ đọc, mỗi dòng là một bản ghi.

## 2. Các Chức Năng Cần Làm

### Quản lý lớp học

Cần có các tác vụ:

- Thêm lớp học: mã lớp, tên môn/lớp.
- Xem danh sách lớp.
- Tìm lớp theo mã lớp.
- Quản lý danh sách sinh viên trong lớp:
  - Thêm sinh viên: mã sinh viên, họ tên.
  - Xem sinh viên theo lớp.
  - Tìm sinh viên theo mã sinh viên.

### Quản lý thời khóa biểu

Mỗi lớp có lịch học gồm:

- Thứ trong tuần.
- Tiết học.
- Phòng học.

Menu cần có:

- Thêm lịch học cho lớp.
- Xem thời khóa biểu của lớp.

### Ghi nhận điểm danh

Mỗi buổi điểm danh cần lưu:

- Mã lớp.
- Ngày học.
- Mã sinh viên.
- Trạng thái:
  - `CM`: Có mặt.
  - `VCP`: Vắng có phép.
  - `VKP`: Vắng không phép.

Menu cần có:

- Điểm danh cho một lớp theo ngày.
- Xem điểm danh của một lớp theo ngày.
- Tìm lịch sử điểm danh theo mã sinh viên.

## 3. Logic Nghiệp Vụ Và Báo Cáo

### Tính tỷ lệ vắng

Với mỗi sinh viên:

```text
số buổi vắng = vắng có phép + vắng không phép
tổng số buổi đã điểm danh = số bản ghi điểm danh của sinh viên đó
tỷ lệ vắng = số buổi vắng / tổng số buổi * 100
```

Nếu tỷ lệ vắng `> 20%`, hiển thị cảnh báo:

```text
Nguy cơ cấm thi
```

### Báo cáo cần có

- Thống kê sĩ số lớp theo từng buổi:
  - Tổng sinh viên.
  - Số có mặt.
  - Số vắng có phép.
  - Số vắng không phép.
- Danh sách sinh viên vắng nhiều nhất:
  - Tính số buổi vắng của từng sinh viên.
  - Sắp xếp giảm dần bằng thuật toán tự cài.
  - In top sinh viên vắng nhiều.

## 4. Thiết Kế Chương Trình

### Các lớp dữ liệu nên có

- `Student`
  - `student_id`
  - `full_name`
  - `next`

- `ClassRoom`
  - `class_id`
  - `class_name`
  - `students`
  - `schedules`
  - `next`

- `Schedule`
  - `weekday`
  - `period`
  - `room`
  - `next`

- `AttendanceRecord`
  - `class_id`
  - `date`
  - `student_id`
  - `status`
  - `next`

- `LinkedList`
  - `head`
  - `append()`
  - `find()`
  - `traverse()`
  - `remove()` nếu cần

### File dữ liệu

Dùng 3 file text chính:

```text
classes.txt
students.txt
attendance.txt
```

Gợi ý định dạng:

```text
classes.txt
CLASS_ID|CLASS_NAME

students.txt
CLASS_ID|STUDENT_ID|FULL_NAME

attendance.txt
CLASS_ID|DATE|STUDENT_ID|STATUS
```

Ví dụ:

```text
IT001|Kỹ thuật lập trình
IT001|20241234|Nguyễn Văn A
IT001|2026-05-14|20241234|CM
```

## 5. Thứ Tự Làm Việc

1. Phân tích yêu cầu và chốt phạm vi chức năng.
2. Thiết kế cấu trúc dữ liệu tự cài:
   - Node.
   - LinkedList.
   - Các lớp dữ liệu chính.
3. Làm phần đọc/ghi file text.
4. Làm menu chính.
5. Làm chức năng quản lý lớp.
6. Làm chức năng quản lý sinh viên.
7. Làm chức năng quản lý thời khóa biểu.
8. Làm chức năng điểm danh theo ngày.
9. Làm chức năng tìm kiếm:
   - Theo ngày của lớp.
   - Theo mã sinh viên.
10. Làm tính tỷ lệ vắng và cảnh báo trên 20%.
11. Làm báo cáo thống kê sĩ số từng buổi.
12. Làm báo cáo sinh viên vắng nhiều nhất.
13. Kiểm thử bằng dữ liệu mẫu.
14. Viết báo cáo bài tập lớn.

## 6. Kiểm Thử

Cần chuẩn bị dữ liệu test cho các trường hợp:

- Thêm lớp mới thành công.
- Thêm sinh viên vào lớp.
- Điểm danh đủ sinh viên trong một ngày.
- Tìm điểm danh theo ngày của lớp.
- Tìm điểm danh theo mã sinh viên.
- Sinh viên vắng đúng 20%.
- Sinh viên vắng trên 20% và có cảnh báo.
- Báo cáo sĩ số hiển thị đúng số có mặt/vắng.
- Báo cáo sinh viên vắng nhiều nhất sắp xếp đúng.

## 7. Báo Cáo Cần Viết

Báo cáo nên có các phần:

- Mô tả đề tài và chức năng chính.
- Thiết kế chương trình:
  - Sơ đồ menu.
  - Các lớp dữ liệu.
  - Cấu trúc danh sách liên kết.
  - Cấu trúc file text.
- Thuật toán đã dùng:
  - Tìm kiếm tuyến tính.
  - Tính tỷ lệ vắng.
  - Sắp xếp danh sách sinh viên vắng nhiều.
  - Đọc/ghi file.
- Kiểm thử:
  - Bảng test case.
  - Kết quả chạy thử.
- Phụ lục code:
  - Hàm `main`.
  - Các hàm xử lý nghiệp vụ chính.

## 8. Giả Định Mặc Định

- Chương trình chạy trên console, không làm giao diện đồ họa.
- Một lớp có nhiều sinh viên.
- Một sinh viên có thể thuộc nhiều lớp nếu dữ liệu nhập như vậy.
- Mỗi sinh viên trong một lớp chỉ có một bản ghi điểm danh cho một ngày.
- Vắng có phép và vắng không phép đều được tính vào tỷ lệ vắng.
- Dữ liệu được lưu ngay sau khi thêm/sửa để tránh mất dữ liệu.

