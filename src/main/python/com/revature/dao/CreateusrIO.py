import json
from dao import read_data as rd



def CreateusrIO(info):
    data = rd.generate_data()
    data1 = {
        "info": {
            "name": info[0],
            "email": info[1],
            "Birth_Date": info[2],
            "password": info[3]
        }, "account": {
            "account_name": info[0],
            "account_number": str(info[4]),
            "type": "costumer",
            "balance": "0.0",
            "status": "Close",
            "enabled": "True"
        },
        "transactions": []
    }
    data['users'].append(data1)
    try:
        with open("C:\\Users\\mouad\\Desktop\\project-0-mouad-zaazaa\\src\\main\\resources\\data.json",
                  'w') as account_write:
            json.dump(data, account_write, indent=4)
            print("account has been created")
            return 1
    except FileNotFoundError:
        print("File data.json is not found")
        return 0
