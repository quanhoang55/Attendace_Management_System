#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass
from models.student import Student
from models.linked_list import Node, LinkedList

#==========================================================================
# CLASSES / DATA STRUCTURE: StudentList
#==========================================================================
@dataclass
# Inheriting from Linked-List
class StudentList(LinkedList):
    pass