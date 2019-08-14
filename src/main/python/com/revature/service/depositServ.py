import json
from dao.loginIO import appendToFile
from dao.read_data import generate_data
from error import excep as e

def depositServ(account,current_balance,amount):
    login_file = generate_data()
    if float(amount) > 1000.00:
        return print("can't deposit more than 1000$")
    else:
        current_balance = float(current_balance) + float(amount)
        data = {"id_transaction": str(int(len(account['transactions'])) + 1), "type": "deposit",
                "description": str(amount)}
    for log in login_file['users']:
        if account['account']['account_number'] == log['account']['account_number']:
            #print("account found")
            if account['account']['status'] == 'Open' and account['account']['enabled'] == 'True':
                log['account']['balance'] = str(current_balance)
                log['transactions'].append(data)
    appendToFile(login_file, account)
    return print("Money has been deposited")