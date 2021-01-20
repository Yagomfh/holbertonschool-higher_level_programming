#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file"""
import sys
import os.path
from os import path


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

elems = sys.argv
f = "add_item.json"
elems.pop(0)

if path.exists(f) is False:
    save_to_json_file(elems, f)
else:
    f_data = load_from_json_file(f)
    f_data.extend(elems)
    save_to_json_file(f_data, f)
