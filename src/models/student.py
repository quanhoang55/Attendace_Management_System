from __future__ import annotations
#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass
#==========================================================================
# CLASSES / DATA STRUCTURE: Student Id
#==========================================================================
@dataclass
class Student_ID:
    ID: str
#==========================================================================
# CLASSES / DATA STRUCTURE: Student
#==========================================================================
@dataclass
class Student:
    student_id: Student_ID
    full_name: str
