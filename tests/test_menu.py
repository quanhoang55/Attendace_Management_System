"""Tests for MainProgram helper methods: _get_non_empty_input, _get_int_input."""

import os
from unittest.mock import patch

import app.services.attendance_manager as am_module

# Trỏ tới thư mục test để tránh đụng dữ liệu thật khi khởi tạo MainProgram
_TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data_menu_test"
)


def _make_program():
    """Helper: tạo MainProgram với data dir cô lập."""
    am_module._BASE_DIR = _TEST_DATA_DIR
    from app.ui.menu import MainProgram
    return MainProgram()


# ==========================================================================
# _get_non_empty_input
# ==========================================================================

def test_get_non_empty_input_returns_on_first_valid():
    print("Testing _get_non_empty_input - returns immediately on non-empty input...")
    prog = _make_program()
    with patch("builtins.input", return_value="CS101"):
        result = prog._get_non_empty_input("Enter: ")
    assert result == "CS101"
    print("_get_non_empty_input returns on first valid - passed!")


def test_get_non_empty_input_strips_whitespace():
    print("Testing _get_non_empty_input - strips surrounding whitespace...")
    prog = _make_program()
    with patch("builtins.input", return_value="  CS101  "):
        result = prog._get_non_empty_input("Enter: ")
    assert result == "CS101"
    print("_get_non_empty_input strips whitespace - passed!")


def test_get_non_empty_input_retries_on_empty():
    print("Testing _get_non_empty_input - retries when input is empty...")
    prog = _make_program()
    # First call returns empty, second returns valid value
    with patch("builtins.input", side_effect=["", "CS101"]):
        result = prog._get_non_empty_input("Enter: ")
    assert result == "CS101"
    print("_get_non_empty_input retries on empty - passed!")


def test_get_non_empty_input_retries_on_whitespace_only():
    print("Testing _get_non_empty_input - retries when input is whitespace only...")
    prog = _make_program()
    with patch("builtins.input", side_effect=["   ", "\t", "CS101"]):
        result = prog._get_non_empty_input("Enter: ")
    assert result == "CS101"
    print("_get_non_empty_input retries on whitespace only - passed!")


# ==========================================================================
# _get_int_input
# ==========================================================================

def test_get_int_input_returns_valid_int():
    print("Testing _get_int_input - returns valid integer...")
    prog = _make_program()
    with patch("builtins.input", return_value="5"):
        result = prog._get_int_input("Enter: ")
    assert result == 5
    print("_get_int_input returns valid int - passed!")


def test_get_int_input_retries_on_non_integer():
    print("Testing _get_int_input - retries on non-integer input...")
    prog = _make_program()
    with patch("builtins.input", side_effect=["abc", "xyz", "3"]):
        result = prog._get_int_input("Enter: ")
    assert result == 3
    print("_get_int_input retries on non-integer - passed!")


def test_get_int_input_retries_on_empty():
    print("Testing _get_int_input - retries on empty input...")
    prog = _make_program()
    with patch("builtins.input", side_effect=["", "7"]):
        result = prog._get_int_input("Enter: ")
    assert result == 7
    print("_get_int_input retries on empty - passed!")


def test_get_int_input_respects_min_bound():
    print("Testing _get_int_input - rejects value below min...")
    prog = _make_program()
    with patch("builtins.input", side_effect=["0", "1"]):
        result = prog._get_int_input("Enter: ", min_val=1, max_val=10)
    assert result == 1
    print("_get_int_input respects min bound - passed!")


def test_get_int_input_respects_max_bound():
    print("Testing _get_int_input - rejects value above max...")
    prog = _make_program()
    with patch("builtins.input", side_effect=["11", "10"]):
        result = prog._get_int_input("Enter: ", min_val=1, max_val=10)
    assert result == 10
    print("_get_int_input respects max bound - passed!")


def test_get_int_input_accepts_boundary_values():
    print("Testing _get_int_input - accepts min and max boundary values...")
    prog = _make_program()
    with patch("builtins.input", return_value="1"):
        result = prog._get_int_input("Enter: ", min_val=1, max_val=10)
    assert result == 1

    with patch("builtins.input", return_value="10"):
        result = prog._get_int_input("Enter: ", min_val=1, max_val=10)
    assert result == 10
    print("_get_int_input accepts boundary values - passed!")


def test_get_int_input_no_bounds():
    print("Testing _get_int_input - no bounds, accepts any integer...")
    prog = _make_program()
    with patch("builtins.input", return_value="-999"):
        result = prog._get_int_input("Enter: ")
    assert result == -999
    print("_get_int_input no bounds accepts any int - passed!")


if __name__ == "__main__":
    test_get_non_empty_input_returns_on_first_valid()
    test_get_non_empty_input_strips_whitespace()
    test_get_non_empty_input_retries_on_empty()
    test_get_non_empty_input_retries_on_whitespace_only()
    test_get_int_input_returns_valid_int()
    test_get_int_input_retries_on_non_integer()
    test_get_int_input_retries_on_empty()
    test_get_int_input_respects_min_bound()
    test_get_int_input_respects_max_bound()
    test_get_int_input_accepts_boundary_values()
    test_get_int_input_no_bounds()
    print("All MainProgram helper tests passed!")
