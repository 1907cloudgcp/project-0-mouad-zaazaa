import json
from com.revature.io import read_data as rd
from com.revature.controller import login as co
import itertools
def login():
    data = rd.read_file()
    info = co.login()
    login = info[0]
    pw = info[1]
    count = 0
    acc=0
    status = 'Close'
    item=None
    for account in data['users']:
        if account['info']['name'] == login:
            if account['account']['enabled'] !='False':

                if account['info']['password'] == pw:
                    print("Welcome " + login)
                    account['account']['status'] ='Open'
                    acc=account['account']['account_number']
                    status = 'Open'
                    #return acc
                    return appendToFile(data, account)
                else:
                    while count < 3:
                        count += 1
                        print("Please reEnter Your password")
                        pw = menu.enter_password()
                        if account['info']['password'] == pw:
                            acc = account['account']['account_number']
                            print("Welcome" + login)
                            account['account']['status']='Open'
                            status='Open'
                            return appendToFile(data,account)
                    if count>= 3:
                        account['account']['enabled'] = 'False'
                        acc=account['account']['account_number']
                        print("your account has been compromized")
                        item=account

            else:
                print("your account is closed for the moment please connect with us")
                return 1
    if item == None:
        print("Incorrect username please connect with us if you think it is a mistake")
        return 0
    return appendToFile(data,item)
def appendToFile(data,account):
    try:
        with open("C:\\Users\\mouad\\Documents\\GitHub\\project-0-mouad-zaazaa\\src\\main\\resources\\data.json",
                  'w') as account_write:
            json.dump(data, account_write, indent=4)
            return account['account']['account_number'],account['account']['status']
    except FileNotFoundError:
        print("File bankaccounts.json is not found")
        return (0, "Server error, please contact support")