import json
import os

PATH = os.path.join("operations.json")

def read_json():
    """
    Преоброзование json --> pythin
    """
    with open(PATH, "r", encoding="uft8") as date:
        return json.load(date)




