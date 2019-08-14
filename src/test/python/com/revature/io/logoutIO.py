from com.revature.io import read_data as rd
from com.revature.io.loginIO import appendToFile


def logoutIO(accountNumber):
    data = rd.read_file()
    for account in data['users']:
        if account['account']['account_number'] == accountNumber:
            if account['account']['enabled'] == "True":
                return account
            else:
                print("Account closed Please connect with us")
