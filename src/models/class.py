import uuid

class Class:    
    def __init__(self, class_name: str, students, schedules, next):
        """Class Object

        Args:
            class_id: generated with uuid
            class_name (str): class name
            students (_type_): _description_
            schedules (_type_): _description_
            next (): _description_
        """        
        self.class_id = str(uuid.uuid4())
        self.students = students
        self.schedules = schedules
        self.next = next