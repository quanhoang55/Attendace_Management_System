"""Tests for SchoolClass: addSchedule, getStudentList, findSession, calculateAbsenceRate edge cases."""

from app.core.attendaceStatus import AttendanceStatus
from app.models.student import Student
from app.models.schedule import Schedule
from app.models.school_class import SchoolClass


def test_add_schedule_success():
    print("Testing SchoolClass.addSchedule - success case...")
    sc = SchoolClass("CS101", "Computer Science")
    sch = Schedule(2, 1, "A101")
    sc.addSchedule(sch)
    assert sc.scheduleList.size() == 1
    assert sc.scheduleList.get(0).room == "A101"
    print("addSchedule success - passed!")


def test_add_multiple_schedules():
    print("Testing SchoolClass.addSchedule - multiple entries...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.addSchedule(Schedule(2, 1, "A101"))
    sc.addSchedule(Schedule(4, 2, "B202"))
    assert sc.scheduleList.size() == 2
    print("addSchedule multiple entries - passed!")


def test_get_student_list_returns_enrolled():
    print("Testing SchoolClass.getStudentList - returns correct list...")
    sc = SchoolClass("CS101", "Computer Science")
    s1 = Student("ST01", "John Doe")
    s2 = Student("ST02", "Jane Smith")
    sc.addStudent(s1)
    sc.addStudent(s2)
    lst = sc.getStudentList()
    assert lst.size() == 2
    assert lst.get(0).getStudentId() == "ST01"
    assert lst.get(1).getStudentId() == "ST02"
    print("getStudentList returns enrolled - passed!")


def test_find_session_not_found_returns_none():
    print("Testing SchoolClass.findSession - not found returns None...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.createSession("2026-06-01")
    result = sc.findSession("2026-12-31")
    assert result is None
    print("findSession not found returns None - passed!")


def test_calculate_absence_rate_no_records_returns_zero():
    print("Testing SchoolClass.calculateAbsenceRate - no sessions returns 0.0...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John Doe"))
    rate = sc.calculateAbsenceRate("ST01")
    assert rate == 0.0
    print("calculateAbsenceRate no sessions returns 0.0 - passed!")


def test_calculate_absence_rate_all_present():
    print("Testing SchoolClass.calculateAbsenceRate - all present returns 0.0...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John Doe"))
    sess1 = sc.createSession("2026-06-01")
    sess2 = sc.createSession("2026-06-02")
    sess1.recordAttendance("ST01", AttendanceStatus.PRESENT)
    sess2.recordAttendance("ST01", AttendanceStatus.PRESENT)
    assert sc.calculateAbsenceRate("ST01") == 0.0
    print("calculateAbsenceRate all present - passed!")


def test_calculate_absence_rate_all_absent():
    print("Testing SchoolClass.calculateAbsenceRate - all absent returns 100.0...")
    sc = SchoolClass("CS101", "Computer Science")
    sc.addStudent(Student("ST01", "John Doe"))
    sess1 = sc.createSession("2026-06-01")
    sess2 = sc.createSession("2026-06-02")
    sess1.recordAttendance("ST01", AttendanceStatus.UNEXCUSED_ABSENCE)
    sess2.recordAttendance("ST01", AttendanceStatus.EXCUSED_ABSENCE)
    assert sc.calculateAbsenceRate("ST01") == 100.0
    print("calculateAbsenceRate all absent - passed!")


if __name__ == "__main__":
    test_add_schedule_success()
    test_add_multiple_schedules()
    test_get_student_list_returns_enrolled()
    test_find_session_not_found_returns_none()
    test_calculate_absence_rate_no_records_returns_zero()
    test_calculate_absence_rate_all_present()
    test_calculate_absence_rate_all_absent()
    print("All SchoolClass additional tests passed!")
