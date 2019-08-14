import json

from dao.ViewBalanceIO import ViewBalanceIO


def ViewBalanceServ(accountnumber):
    account = ViewBalanceIO(accountnumber)
    if account['account']['enabled'] == "True":
        name = account['info']['name']
        balance = account['account']['balance']
        return name, balance
