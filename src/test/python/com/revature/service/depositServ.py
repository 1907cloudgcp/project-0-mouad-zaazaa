import json
from com.revature.io import read_data as rd

def depositServ(account,current_balance,amount):
    login_file = rd.read_file()
    if float(amount) > 1000.00:
        return print("can't deposit more than 1000$")
    else:
        current_balance = float(current_balance) + float(amount)
        data = {"id_transaction": str(int(len(account['transactions'])) + 1), "type": "deposit",
                "description": str(amount)}
    for log in login_file['users']:
        if account['account']['account_number'] == log['account']['account_number']:
            print("account found")
            if account['account']['status'] == 'Open' and account['account']['enabled'] == 'True':
                log['account']['balance'] = str(current_balance)
                log['transactions'].append(data)
    try:
        with open("C:\\Users\\mouad\\Documents\\GitHub\\project-0-mouad-zaazaa\\src\\main\\resources\\data.json",
                  'w') as account_write:
            json.dump(login_file, account_write, indent=4)
            return print("money has been deposited")
    except FileNotFoundError:
        print("File bankaccounts.json is not found")
        return (0, "Server error, please contact support")