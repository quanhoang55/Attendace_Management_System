"""Tests for FileManager: readFile, writeFile in isolation."""

import os
import shutil

from app.services.file_manager import FileManager

# Use a dedicated temp directory so tests don't pollute production data
_TEST_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data_file_manager_test"
)


def _setup():
    """Creates a clean test directory before each test."""
    if os.path.exists(_TEST_DIR):
        shutil.rmtree(_TEST_DIR)
    os.makedirs(_TEST_DIR, exist_ok=True)


def _teardown():
    """Removes test directory after each test."""
    if os.path.exists(_TEST_DIR):
        shutil.rmtree(_TEST_DIR)


def test_read_nonexistent_file_returns_empty_list():
    print("Testing FileManager.readFile - nonexistent file returns empty list...")
    _setup()
    try:
        fm = FileManager()
        result = fm.readFile(os.path.join(_TEST_DIR, "missing.txt"))
        assert result.size() == 0
        print("readFile nonexistent returns empty - passed!")
    finally:
        _teardown()


def test_write_and_read_roundtrip():
    print("Testing FileManager.writeFile + readFile - round-trip...")
    _setup()
    try:
        fm = FileManager()
        path = os.path.join(_TEST_DIR, "test.txt")
        fm.writeFile(path, "line1\nline2\nline3\n")
        result = fm.readFile(path)
        assert result.size() == 3
        assert result.get(0) == "line1"
        assert result.get(1) == "line2"
        assert result.get(2) == "line3"
        print("writeFile + readFile roundtrip - passed!")
    finally:
        _teardown()


def test_write_creates_missing_directory():
    print("Testing FileManager.writeFile - creates missing directories...")
    _setup()
    try:
        fm = FileManager()
        nested_path = os.path.join(_TEST_DIR, "subdir", "nested.txt")
        fm.writeFile(nested_path, "hello\n")
        assert os.path.exists(nested_path)
        print("writeFile creates missing directory - passed!")
    finally:
        _teardown()


def test_write_overwrites_existing_content():
    print("Testing FileManager.writeFile - overwrites existing content...")
    _setup()
    try:
        fm = FileManager()
        path = os.path.join(_TEST_DIR, "overwrite.txt")
        fm.writeFile(path, "old content\n")
        fm.writeFile(path, "new content\n")
        result = fm.readFile(path)
        assert result.size() == 1
        assert result.get(0) == "new content"
        print("writeFile overwrites existing content - passed!")
    finally:
        _teardown()


def test_read_skips_empty_lines():
    print("Testing FileManager.readFile - skips empty lines...")
    _setup()
    try:
        fm = FileManager()
        path = os.path.join(_TEST_DIR, "empty_lines.txt")
        fm.writeFile(path, "line1\n\nline2\n\n\nline3\n")
        result = fm.readFile(path)
        assert result.size() == 3
        assert result.get(0) == "line1"
        assert result.get(1) == "line2"
        assert result.get(2) == "line3"
        print("readFile skips empty lines - passed!")
    finally:
        _teardown()


def test_write_empty_content_creates_file():
    print("Testing FileManager.writeFile - empty content creates empty file...")
    _setup()
    try:
        fm = FileManager()
        path = os.path.join(_TEST_DIR, "empty.txt")
        fm.writeFile(path, "")
        assert os.path.exists(path)
        result = fm.readFile(path)
        assert result.size() == 0
        print("writeFile empty content creates file - passed!")
    finally:
        _teardown()


if __name__ == "__main__":
    test_read_nonexistent_file_returns_empty_list()
    test_write_and_read_roundtrip()
    test_write_creates_missing_directory()
    test_write_overwrites_existing_content()
    test_read_skips_empty_lines()
    test_write_empty_content_creates_file()
    print("All FileManager tests passed!")
