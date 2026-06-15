#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
import uuid

#==========================================================================
# CLASSES / DATA STRUCTURE: __BLUEPRINT__
#==========================================================================

class Student:
    def __init__(self, full_name: str):
        """Student Class

        Args:
            full_name (str): student's full name
        """        
        self.stuent_id = str(uuid.uuid4())
        self.full_name = full_name