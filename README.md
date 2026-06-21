# 📋 Hệ Thống Quản Lý Điểm Danh

Ứng dụng dòng lệnh (CLI) quản lý điểm danh học sinh, được xây dựng bằng **Python** — không dùng bất kỳ thư viện collection nào của ngôn ngữ, toàn bộ cấu trúc dữ liệu được tự cài đặt bằng danh sách liên kết đơn (`MyLinkedList`).

---

## ✨ Tính Năng

### Quản Lý Lớp Học
- Thêm lớp học mới
- Xem danh sách tất cả lớp học
- Thêm học sinh vào lớp
- Xem danh sách học sinh trong lớp
- Thêm / xem thời khóa biểu cho lớp

### Điểm Danh
- Ghi nhận điểm danh (Có mặt / Vắng có phép / Vắng không phép)
- Tìm kiếm điểm danh theo lớp + ngày
- Tìm kiếm lịch sử điểm danh theo mã học sinh
- Xem tỉ lệ vắng mặt của học sinh trong một lớp

### Báo Cáo
- Thống kê điểm danh theo buổi học
- Xếp hạng học sinh vắng nhiều nhất
- Danh sách học sinh có nguy cơ (tỉ lệ vắng > 20%)

### Lưu Trữ
- Tự động lưu dữ liệu ra file khi thoát
- Tự động tải lại dữ liệu khi khởi động

---

## 🏗️ Kiến Trúc

```
ktlt_project/
├── main.py                        # Entry point
│
├── app/
│   ├── core/
│   │   ├── linked_list.py         # MyLinkedList
│   │   └── attendanceStatus.py    # AttendanceStatus
│   │
│   ├── models/
│   │   ├── student.py             # Student
│   │   ├── schedule.py            # Schedule
│   │   ├── attendance.py          # AttendanceRecord
│   │   ├── session.py             # Session
│   │   └── school_class.py        # SchoolClass
│   │
│   ├── services/
│   │   ├── file_manager.py        # Đọc/ghi file
│   │   ├── report_service.py      # Tạo báo cáo
│   │   └── attendance_manager.py  # điều phối toàn hệ thống
│   │
│   └── ui/
│       └── menu.py                # Giao diện menu CLI
│
├── tests/
│   ├── test_attendance_manager.py
│   ├── test_attendance_record.py
│   ├── test_attendance_status.py
│   ├── test_file_manager.py
│   ├── test_linked_list_edge_cases.py
│   ├── test_linked_list.py
│   ├── test_menu.py
│   ├── test_models.py
│   ├── test_persistence.py
│   ├── test_report_service.py
│   ├── test_schedule.py
│   ├── test_school_class.py
│   ├── test_services.py
│   ├── test_session.py
│   └── test_student.py
│
└── data/
    ├── classes.txt
    ├── students.txt
    ├── schedules.txt
    ├── sessions.txt
    └── attendance.txt
```

### Phân Lớp Hệ Thống

```
MainProgram  (UI / menu loop)
    │
AttendanceManager  (Facade / điều phối)
    │                   └──────────────────────────┐
SchoolClass                         AttendanceReport   FileManager
    │    └──────────────┐
Schedule    Session
                │
          AttendanceRecord ── AttendanceStatus
                │
            Student

MyLinkedList<T> + Node<T>  ← dùng xuyên suốt toàn bộ hệ thống
```
---

## 🚀 Cách Chạy

```bash
# Chạy ứng dụng chính
python main.py
```

```bash
# Chạy test
python -m tests.test_attendance_manager
python -m tests.test_attendance_record
python -m tests.test_attendance_status
python -m tests.test_file_manager
python -m tests.test_linked_list_edge_cases
python -m tests.test_linked_list
python -m tests.test_menu
python -m tests.test_models
python -m tests.test_persistence
python -m tests.test_report_service
python -m tests.test_schedule
python -m tests.test_school_class
python -m tests.test_services
python -m tests.test_session
python -m tests.test_student
```

---

## 📄 Định Dạng Dữ Liệu

Dữ liệu được lưu dưới dạng văn bản thuần, phân cách bằng ký tự `|`, mỗi bản ghi trên một dòng:

| File | Định dạng |
|------|-----------|
| `classes.txt` | `classId\|className` |
| `students.txt` | `classId\|studentId\|fullName` |
| `schedules.txt` | `classId\|dayOfWeek\|period\|room` |
| `sessions.txt` | `classId\|date` |
| `attendance.txt` | `classId\|date\|studentId\|status` |

