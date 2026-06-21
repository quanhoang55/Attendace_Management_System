"""Tests for AttendanceManager service: business logic methods not covered by persistence tests."""

import os
import shutil

from app.core.attendaceStatus import AttendanceStatus
from app.models.student import Student
from app.models.school_class import SchoolClass
from app.services.attendance_manager import AttendanceManager

# Use a dedicated temp data directory so tests don't pollute production data
_TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data_test"
)


def _make_manager_with_class():
    """Helper: creates an AttendanceManager with one class and one student."""
    import app.services.attendance_manager as am_module
    am_module._BASE_DIR = _TEST_DATA_DIR

    manager = AttendanceManager()
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John Doe"))
    manager.addClass(sc)
    return manager


def test_add_class_duplicate_raises():
    print("Testing AttendanceManager.addClass - duplicate class ID raises ValueError...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = AttendanceManager()
        sc1 = SchoolClass("CS101", "Computer Science")
        sc2 = SchoolClass("CS101", "Duplicate Class")
        manager.addClass(sc1)
        try:
            manager.addClass(sc2)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
        print("addClass duplicate raises ValueError - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_find_class_by_id_not_found_returns_none():
    print("Testing AttendanceManager.findClassById - not found returns None...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = AttendanceManager()
        result = manager.findClassById("NONEXISTENT")
        assert result is None
        print("findClassById not found returns None - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_find_class_by_id_found():
    print("Testing AttendanceManager.findClassById - found...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = _make_manager_with_class()
        result = manager.findClassById("CS101")
        assert result is not None
        assert result.className == "Computer Science"
        print("findClassById found - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_get_all_classes_returns_all():
    print("Testing AttendanceManager.getAllClasses - returns full list...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = AttendanceManager()
        manager.addClass(SchoolClass("CS101", "Computer Science"))
        manager.addClass(SchoolClass("MA101", "Mathematics"))
        lst = manager.getAllClasses()
        assert lst.size() == 2
        print("getAllClasses returns all - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_record_attendance_class_not_found_raises():
    print("Testing AttendanceManager.recordAttendance - class not found raises ValueError...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = AttendanceManager()
        try:
            manager.recordAttendance("NONEXISTENT", "2026-06-01", "ST01", AttendanceStatus.PRESENT)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
        print("recordAttendance class not found - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_record_attendance_student_not_found_raises():
    print("Testing AttendanceManager.recordAttendance - student not found raises ValueError...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = _make_manager_with_class()
        try:
            manager.recordAttendance("CS101", "2026-06-01", "ST99", AttendanceStatus.PRESENT)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
        print("recordAttendance student not found - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_record_attendance_creates_session_if_missing():
    print("Testing AttendanceManager.recordAttendance - creates session if not exists...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = _make_manager_with_class()
        manager.recordAttendance("CS101", "2026-06-01", "ST01", AttendanceStatus.PRESENT)
        sc = manager.findClassById("CS101")
        sess = sc.findSession("2026-06-01")
        assert sess is not None
        assert sess.findAttendance("ST01").getStatus() == AttendanceStatus.PRESENT
        print("recordAttendance creates session if missing - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_search_by_date_class_not_found_raises():
    print("Testing AttendanceManager.searchByDate - class not found raises ValueError...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = AttendanceManager()
        try:
            manager.searchByDate("NONEXISTENT", "2026-06-01")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
        print("searchByDate class not found - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_search_by_date_found():
    print("Testing AttendanceManager.searchByDate - returns correct session...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = _make_manager_with_class()
        sc = manager.findClassById("CS101")
        sc.createSession("2026-06-10")
        sess = manager.searchByDate("CS101", "2026-06-10")
        assert sess is not None
        assert sess.date == "2026-06-10"
        print("searchByDate found - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_search_by_date_not_found_returns_none():
    print("Testing AttendanceManager.searchByDate - date not found returns None...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = _make_manager_with_class()
        sess = manager.searchByDate("CS101", "2026-12-31")
        assert sess is None
        print("searchByDate not found returns None - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_search_by_student_id_cross_class():
    print("Testing AttendanceManager.searchByStudentId - collects records across classes...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = AttendanceManager()

        sc1 = SchoolClass("CS101", "Computer Science")
        sc1.addStudent(Student("ST01", "John Doe"))
        sess1 = sc1.createSession("2026-06-01")
        sess1.recordAttendance("ST01", AttendanceStatus.PRESENT)

        sc2 = SchoolClass("MA101", "Mathematics")
        sc2.addStudent(Student("ST01", "John Doe"))
        sess2 = sc2.createSession("2026-06-02")
        sess2.recordAttendance("ST01", AttendanceStatus.EXCUSED_ABSENCE)

        manager.addClass(sc1)
        manager.addClass(sc2)

        records = manager.searchByStudentId("ST01")
        assert records.size() == 2
        print("searchByStudentId cross-class - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_search_by_student_id_not_found_returns_empty():
    print("Testing AttendanceManager.searchByStudentId - not found returns empty list...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager = _make_manager_with_class()
        records = manager.searchByStudentId("ST99")
        assert records.size() == 0
        print("searchByStudentId not found returns empty - passed!")
    finally:
        am_module._BASE_DIR = original_base


def _make_manager_with_attendance():
    """Helper: creates a manager with 2 students and attendance data across 5 sessions."""
    import app.services.attendance_manager as am_module
    am_module._BASE_DIR = _TEST_DATA_DIR

    manager = AttendanceManager()
    sc = SchoolClass("CS101", "Computer Science")
    s1 = Student("ST01", "John Doe")
    s2 = Student("ST02", "Jane Smith")
    sc.addStudent(s1)
    sc.addStudent(s2)

    # 5 sessions: ST01 has 1 absence (20%), ST02 has 3 absences (60%)
    from app.core.attendaceStatus import AttendanceStatus
    for date in ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05"]:
        sc.createSession(date)

    sc.findSession("2026-06-01").recordAttendance("ST01", AttendanceStatus.PRESENT)
    sc.findSession("2026-06-02").recordAttendance("ST01", AttendanceStatus.PRESENT)
    sc.findSession("2026-06-03").recordAttendance("ST01", AttendanceStatus.PRESENT)
    sc.findSession("2026-06-04").recordAttendance("ST01", AttendanceStatus.PRESENT)
    sc.findSession("2026-06-05").recordAttendance("ST01", AttendanceStatus.EXCUSED_ABSENCE)

    sc.findSession("2026-06-01").recordAttendance("ST02", AttendanceStatus.UNEXCUSED_ABSENCE)
    sc.findSession("2026-06-02").recordAttendance("ST02", AttendanceStatus.PRESENT)
    sc.findSession("2026-06-03").recordAttendance("ST02", AttendanceStatus.UNEXCUSED_ABSENCE)
    sc.findSession("2026-06-04").recordAttendance("ST02", AttendanceStatus.PRESENT)
    sc.findSession("2026-06-05").recordAttendance("ST02", AttendanceStatus.UNEXCUSED_ABSENCE)

    manager.addClass(sc)
    return manager, sc


def test_report_attendance_by_session_via_manager():
    print("Testing AttendanceManager.reportAttendanceBySession - delegates correctly...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager, sc = _make_manager_with_attendance()
        sess = sc.findSession("2026-06-01")
        report_str = manager.reportAttendanceBySession(sess)

        assert "2026-06-01" in report_str
        assert "Present Students" in report_str
        assert "Total Enrolled Students : 2" in report_str
        print("reportAttendanceBySession via manager - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_get_most_absent_students_via_manager():
    print("Testing AttendanceManager.getMostAbsentStudents - returns sorted by absence count...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager, sc = _make_manager_with_attendance()
        items = manager.getMostAbsentStudents(sc)

        assert items.size() == 2
        # ST02 has 3 absences, ST01 has 1 → ST02 should be first
        assert items.get(0).student.getStudentId() == "ST02"
        assert items.get(1).student.getStudentId() == "ST01"
        print("getMostAbsentStudents via manager sorted correctly - passed!")
    finally:
        am_module._BASE_DIR = original_base


def test_get_absence_warning_list_via_manager():
    print("Testing AttendanceManager.getAbsenceWarningList - returns only >20% absence rate...")
    import app.services.attendance_manager as am_module
    original_base = am_module._BASE_DIR
    am_module._BASE_DIR = _TEST_DATA_DIR
    try:
        manager, sc = _make_manager_with_attendance()
        warnings = manager.getAbsenceWarningList(sc)

        # ST02: 60% (warning), ST01: 20% (not warning, threshold is strictly >20%)
        assert warnings.size() == 1
        assert warnings.get(0).student.getStudentId() == "ST02"
        assert warnings.get(0).absenceRate > 20.0
        print("getAbsenceWarningList via manager - passed!")
    finally:
        am_module._BASE_DIR = original_base


if __name__ == "__main__":
    test_add_class_duplicate_raises()
    test_find_class_by_id_not_found_returns_none()
    test_find_class_by_id_found()
    test_get_all_classes_returns_all()
    test_record_attendance_class_not_found_raises()
    test_record_attendance_student_not_found_raises()
    test_record_attendance_creates_session_if_missing()
    test_search_by_date_class_not_found_raises()
    test_search_by_date_found()
    test_search_by_date_not_found_returns_none()
    test_search_by_student_id_cross_class()
    test_search_by_student_id_not_found_returns_empty()
    test_report_attendance_by_session_via_manager()
    test_get_most_absent_students_via_manager()
    test_get_absence_warning_list_via_manager()
    print("All AttendanceManager tests passed!")

