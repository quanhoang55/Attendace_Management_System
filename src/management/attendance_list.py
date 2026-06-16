#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass
from models.attendance_record import AttendanceRecord
from models.linked_list import Node, LinkedList

#==========================================================================
# CLASSES / DATA STRUCTURE: StudentList
#==========================================================================
@dataclass
# Inheriting from Linked-List
class AttendanceList(LinkedList):
    pass