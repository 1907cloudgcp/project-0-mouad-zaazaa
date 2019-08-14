#from src.main.python.com.revature.dao.read_data import read_file

from dao import read_data as rd

def depositIO(accountNumber, amount):
        data = rd.generate_data()
        amount = float(amount)
        for account in data['users']:
            if account['account']['account_number'] == accountNumber:

                if account['account']['enabled'] == "True":
                    current_balance = float(account['account']['balance'])
                    info=[account,current_balance]
                    return info
                else:
                    print("Account closed Please connect with us")