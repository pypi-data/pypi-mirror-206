import sys
import json

curr_path = sys.path[0]
tempfile = curr_path + "/templates.json"

with open(tempfile, "r+") as fp:
    templates = json.load(fp)
    fp.close()