import unittest
from app.services.file_manager import FileManager
from app.services.report_service import AttendanceReport
from app.services.attendance_manager import AttendanceManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_file(self):
        pass

    def test_write_file(self):
        pass


class TestReportService(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_report(self):
        pass

    def test_absence_calculation(self):
        pass


class TestAttendanceManager(unittest.TestCase):
    def setUp(self):
        pass

    def test_attendance_manager_initialization(self):
        pass

    def test_save_data(self):
        pass

    def test_load_data(self):
        pass


if __name__ == '__main__':
    unittest.main()
