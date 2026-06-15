#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================

#==========================================================================
# CLASSES / DATA STRUCTURE: Attendance Record
#==========================================================================
class AttendanceRecord:
    def __init__(self, myClass = None, student = None):
        self.class_id = myClass.id
        self.date = myClass.schedule
