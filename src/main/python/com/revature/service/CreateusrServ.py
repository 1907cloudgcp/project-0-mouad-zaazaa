import re
import json
from random import randint
from dao.read_data import generate_data



def CreateUsrServ(info):
    #name should have more than 6 characters
    #name has to be unique
    #name consit of leters and . + -
    if len(info[0]) > 6 and not_in("account_name", info[0]) and re.match(r"^[a-zA-Z0-9_.+-]+$", info[0]):
        name = info[0]
    else:
        print("a valid name must be unique and consist of 6 characters, not have any special characters")
        return None
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", info[1]):
        email = info[1]
    else:
        print("please enter a valid email")
        return None

    if re.match(r"[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])", info[2]):
        BirthDay = info[2]
    else:
        print("please enter a valid date")
        return None

    if len(info[3]) > 6:
        password = info[3]

    else:
        print("your password should contain 6 characters and it should be alphanumeric")
        return None

    if not_in("account_number", info[4]) == True:
        account_number = str(info[4])
    return info

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def not_in(type, info):
    data = generate_data()
    for item in data['users']:
        if type == "account_name" or type == "account_number":
            if item['account'][type] == info:
                return False
    return True