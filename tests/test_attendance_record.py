"""Tests for AttendanceRecord model: constructor, getStatus, setStatus, helper attributes."""

from app.core.attendaceStatus import AttendanceStatus
from app.models.student import Student
from app.models.attendance import AttendanceRecord


def _make_student():
    """Helper: creates a default Student."""
    return Student("ST01", "John Doe")


def test_get_status_returns_initial_status():
    print("Testing AttendanceRecord.getStatus - returns initial status...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT)
    assert rec.getStatus() == AttendanceStatus.PRESENT
    print("getStatus returns initial status - passed!")


def test_set_status_updates_status():
    print("Testing AttendanceRecord.setStatus - updates status correctly...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT)
    rec.setStatus(AttendanceStatus.EXCUSED_ABSENCE)
    assert rec.getStatus() == AttendanceStatus.EXCUSED_ABSENCE
    print("setStatus updates status - passed!")


def test_set_status_to_unexcused():
    print("Testing AttendanceRecord.setStatus - set to UNEXCUSED_ABSENCE...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT)
    rec.setStatus(AttendanceStatus.UNEXCUSED_ABSENCE)
    assert rec.getStatus() == AttendanceStatus.UNEXCUSED_ABSENCE
    print("setStatus to UNEXCUSED_ABSENCE - passed!")


def test_constructor_invalid_status_raises():
    print("Testing AttendanceRecord constructor - invalid status raises ValueError...")
    s = _make_student()
    try:
        AttendanceRecord(s, "INVALID_STATUS")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("constructor invalid status raises ValueError - passed!")


def test_set_status_invalid_raises():
    print("Testing AttendanceRecord.setStatus - invalid status raises ValueError...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT)
    try:
        rec.setStatus("WRONG")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("setStatus invalid raises ValueError - passed!")


def test_student_reference_stored():
    print("Testing AttendanceRecord - student reference is stored correctly...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT)
    assert rec.student is s
    assert rec.student.getStudentId() == "ST01"
    assert rec.student.getFullName() == "John Doe"
    print("student reference stored - passed!")


def test_class_id_helper_attribute():
    print("Testing AttendanceRecord - classId helper attribute stored...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT, classId="CS101", date="2026-06-01")
    assert rec.classId == "CS101"
    print("classId helper attribute - passed!")


def test_date_helper_attribute():
    print("Testing AttendanceRecord - date helper attribute stored...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT, classId="CS101", date="2026-06-01")
    assert rec.date == "2026-06-01"
    print("date helper attribute - passed!")


def test_helper_attributes_default_to_none():
    print("Testing AttendanceRecord - classId and date default to None...")
    s = _make_student()
    rec = AttendanceRecord(s, AttendanceStatus.PRESENT)
    assert rec.classId is None
    assert rec.date is None
    print("classId and date default to None - passed!")


if __name__ == "__main__":
    test_get_status_returns_initial_status()
    test_set_status_updates_status()
    test_set_status_to_unexcused()
    test_constructor_invalid_status_raises()
    test_set_status_invalid_raises()
    test_student_reference_stored()
    test_class_id_helper_attribute()
    test_date_helper_attribute()
    test_helper_attributes_default_to_none()
    print("All AttendanceRecord tests passed!")
