#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from models.linked_list import LinkedList
import uuid
from dataclasses import dataclass, field
from models.student import Student
from models.schedule import Schedule

#==========================================================================
# CLASSES / DATA STRUCTURE: Class
#==========================================================================

@dataclass()
class Class:    
    class_id: str
    class_name: str
    students: LinkedList
    schedules: LinkedList