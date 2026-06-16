#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
import uuid
from dataclasses import dataclass, field
from models.student import Student
from models.schedule import Schedule, Room

#==========================================================================
# CLASSES / DATA STRUCTURE: Class
#==========================================================================

@dataclass()
class Class:    
    class_id: str =  field(default_factory=lambda: str(uuid.uuid4()))
    class_name: str
    students: Student
    schedule: Schedule