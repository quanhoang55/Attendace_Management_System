"""Tests for AttendanceStatus: validation of allowed status values."""

from app.core.attendaceStatus import AttendanceStatus


def test_is_valid_present():
    print("Testing AttendanceStatus.is_valid - PRESENT...")
    assert AttendanceStatus.is_valid(AttendanceStatus.PRESENT) is True
    print("PRESENT valid - passed!")


def test_is_valid_excused_absence():
    print("Testing AttendanceStatus.is_valid - EXCUSED_ABSENCE...")
    assert AttendanceStatus.is_valid(AttendanceStatus.EXCUSED_ABSENCE) is True
    print("EXCUSED_ABSENCE valid - passed!")


def test_is_valid_unexcused_absence():
    print("Testing AttendanceStatus.is_valid - UNEXCUSED_ABSENCE...")
    assert AttendanceStatus.is_valid(AttendanceStatus.UNEXCUSED_ABSENCE) is True
    print("UNEXCUSED_ABSENCE valid - passed!")


def test_is_valid_rejects_invalid_string():
    print("Testing AttendanceStatus.is_valid - invalid strings...")
    assert AttendanceStatus.is_valid("INVALID") is False
    assert AttendanceStatus.is_valid("present") is False
    assert AttendanceStatus.is_valid("") is False
    assert AttendanceStatus.is_valid("ABSENT") is False
    print("Invalid strings rejected - passed!")


def test_status_constants():
    print("Testing AttendanceStatus constants...")
    assert AttendanceStatus.PRESENT == "PRESENT"
    assert AttendanceStatus.EXCUSED_ABSENCE == "EXCUSED_ABSENCE"
    assert AttendanceStatus.UNEXCUSED_ABSENCE == "UNEXCUSED_ABSENCE"
    print("Status constants - passed!")


if __name__ == "__main__":
    test_is_valid_present()
    test_is_valid_excused_absence()
    test_is_valid_unexcused_absence()
    test_is_valid_rejects_invalid_string()
    test_status_constants()
    print("All AttendanceStatus tests passed!")
