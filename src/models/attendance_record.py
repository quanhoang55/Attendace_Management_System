# ==========================================================================
# IMPORTS & CONFIGURATION
# ==========================================================================
from enum import Enum
from models.student import Student, Student_ID
from models.class_record import Class
from models.schedule import Schedule, Weekday, Period, Room


# ==========================================================================
# CLASSES / DATA STRUCTURE: Status
# ==========================================================================
class Status(Enum):
    CM = "Co mat"
    VCP = "Vang mat co phep"
    VKP = "Vang mat khong phep"


# ==========================================================================
# CLASSES / DATA STRUCTURE: Attendance Record
# ==========================================================================
class AttendanceRecord:
    def __init__(self, class_ob: Class, student: Student, status: Status):
        self.class_id = class_ob.class_id
        self.date = class_ob.schedule
        if class_ob.students.search(student) is not None:
            self.student_id = student.student_id
            self.status = status


# ==========================================================================
# Test: Pass
# ==========================================================================
class MockNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MockStudentList:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def search(self, student):
        return MockNode(student) if student in self.students else None


def main():
    print("--- 1. Constructing Schedule & Class Entities ---")

    # Instantiate your specific Schedule format
    class_schedule = Schedule(
        weekday=Weekday.WEDNESDAY, period=Period.WEEK2, room=Room.NO3
    )

    # Initialize mock students and lists
    student_id = Student_ID("STU99")
    alice = Student(student_id=student_id, full_name="Alice Nguyen")

    student_list = MockStudentList()
    student_list.add(alice)

    # Initialize the main Class record
    python_class = Class(
        class_id="PY101",
        class_name="Python Core",
        students=student_list,
        schedule=class_schedule,
    )

    print(f"Class Schedule Object Created: {python_class.schedule}")

    print("\n--- 2. Instantiating AttendanceRecord ---")
    # Mark Alice present (CM)
    record = AttendanceRecord(class_ob=python_class, student=alice, status=Status.CM)

    # Inspect all saved values inside the generated record
    print(f"Recorded Class ID : {record.class_id}")
    print(f"Recorded Student ID: {record.student_id.ID}")
    print(f"Attendance Status  : {record.status.value} ({record.status.name})")

    print("\n--- 3. Verifying Schedule Data Inside AttendanceRecord ---")
    # Access inner properties of your custom schedule instance
    print(
        f"Day of the Week    : {record.date.weekday.name} (Value: {record.date.weekday})"
    )
    print(
        f"Assigned Period    : {record.date.period.name} (Value: {record.date.period})"
    )
    print(
        f"Assigned Room Location: Room {record.date.room.name} (Value: {record.date.room})"
    )


if __name__ == "__main__":
    main()
