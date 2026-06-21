"""Tests for Session model: recordAttendance, findAttendance, countPresent."""

from app.core.attendaceStatus import AttendanceStatus
from app.models.student import Student
from app.models.session import Session
from app.models.school_class import SchoolClass


def _make_class_with_student(class_id="CS101", student_id="ST01", student_name="John Doe"):
    """Helper: creates a SchoolClass with one enrolled student."""
    sc = SchoolClass(class_id, "Computer Science")
    s = Student(student_id, student_name)
    sc.addStudent(s)
    return sc


def test_record_attendance_success():
    print("Testing Session.recordAttendance - success case...")
    sc = _make_class_with_student()
    sess = sc.createSession("2026-06-01")
    sess.recordAttendance("ST01", AttendanceStatus.PRESENT)
    assert sess.attendanceList.size() == 1
    rec = sess.attendanceList.get(0)
    assert rec.getStatus() == AttendanceStatus.PRESENT
    print("recordAttendance success - passed!")


def test_record_attendance_no_class_context():
    print("Testing Session.recordAttendance - no class context raises ValueError...")
    sess = Session("2026-06-01", school_class=None)
    try:
        sess.recordAttendance("ST01", AttendanceStatus.PRESENT)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("recordAttendance no class context - passed!")


def test_record_attendance_student_not_enrolled():
    print("Testing Session.recordAttendance - student not enrolled raises ValueError...")
    sc = SchoolClass("CS101", "Computer Science")
    sess = sc.createSession("2026-06-01")
    try:
        sess.recordAttendance("ST99", AttendanceStatus.PRESENT)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("recordAttendance student not enrolled - passed!")


def test_record_attendance_duplicate_raises():
    print("Testing Session.recordAttendance - duplicate raises ValueError...")
    sc = _make_class_with_student()
    sess = sc.createSession("2026-06-01")
    sess.recordAttendance("ST01", AttendanceStatus.PRESENT)
    try:
        sess.recordAttendance("ST01", AttendanceStatus.EXCUSED_ABSENCE)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("recordAttendance duplicate - passed!")


def test_find_attendance_found():
    print("Testing Session.findAttendance - found...")
    sc = _make_class_with_student()
    sess = sc.createSession("2026-06-01")
    sess.recordAttendance("ST01", AttendanceStatus.EXCUSED_ABSENCE)
    rec = sess.findAttendance("ST01")
    assert rec is not None
    assert rec.getStatus() == AttendanceStatus.EXCUSED_ABSENCE
    print("findAttendance found - passed!")


def test_find_attendance_not_found():
    print("Testing Session.findAttendance - not found returns None...")
    sc = SchoolClass("CS101", "Computer Science")
    sess = sc.createSession("2026-06-01")
    assert sess.findAttendance("ST99") is None
    print("findAttendance not found - passed!")


def test_count_present_mixed():
    print("Testing Session.countPresent - mixed statuses...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John"))
    sc.addStudent(Student("ST02", "Jane"))
    sc.addStudent(Student("ST03", "Bob"))
    sess = sc.createSession("2026-06-01")
    sess.recordAttendance("ST01", AttendanceStatus.PRESENT)
    sess.recordAttendance("ST02", AttendanceStatus.EXCUSED_ABSENCE)
    sess.recordAttendance("ST03", AttendanceStatus.PRESENT)
    assert sess.countPresent() == 2
    print("countPresent mixed - passed!")


def test_count_present_all_absent():
    print("Testing Session.countPresent - all absent...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John"))
    sess = sc.createSession("2026-06-01")
    sess.recordAttendance("ST01", AttendanceStatus.UNEXCUSED_ABSENCE)
    assert sess.countPresent() == 0
    print("countPresent all absent - passed!")


def test_count_present_empty_session():
    print("Testing Session.countPresent - no records returns 0...")
    sc = SchoolClass("CS101", "Computer Science")
    sess = sc.createSession("2026-06-01")
    assert sess.countPresent() == 0
    print("countPresent empty session - passed!")


if __name__ == "__main__":
    test_record_attendance_success()
    test_record_attendance_no_class_context()
    test_record_attendance_student_not_enrolled()
    test_record_attendance_duplicate_raises()
    test_find_attendance_found()
    test_find_attendance_not_found()
    test_count_present_mixed()
    test_count_present_all_absent()
    test_count_present_empty_session()
    print("All Session tests passed!")
