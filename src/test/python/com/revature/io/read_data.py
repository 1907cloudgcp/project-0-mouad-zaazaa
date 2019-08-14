
import json

from com.revature.error.exceptions import FileNotFound


def read_file():

    try:
        current_file_dir = 'C:\\Users\\mouad\\Documents\\GitHub\\project-0-mouad-zaazaa\\src\\main\\resources\\data.json'
        with open(current_file_dir,'r') as json_file:
            file = json.load(json_file)
            return file
    except FileNotFoundError:
        try:
            raise FileNotFound('file not found',current_file_dir)
        except FileNotFound as x:
            print(x)
        return 0
read_file()