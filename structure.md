# 🗂️ Sơ Đồ Cấu Trúc Project

## Sơ Đồ Cây Thư Mục

```
ktlt_project/
│
├── 📄 main.py
├── 📄 README.md
├── 📄 structure.md
├── 📄 guide.txt
├── 📄 test_run_guide.txt
├── 📄 classdiagram.mmd
├── 🖼️ class_diagram.png
├── 📄 .gitignore
│
├── 📁 app/
│   ├── 📄 __init__.py
│   │
│   ├── 📁 core/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 attendaceStatus.py
│   │   └── 📄 linked_list.py
│   │
│   ├── 📁 models/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 attendance.py
│   │   ├── 📄 schedule.py
│   │   ├── 📄 school_class.py
│   │   ├── 📄 session.py
│   │   └── 📄 student.py
│   │
│   ├── 📁 services/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 attendance_manager.py
│   │   ├── 📄 file_manager.py
│   │   └── 📄 report_service.py
│   │
│   └── 📁 ui/
│       ├── 📄 __init__.py
│       └── 📄 menu.py
│
├── 📁 tests/
│   ├── 📄 __init__.py
│   ├── 📄 test_attendance_manager.py
│   ├── 📄 test_attendance_record.py
│   ├── 📄 test_attendance_status.py
│   ├── 📄 test_file_manager.py
│   ├── 📄 test_linked_list.py
│   ├── 📄 test_linked_list_edge_cases.py
│   ├── 📄 test_menu.py
│   ├── 📄 test_models.py
│   ├── 📄 test_persistence.py
│   ├── 📄 test_report_service.py
│   ├── 📄 test_schedule.py
│   ├── 📄 test_school_class.py
│   ├── 📄 test_services.py
│   ├── 📄 test_session.py
│   └── 📄 test_student.py
│
└── 📁 data/
    ├── 📄 attendance.txt
    ├── 📄 classes.txt
    ├── 📄 schedules.txt
    ├── 📄 sessions.txt
    └── 📄 students.txt
```

---

## Sơ Đồ Mermaid

```mermaid
graph TD
    ROOT["📁 ktlt_project/"]

    ROOT --> MAIN["📄 main.py<br/><i>Entry point</i>"]
    ROOT --> README["📄 README.md"]
    ROOT --> DOCS["📄 structure.md, guide.txt, test_run_guide.txt"]

    ROOT --> APP["📁 app/"]
    ROOT --> TESTS["📁 tests/"]
    ROOT --> DATA["📁 data/"]

    APP --> CORE["📁 core/"]
    APP --> MODELS["📁 models/"]
    APP --> SERVICES["📁 services/"]
    APP --> UI["📁 ui/"]

    CORE --> LL["📄 linked_list.py<br/><i>MyLinkedList, Node</i>"]
    CORE --> CONST["📄 attendaceStatus.py<br/><i>AttendanceStatus</i>"]

    MODELS --> ST["📄 student.py<br/><i>Student</i>"]
    MODELS --> SCH["📄 schedule.py<br/><i>Schedule</i>"]
    MODELS --> ATT["📄 attendance.py<br/><i>AttendanceRecord</i>"]
    MODELS --> SESS["📄 session.py<br/><i>Session</i>"]
    MODELS --> SC["📄 school_class.py<br/><i>SchoolClass</i>"]

    SERVICES --> FM["📄 file_manager.py<br/><i>FileManager</i>"]
    SERVICES --> RS["📄 report_service.py<br/><i>AttendanceReport<br/>AbsenceReportItem</i>"]
    SERVICES --> AM["📄 attendance_manager.py<br/><i>AttendanceManager</i>"]

    UI --> MENU["📄 menu.py<br/><i>MainProgram</i>"]

    TESTS --> T_MGR["📄 test_attendance_manager.py"]
    TESTS --> T_REC["📄 test_attendance_record.py"]
    TESTS --> T_STAT["📄 test_attendance_status.py"]
    TESTS --> T_FM["📄 test_file_manager.py"]
    TESTS --> T_LL["📄 test_linked_list.py"]
    TESTS --> T_LLE["📄 test_linked_list_edge_cases.py"]
    TESTS --> T_MENU["📄 test_menu.py"]
    TESTS --> T_MOD["📄 test_models.py"]
    TESTS --> T_PER["📄 test_persistence.py"]
    TESTS --> T_REP["📄 test_report_service.py"]
    TESTS --> T_SCH["📄 test_schedule.py"]
    TESTS --> T_SC["📄 test_school_class.py"]
    TESTS --> T_SER["📄 test_services.py"]
    TESTS --> T_SESS["📄 test_session.py"]
    TESTS --> T_STU["📄 test_student.py"]

    DATA --> D1["📄 attendance.txt"]
    DATA --> D2["📄 classes.txt"]
    DATA --> D3["📄 schedules.txt"]
    DATA --> D4["📄 sessions.txt"]
    DATA --> D5["📄 students.txt"]
```

---

## Mô Tả Nhanh Từng Thành Phần

| Thư mục / File | Mô tả |
|----------------|-------|
| `main.py` | Entry point — khởi động `MainProgram` |
| `app/core/linked_list.py` | Cấu trúc dữ liệu tự cài: `Node` + `MyLinkedList` |
| `app/core/attendaceStatus.py` | Hằng số `AttendanceStatus` (PRESENT / EXCUSED / UNEXCUSED) |
| `app/models/student.py` | Thông tin học sinh |
| `app/models/schedule.py` | Thời khóa biểu (thứ, tiết, phòng) |
| `app/models/attendance.py` | Bản ghi điểm danh của một học sinh trong một buổi |
| `app/models/session.py` | Một buổi học cụ thể (lớp + ngày) |
| `app/models/school_class.py` | Lớp học, chứa danh sách học sinh / lịch / buổi học |
| `app/services/file_manager.py` | Đọc và ghi file văn bản thuần |
| `app/services/report_service.py` | Báo cáo thống kê, xếp hạng vắng, cảnh báo nguy cơ |
| `app/services/attendance_manager.py` | Facade: điều phối toàn bộ hệ thống, lưu/tải dữ liệu |
| `app/ui/menu.py` | Giao diện menu CLI (12 chức năng) |
| `tests/` | Chứa 15 file test bao phủ toàn bộ các module trong `app/` |
| `data/` | File lưu trữ dữ liệu dạng text (pipe-delimited) |
