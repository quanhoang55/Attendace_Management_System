# ==========================================================================
# IMPORTS & CONFIGURATION
# ==========================================================================
from enum import Enum
from src.models.schedule import Schedule
from src.models.student import Student
from src.models.class_record import Class


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
