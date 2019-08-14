
import json
from error import excep as e
from controller import Menu as menu


def generate_data():

    try:
        current_file_dir = 'C:\\Users\\mouad\\Desktop\\project-0-mouad-zaazaa\\src\\main\\resources\\data.json'
        with open(current_file_dir,'r') as json_file:
            file = json.load(json_file)
            return file
    except FileNotFoundError:
        try:
            raise e.FileNotFound('file not found')
        except e.FileNotFound as x:
            print(x)
    return menu.menu_main()