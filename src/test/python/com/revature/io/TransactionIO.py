from com.revature.io import read_data as rd
import json


def TransactioniO(accountNumber):
    login_file = rd.read_file()
    for account in login_file['users']:
        if account['account']['account_number'] == str(accountNumber):
            return account
    return "account number deosn't match our database please connect with us if you think it's a mistake"
