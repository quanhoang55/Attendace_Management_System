"""Tests for Student model: constructor, getStudentId, getFullName."""

from app.models.student import Student


def test_student_get_id():
    print("Testing Student.getStudentId...")
    s = Student("ST01", "John Doe")
    assert s.getStudentId() == "ST01"
    print("getStudentId - passed!")


def test_student_get_full_name():
    print("Testing Student.getFullName...")
    s = Student("ST01", "John Doe")
    assert s.getFullName() == "John Doe"
    print("getFullName - passed!")


def test_student_attributes_stored_correctly():
    print("Testing Student attributes stored correctly...")
    s = Student("ST99", "Nguyen Van A")
    assert s.studentId == "ST99"
    assert s.fullName == "Nguyen Van A"
    print("Student attributes stored correctly - passed!")


def test_student_id_and_name_are_independent():
    print("Testing Student ID and name are independent across instances...")
    s1 = Student("ST01", "John Doe")
    s2 = Student("ST02", "Jane Smith")
    assert s1.getStudentId() != s2.getStudentId()
    assert s1.getFullName() != s2.getFullName()
    print("Student independence across instances - passed!")


def test_student_id_with_special_characters():
    print("Testing Student with various ID formats...")
    s = Student("2251234567", "Tran Thi B")
    assert s.getStudentId() == "2251234567"
    assert s.getFullName() == "Tran Thi B"
    print("Student numeric ID format - passed!")


if __name__ == "__main__":
    test_student_get_id()
    test_student_get_full_name()
    test_student_attributes_stored_correctly()
    test_student_id_and_name_are_independent()
    test_student_id_with_special_characters()
    print("All Student tests passed!")
