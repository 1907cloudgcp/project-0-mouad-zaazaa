from dao.read_data import generate_data
from dao.loginIO import appendToFile
from dao.logoutIO import logoutIO


def logoutServ(account):
    data = generate_data()
    for log in data['users']:
        if account['account']['account_number'] == log['account']['account_number']:
            if log['account']['status'] == 'Open' and log['account']['enabled'] == 'True':
                log['account']['status']='Close'
    appendToFile(data, account)