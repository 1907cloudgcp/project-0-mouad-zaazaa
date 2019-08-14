import re
import json
from random import randint
from com.revature.io import read_data as rd


def CreateUsrServ(info):
    #usernames can consist of lowercase and capital
    #can consist of alphabetic character
    #username can consist of underscore and hyphens
    #cannot have a underscore or hypens in begining or end
    #should be 6 characters or greater
    if len(info[0]) > 6 and not_in("account_name", info[0]) and re.match(r"^[a-zA-Z0-9_.+-]+$", info[0]):
        name = info[0]
    else:
        print("a valid name must be unique and consist of 6 characters, not have any special characters")
        return None
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", info[1]):
        #print('valid')
        email = info[1]
    else:
        print("please enter a valid email")
        return None

    if re.match(r"[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])", info[2]):
        #print('valid')
        BirthDay = info[2]
    else:
        print("please enter a valid date")
        return None

    if info[3].isalpha() and len(info[3]) > 6:
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
    login_file = rd.read_file()
    for item in login_file['users']:
        if type == "account_name" or type == "account_number":
            if item['account'][type] == info:
                return False
    return True