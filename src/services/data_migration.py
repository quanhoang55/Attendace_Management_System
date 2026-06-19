# ==========================================================================
# IMPORTS & MODULE LOADING
# ==========================================================================
import os
from typing import List
import json

# ==========================================================================
# PARAMETERS
# ==========================================================================

# ./
ROOTDIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# ./data/
DATAPATH = os.path.join(ROOTDIR, "data/")
# ./data/...
attendance_file_path = os.path.join(DATAPATH, "attendance.txt")
classes_file_path = os.path.join(DATAPATH, "classes.txt")
schedules_file_path = os.path.join(DATAPATH, "schedules.txt")
student_file_path = os.path.join(DATAPATH, "students.txt")


# ==========================================================================
# CORE LOGIC & BUSINESS FUNCTIONS
# ==========================================================================
def txt_to_ls(file_path: str) -> List[List[str]]:
    """Turn .txt file into a list of list

    Args:
        file_path (str): .txt file path

    Returns:
        List[List[str]]: a list of list string
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            raw_data = file.read().split("\n")[:-1]
            clean_data = [element.split("|") for element in raw_data]
    except Exception:
        print(f"{Exception}: the file_path can't be read")
        return
    return clean_data


def ls_mapping(clean_data: List[List[str]]):
    pass


def insert_to_supabase():
    pass


# ==========================================================================
# MAIN EXECUTION ENTRYPOINT
# ==========================================================================
def main():
    data = txt_to_ls(schedules_file_path)
    json_dump = json.dumps(data, ensure_ascii=False)


if __name__ == "__main__":
    main()
