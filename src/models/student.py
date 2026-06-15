#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
import uuid
from dataclasses import dataclass, field

#==========================================================================
# CLASSES / DATA STRUCTURE: __BLUEPRINT__
#==========================================================================

@dataclass
class Student:
    student_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    full_name: str