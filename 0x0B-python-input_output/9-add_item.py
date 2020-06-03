#!/usr/bin/python3
"""doc"""
from sys import argv as av
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


fn = 'add_item.json'
lst = []
if os.path.exists(fn):
    lst = load_from_json_file(fn)
save_to_json_file(lst + av[1:], fn)
