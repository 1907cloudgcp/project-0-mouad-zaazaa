import json
from com.revature.io.TransactionIO import TransactioniO

def TransactionServ(numaccount):
    account=TransactioniO(numaccount)
    #print(account)
    if account['account']['enabled'] == "True":
        current_balance = float(account['account']['balance'])
        print(account['account']['account_name'] + "'s transactions")
        for transaction in account['transactions']:
            print(transaction['type'] + " " + transaction['description'] + "$")
        print("_______ END TRANSACTIONS_______")
