import json

from dao.read_data import generate_data
from dao.loginIO import appendToFile


def withdrawServ(account, current_balance, amount):
    data = generate_data()
    if float(current_balance) - float(amount) < 0:
        return print("Insufficient funds")
    else:
        current_balance = float(current_balance) - float(amount)
        data1 = {"id_transaction": str(int(len(account['transactions'])) + 1), "type": "withdraw",
                "description": str(amount)}
        account['account']['balance'] = str(current_balance)
        account['transactions'].append(data1)
        for log in data['users']:
            if account['account']['account_number'] == log['account']['account_number']:
                if account['account']['status'] == 'Open' and account['account']['enabled'] == 'True':
                    log['account']['balance'] = str(current_balance)
                    log['transactions'].append(data1)
    appendToFile(data, account)
    return print("Get your money")