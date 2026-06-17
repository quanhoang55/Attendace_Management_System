#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass
from enum import Enum

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

@dataclass
class AttendanceRecord:
    class_id: str
    date: str
    student_id: str
    status: Status