#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from dataclasses import dataclass
from typing import Any, Optional

#==========================================================================
# CLASSES / DATA STRUCTURE: NODE
#==========================================================================
@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None

#==========================================================================
# CLASSES / DATA STRUCTURE: LinkedList
#==========================================================================
class LinkedList:
    def __init__(self, head: Node = None):
        """Init Linked-List

        Args:
            head (Node, optional): The Beginning of this Linked-List. Defaults to None.
        """        
        self.head = head

    def appendFirst(self, value):
        """Adds a new node to the beginning of the list.

        Args:
            value (Node): Node we want to add
        """        
        # check is this head None or Not
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def appendLast(self, value):
        """Adds a new node to the end of the list.

        Args:
            value (Node): None we want to add
        """    
        # check is this head None or Not    
        if self.head is None:
            self.head = Node(value)
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(value)

    def delete(self, value):
        """Removes the first node that matches the given value.

        Args:
            value (Node): Node we want to delete
        """
        # check is this head None or Not
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        tmp = self.head
        while tmp.next is not None:
            if tmp.next.data == value:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next

    def search(self, value) -> bool:
        """Returns Node if the value exists in the list, otherwise None.

        Args:
            value (Node): Node we want to search

        Returns:
            Node
        """        
        tmp = self.head
        while tmp is not None:
            if tmp.data == value:
                return tmp
            tmp = tmp.next
        return None
