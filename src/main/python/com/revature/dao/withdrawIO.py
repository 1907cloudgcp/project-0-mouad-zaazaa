from dao import read_data as rd
def withdraw(accountNumber, amount):
    data = rd.generate_data()
    amount = float(amount)
    for account in data['users']:
        if account['account']['account_number'] == accountNumber:
            if account['account']['enabled'] == "True":
                current_balance = float(account['account']['balance'])
                info = [account, current_balance]
                return info
    return 0
