#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass, field
import uuid
from enum import IntEnum, Enum
from models.schedule import Schedule
from models.student import Student

#==========================================================================
# CLASSES / DATA STRUCTURE: Status
#==========================================================================
class Status(Enum):
    CM = "Co mat"
    VCP = "Vang mat co phep"
    VKP = "Vang mat khong phep"

#==========================================================================
# CLASSES / DATA STRUCTURE: Attendance Record
#==========================================================================

@dataclass(frozen=True)
class AttendanceRecord:
    class_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    date: Schedule
    student_id: str = Student.student_id
    status: Status