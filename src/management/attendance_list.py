# ==========================================================================
# IMPORTS & CONFIGURATION
# ==========================================================================
from src.models.attendance_record import AttendanceRecord
from src.models.student import Student_ID

# from src.models.class_record import Class
from src.models.linked_list import Node, LinkedList


# ==========================================================================
# CLASSES / DATA STRUCTURE: StudentList
# ==========================================================================
# Inheriting from Linked-List
class AttendanceList(LinkedList):
    def __init__(self, record: AttendanceRecord):
        self.head = Node(record)

    def isBanned(self, student_id: Student_ID, class_id):
        pass
