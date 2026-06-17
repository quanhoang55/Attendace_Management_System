#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from src.models.schedule import Schedule
from src.management.student_list import StudentList
from typing import Optional

#==========================================================================
# CLASSES / DATA STRUCTURE: Class
#==========================================================================

class Class:
    def __init__(self, class_id: str, class_name: str, students: Optional[StudentList], schedule: Schedule):
        """Init class

        Args:
            class_id (str): Class Id
            class_name (str): Class Name
            students (Optional[StudentList]): Student List (Inheritring from Linked List)
            schedule (Schedule): schedule
        """        
        self.class_id = class_id
        self.class_name = class_name
        self.students = students
        self.schedule = schedule