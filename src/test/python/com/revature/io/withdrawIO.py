from com.revature.io import read_data as rd
def withdraw(accountNumber, amount):
    login_file = rd.read_file()
    amount = float(amount)
    for account in login_file['users']:
        if account['account']['account_number'] == accountNumber:
            if account['account']['enabled'] == "True":
                current_balance = float(account['account']['balance'])
                info = [account, current_balance]
                return info
    return 0
