import json

from dao import read_data as rd


def TransactioniO(accountNumber):
    data = rd.generate_data()
    for account in data['users']:
        if account['account']['account_number'] == str(accountNumber):
            return account
    return "account number deosn't match our database please connect with us if you think it's a mistake"