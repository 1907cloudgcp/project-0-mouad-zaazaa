import json

#from src.main.python.com.revature.dao.read_data import read_file
from dao import read_data as rd
def ViewBalanceIO(accountNumber):
    data = rd.generate_data()
    for account in data['users']:
        if account['account']['account_number'] == accountNumber:
            return account

    return "accoun't number doesnt match"