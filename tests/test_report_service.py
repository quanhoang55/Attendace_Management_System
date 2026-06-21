"""Tests for AttendanceReport.reportAttendanceBySession: count and format."""

from app.core.attendaceStatus import AttendanceStatus
from app.models.student import Student
from app.models.school_class import SchoolClass
from app.services.report_service import AttendanceReport


def _make_session_with_students():
    """Helper: creates a class with 3 students and one session."""
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John Doe"))
    sc.addStudent(Student("ST02", "Jane Smith"))
    sc.addStudent(Student("ST03", "Bob Johnson"))
    sess = sc.createSession("2026-06-01")
    return sc, sess


def test_report_by_session_counts_present_and_absences():
    print("Testing AttendanceReport.reportAttendanceBySession - counts present and absences...")
    sc, sess = _make_session_with_students()
    sess.recordAttendance("ST01", AttendanceStatus.PRESENT)
    sess.recordAttendance("ST02", AttendanceStatus.EXCUSED_ABSENCE)
    sess.recordAttendance("ST03", AttendanceStatus.UNEXCUSED_ABSENCE)

    report = AttendanceReport()
    report_str = report.reportAttendanceBySession(sess)

    assert "Present Students        : 1" in report_str
    assert "Excused Absences        : 1" in report_str
    assert "Unexcused Absences      : 1" in report_str
    assert "Total Enrolled Students : 3" in report_str
    assert "Not Yet Recorded        : 0" in report_str
    print("reportAttendanceBySession counts - passed!")


def test_report_by_session_contains_date():
    print("Testing AttendanceReport.reportAttendanceBySession - contains session date...")
    sc, sess = _make_session_with_students()
    report = AttendanceReport()
    report_str = report.reportAttendanceBySession(sess)
    assert "2026-06-01" in report_str
    print("reportAttendanceBySession contains date - passed!")


def test_report_by_session_not_yet_recorded():
    print("Testing AttendanceReport.reportAttendanceBySession - counts not yet recorded...")
    sc, sess = _make_session_with_students()
    # Only record ST01, leaving ST02 and ST03 unrecorded
    sess.recordAttendance("ST01", AttendanceStatus.PRESENT)

    report = AttendanceReport()
    report_str = report.reportAttendanceBySession(sess)

    assert "Present Students        : 1" in report_str
    assert "Not Yet Recorded        : 2" in report_str
    print("reportAttendanceBySession not yet recorded - passed!")


def test_report_by_session_all_present():
    print("Testing AttendanceReport.reportAttendanceBySession - all present...")
    sc, sess = _make_session_with_students()
    sess.recordAttendance("ST01", AttendanceStatus.PRESENT)
    sess.recordAttendance("ST02", AttendanceStatus.PRESENT)
    sess.recordAttendance("ST03", AttendanceStatus.PRESENT)

    report = AttendanceReport()
    report_str = report.reportAttendanceBySession(sess)

    assert "Present Students        : 3" in report_str
    assert "Excused Absences        : 0" in report_str
    assert "Unexcused Absences      : 0" in report_str
    assert "Not Yet Recorded        : 0" in report_str
    print("reportAttendanceBySession all present - passed!")


def test_report_by_session_empty():
    print("Testing AttendanceReport.reportAttendanceBySession - no records...")
    sc, sess = _make_session_with_students()
    report = AttendanceReport()
    report_str = report.reportAttendanceBySession(sess)

    assert "Present Students        : 0" in report_str
    assert "Not Yet Recorded        : 3" in report_str
    print("reportAttendanceBySession empty session - passed!")


if __name__ == "__main__":
    test_report_by_session_counts_present_and_absences()
    test_report_by_session_contains_date()
    test_report_by_session_not_yet_recorded()
    test_report_by_session_all_present()
    test_report_by_session_empty()
    print("All AttendanceReport session report tests passed!")