> Trạng thái điểm danh (`status`) nhận một trong ba giá trị: `PRESENT`, `EXCUSED_ABSENCE`, `UNEXCUSED_ABSENCE`.

---

## 📐 Yêu Cầu Về Project

Đây là project học thuật với các ràng buộc bắt buộc:

- Không được dùng `list`, `dict`, `set`, `tuple`, hay bất kỳ collection nào của Python cho dữ liệu ứng dụng
- Không dùng hàm sort/search có sẵn (`sorted()`, `.sort()`, `.find()`, v.v.)
- Sắp xếp danh sách vắng nhiều nhất: **Bubble Sort** thủ công trên các node của `MyLinkedList`.

---

## 🗃️ Mô Tả Các Lớp Chính

| Lớp | Vai Trò |
|-----|---------|
| `MyLinkedList` | Danh sách liên kết đơn tự cài — cấu trúc dữ liệu duy nhất trong toàn hệ thống |
| `Student` | Thông tin học sinh (mã, họ tên) |
| `Schedule` | Thời khóa biểu (thứ, tiết, phòng) |
| `AttendanceRecord` | Bản ghi điểm danh của một học sinh trong một buổi |
| `Session` | Một buổi học cụ thể (lớp + ngày) |
| `SchoolClass` | Lớp học — chứa danh sách học sinh, thời khóa biểu, buổi học |
| `AttendanceManager` | Facade: cổng giao tiếp duy nhất giữa UI và domain |
| `AttendanceReport` | Tạo báo cáo thống kê, xếp hạng, cảnh báo |
| `FileManager` | Đọc/ghi file văn bản thuần |
| `AbsenceReportItem` | DTO chứa kết quả tính toán vắng mặt của từng học sinh |

---

## 📊 Công Thức Nghiệp Vụ

**Tỉ lệ vắng mặt:**
```
ti_le = (so_buoi_vang / tong_so_buoi_co_ghi_nhan) x 100
```
- Vắng = `EXCUSED_ABSENCE` hoặc `UNEXCUSED_ABSENCE`
- Nếu chưa có buổi nào được ghi nhận -> tỉ lệ = `0.0`

**Học sinh có nguy cơ:** tỉ lệ vắng **> 20%**

---

## 🧪 Các Test Case

| File test | Nội dung kiểm tra |
|-----------|-------------------|
| `test_linked_list.py` | Các thao tác `addLast`, `remove`, `find`, `get`, `size` trên `MyLinkedList`; helper `split_line` |
| `test_linked_list_edge_cases.py` | Các trường hợp biên của `MyLinkedList` như `traverse`, `remove` dùng predicate, truy cập index âm hoặc vượt giới hạn |
| `test_student.py` | Constructor và các phương thức `getStudentId`, `getFullName` của `Student` |
| `test_schedule.py` | Constructor và các thuộc tính `dayOfWeek`, `period`, `room` của `Schedule` |
| `test_attendance_status.py` | Hàm kiểm tra `is_valid` và các hằng số `PRESENT`, `EXCUSED_ABSENCE`, `UNEXCUSED_ABSENCE` của `AttendanceStatus` |
| `test_attendance_record.py` | Constructor, `getStatus`, `setStatus` của `AttendanceRecord`, kiểm tra giá trị không hợp lệ |
| `test_session.py` | Các phương thức `recordAttendance`, `findAttendance`, `countPresent` của `Session` |
| `test_school_class.py` | Các phương thức `addSchedule`, `getStudentList`, `findSession`, `calculateAbsenceRate` của `SchoolClass` |
| `test_models.py` | Logic tổng hợp của domain models (Student, SchoolClass, Session, AttendanceRecord) |
| `test_file_manager.py` | Đọc và ghi file của `FileManager` qua `readFile`, `writeFile` |
| `test_report_service.py` | Tạo chuỗi báo cáo theo buổi học qua `reportAttendanceBySession` của `AttendanceReport` |
| `test_attendance_manager.py` | Các phương thức quản lý chính của `AttendanceManager` (`addClass`, `findClassById`, `getAllClasses`, `recordAttendance`, `searchByDate`, `searchByStudentId`) |
| `test_services.py` | Tính toán và sắp xếp trong `AttendanceReport` (`getAbsenceWarningList`, `getMostAbsentStudents`) |
| `test_persistence.py` | Chu trình lưu và tải dữ liệu (`saveData`, `loadData`) thông qua `AttendanceManager` |
| `test_menu.py` | Các helper xử lý nhập liệu từ bàn phím (`_get_non_empty_input`, `_get_int_input`) của `MainProgram` |