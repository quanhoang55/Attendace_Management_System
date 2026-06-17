# ==========================================================================
# IMPORTS & CONFIGURATION
# ==========================================================================
from src.models.student import Student, Student_ID
from src.models.linked_list import Node, LinkedList
from typing import Optional


# ==========================================================================
# CLASSES / DATA STRUCTURE: StudentList
# ==========================================================================
# Inheriting from Linked-List
class StudentList(LinkedList):
    def __init__(self, student: Optional[Student]):
        """Init Student List

        Args:
            student (Optional[Student]): student class
        """
        self.head = Node(student)


# ==========================================================================
# Testing: PASS
# ==========================================================================
def print_list(lst: LinkedList):
    """Helper function to print the current state of the list"""
    current = lst.head
    elements = []
    while current is not None:
        if current.data:
            elements.append(f"[{current.data.student_id.ID}: {current.data.full_name}]")
        else:
            elements.append("[None]")
        current = current.next
    print(" -> ".join(elements) if elements else "Empty List")


# ==========================================================================
# Test: Pass
# ==========================================================================


def main():
    print("--- 1. Initializing Students ---")
    # Create students using your @dataclass models
    student1 = Student(student_id=Student_ID("STU001"), full_name="Alice Smith")
    student2 = Student(student_id=Student_ID("STU002"), full_name="Bob Jones")
    student3 = Student(student_id=Student_ID("STU003"), full_name="Charlie Brown")

    # Notice how clean the print output is because of @dataclass!
    print(student1)
    print(student2)
    print(student3)
    print("\n--- 2. Initializing Student List ---")

    # Create a list with the first student as the head
    student_list = StudentList(student1)

    print_list(student_list)

    print("\n--- 3. Testing appendLast ---")
    # Add Charlie to the end of the list
    student_list.appendLast(student3)
    print_list(student_list)

    print("\n--- 4. Testing appendFirst ---")
    # Add Bob to the beginning of the list
    student_list.appendFirst(student2)
    print_list(student_list)

    print("\n--- 5. Testing search ---")
    # Search for an existing student object
    found_node = student_list.search(student3)
    if found_node:
        print(f"Found: {found_node.data.full_name}")
    else:
        print("Student not found.")

    print("\n--- 6. Testing swap ---")
    # Swap Alice and Charlie in the list
    print("Before swap:")
    print_list(student_list)
    student_list.swap(student1, student3)
    print("After swapping Alice and Charlie:")
    print_list(student_list)

    print("\n--- 7. Testing delete ---")
    # Delete Bob (who is currently at the front)
    student_list.delete(student2)
    print("After deleting Bob:")
    print_list(student_list)


if __name__ == "__main__":
    main()
