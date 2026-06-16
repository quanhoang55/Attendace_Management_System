#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass
from models.class_record import Class
from models.linked_list import Node, LinkedList

#==========================================================================
# CLASSES / DATA STRUCTURE: StudentList
#==========================================================================
@dataclass
# Inheriting from Linked-List
class ClassList(LinkedList):
    pass