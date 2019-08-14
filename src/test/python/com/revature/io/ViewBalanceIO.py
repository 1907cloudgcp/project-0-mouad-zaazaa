from com.revature.io import read_data as rd
import json

def ViewBalanceIO(accountNumber):
    login_file = rd.read_file()
    for account in login_file['users']:
        if account['account']['account_number'] == accountNumber:
            return account

    return "accoun't number doesnt match"