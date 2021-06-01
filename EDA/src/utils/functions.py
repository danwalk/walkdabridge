import json
import os

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

def getcsvdatafullpath(name_of_file):
    SEP = os.sep
    dir = os.path.dirname
    csv_fullpath = dir(dir(dir(os.getcwd()))) + SEP + "data" + SEP + name_of_file
    return csv_fullpath