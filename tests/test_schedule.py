"""Tests for Schedule model: constructor and attribute access."""

from app.models.schedule import Schedule


def test_schedule_attributes():
    print("Testing Schedule attributes...")
    sch = Schedule(2, 1, "A101")
    assert sch.dayOfWeek == 2
    assert sch.period == 1
    assert sch.room == "A101"
    print("Schedule attributes - passed!")


def test_schedule_different_days():
    print("Testing Schedule with different day values (2=Mon ... 8=Sun)...")
    for day in range(2, 9):
        sch = Schedule(day, 3, "B202")
        assert sch.dayOfWeek == day
    print("Schedule different days - passed!")


def test_schedule_different_periods():
    print("Testing Schedule with different period values...")
    for period in range(1, 7):
        sch = Schedule(3, period, "C303")
        assert sch.period == period
    print("Schedule different periods - passed!")


if __name__ == "__main__":
    test_schedule_attributes()
    test_schedule_different_days()
    test_schedule_different_periods()
    print("All Schedule tests passed!")
