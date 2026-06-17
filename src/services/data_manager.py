import os
from typing import Optional
from models.linked_list import LinkedList, Node
from models.student import Student
from models.class_record import Class
from models.schedule import Schedule, Weekday, Period
from models.attendance_record import AttendanceRecord, Status

class DataManager:
    def __init__(self, data_dir: str = "data"):
        """Initializes DataManager with the data directory path.

        Args:
            data_dir (str): Path to data directory.
        """
        self.data_dir = data_dir
        # Ensure the data directory exists
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            
        self.classes_file = os.path.join(self.data_dir, "classes.txt")
        self.students_file = os.path.join(self.data_dir, "students.txt")
        self.schedules_file = os.path.join(self.data_dir, "schedules.txt")
        self.attendance_file = os.path.join(self.data_dir, "attendance.txt")

    def _read_lines(self, file_path: str) -> list[str]:
        """Helper to read lines from a file, returning clean, non-empty lines.

        Args:
            file_path (str): File path.

        Returns:
            list[str]: Clean lines.
        """
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def _find_class_node(self, classes_list: LinkedList, class_id: str) -> Optional[Node]:
        """Helper to find the Node containing a Class by its ID.

        Args:
            classes_list (LinkedList): List of classes.
            class_id (str): Class ID.

        Returns:
            Optional[Node]: The node containing the class, or None.
        """
        curr = classes_list.head
        while curr is not None:
            if curr.data.class_id == class_id:
                return curr
            curr = curr.next
        return None

    def load_classes(self) -> LinkedList:
        """Loads classes, students, and schedules from files.

        Returns:
            LinkedList: List of Class objects.
        """
        classes_list = LinkedList(None)
        
        # 1. Read class list
        class_lines = self._read_lines(self.classes_file)
        for line in class_lines:
            parts = line.split("|")
            if len(parts) == 2:
                class_id, class_name = parts
                new_class = Class(
                    class_id=class_id,
                    class_name=class_name,
                    students=LinkedList(None),
                    schedules=LinkedList(None)
                )
                classes_list.appendLast(new_class)

        # 2. Read student list
        student_lines = self._read_lines(self.students_file)
        for line in student_lines:
            parts = line.split("|")
            if len(parts) == 3:
                class_id, student_id, full_name = parts
                class_node = self._find_class_node(classes_list, class_id)
                if class_node is not None:
                    student = Student(student_id=student_id, full_name=full_name)
                    class_node.data.students.appendLast(student)

        # 3. Read schedule list
        schedule_lines = self._read_lines(self.schedules_file)
        for line in schedule_lines:
            parts = line.split("|")
            if len(parts) == 4:
                class_id, weekday_str, period_str, room_str = parts
                class_node = self._find_class_node(classes_list, class_id)
                if class_node is not None:
                    schedule = Schedule(
                        weekday=Weekday(int(weekday_str)),
                        period=Period(int(period_str)),
                        room=room_str
                    )
                    class_node.data.schedules.appendLast(schedule)

        return classes_list

    def save_classes(self, classes_list: LinkedList):
        """Saves classes, students, and schedules to files.

        Args:
            classes_list (LinkedList): List of Class objects.
        """
        with open(self.classes_file, "w", encoding="utf-8") as fc, \
             open(self.students_file, "w", encoding="utf-8") as fs, \
             open(self.schedules_file, "w", encoding="utf-8") as fsch:
            
            curr_class = classes_list.head
            while curr_class is not None:
                c: Class = curr_class.data
                # Write class basic info
                fc.write(f"{c.class_id}|{c.class_name}\n")
                
                # Write students of this class
                curr_student = c.students.head
                while curr_student is not None:
                    s: Student = curr_student.data
                    fs.write(f"{c.class_id}|{s.student_id}|{s.full_name}\n")
                    curr_student = curr_student.next
                
                # Write schedules of this class
                curr_sch = c.schedules.head
                while curr_sch is not None:
                    sch: Schedule = curr_sch.data
                    fsch.write(f"{c.class_id}|{sch.weekday.value}|{sch.period.value}|{sch.room}\n")
                    curr_sch = curr_sch.next
                
                curr_class = curr_class.next

    def load_attendance(self) -> LinkedList:
        """Loads attendance records from file.

        Returns:
            LinkedList: List of AttendanceRecord objects.
        """
        attendance_list = LinkedList(None)
        lines = self._read_lines(self.attendance_file)
        for line in lines:
            parts = line.split("|")
            if len(parts) == 4:
                class_id, date, student_id, status_str = parts
                record = AttendanceRecord(
                    class_id=class_id,
                    date=date,
                    student_id=student_id,
                    status=Status(status_str)
                )
                attendance_list.appendLast(record)
        return attendance_list

    def save_attendance(self, attendance_list: LinkedList):
        """Saves attendance records to file.

        Args:
            attendance_list (LinkedList): List of AttendanceRecord objects.
        """
        with open(self.attendance_file, "w", encoding="utf-8") as f:
            curr = attendance_list.head
            while curr is not None:
                r: AttendanceRecord = curr.data
                f.write(f"{r.class_id}|{r.date}|{r.student_id}|{r.status.value}\n")
                curr = curr.next
