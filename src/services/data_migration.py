# ==========================================================================
# Author: Hoang Anh Quan
# Purpose: From txt file insert into Supabase: Data Migration
# ==========================================================================
# IMPORTS & MODULE LOADING
# ==========================================================================
import os
from typing import List, Dict
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

# keys:
attendance_keys = []
classes_keys = ["class_id", "class_name"]
schedules_keys = ["class_id", "weekday", "period", "room"]
student_keys = ["class_id", "student_id", "student_name"]


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


def ls_mapping(clean_data: List[List[str]], keys: List[str]):
    if len(keys) != len(clean_data[0]):
        print("the lenght of keys isn't equal to the lenght of clean_data!")
        return
    data = []
    for element in clean_data:
        zipped_data = dict(zip(keys, element))
        data.append(zipped_data)

    data = json.dumps(data, ensure_ascii=False, indent=4)
    return data


def insert_to_supabase():
    pass


# ==========================================================================
# MAIN EXECUTION ENTRYPOINT
# ==========================================================================
def main():
    data = txt_to_ls(classes_file_path)
    json_data = ls_mapping(data, classes_keys)
    print(json_data)


if __name__ == "__main__":
    main()
