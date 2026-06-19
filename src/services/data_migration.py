# ==========================================================================
# Author: Hoang Anh Quan
# Purpose: From txt file insert into Supabase: Data Migration
# ==========================================================================
# IMPORTS & MODULE LOADING
# ==========================================================================
from dotenv import load_dotenv
import os
from typing import List, Dict, Optional, Any
import json
from supabase import create_client, Client

# ==========================================================================
# PARAMETERS
# ==========================================================================

# Supabase Connection
# load the .env
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

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
schedules_keys = ["schedule_id", "class_id", "weekday", "period", "room"]
student_keys = ["student_id", "class_id", "student_name"]
# Input
file_path = student_file_path
key = student_keys
table_name = "student"
pk_fields = ["student_id"]


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
            raw_data = file.read().splitlines()
            clean_data = [element.split("|") for element in raw_data]
    except Exception:
        print(f"{Exception}: the file_path can't be read")
        return
    return clean_data


def ls_mapping(
    clean_data: List[List[Any]], keys: List[str]
) -> Optional[List[Dict[str, Any]]]:
    """turn a List of List into List of Dictionary

    Args:
        clean_data (List[List[Any]]): List of List
        keys (List[str]): List of Keys

    Returns:
        Optional[List[Dict[str, Any]]]: A List of Dictionary
    """
    if len(keys) != len(clean_data[0]):
        print("the lenght of keys isn't equal to the lenght of clean_data!")
        return
    data = []
    for element in clean_data:
        zipped_data = dict(zip(keys, element))
        data.append(zipped_data)
    return data


def remove_duplicates_before_upsert(
    data: List[Dict[str, Any]], pk_fields: List[str]
) -> List[Dict[str, Any]]:
    """Remove Duplicates

    Args:
        data (List[Dict[str, Any]])
        pk_fields (List[str])

    Returns:
        List[Dict[str, Any]]
    """
    seen = set()
    unique_data = []
    for row in data:
        identifier = tuple(row[key] for key in pk_fields if key in row)
        if identifier not in seen:
            seen.add(identifier)
            unique_data.append(row)
    return unique_data


def upsert_json_to_supabase(data: List[Dict[str, Any]], table_name: str):
    """Upsert json into supabase

    Args:
        data (List[Dict[str, Any]]):
        table_name (str):
    """
    try:
        response = supabase.table(table_name).insert(data).execute()
        print("Upsert Successfully!")
    except Exception as e:
        print(f"{e}: Can't upsert data to Supabase!")
    return


def data_migration(
    file_path: str, keys: List[str], table_name: str, pk_fields: List[str]
):
    data = txt_to_ls(file_path)
    mapping_data = ls_mapping(data, keys)
    cleaned_data = remove_duplicates_before_upsert(mapping_data, pk_fields)
    upsert_json_to_supabase(cleaned_data, table_name)


# ==========================================================================
# MAIN EXECUTION ENTRYPOINT
# ==========================================================================
data_migration(
    file_path,
    key,
    table_name,
    pk_fields,
)
