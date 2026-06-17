#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass

# CLASSES / DATA STRUCTURE: Student
#==========================================================================
@dataclass
class Student:
    student_id: str
    full_name: str
