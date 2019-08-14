from com.revature.io import read_data as rd
from com.revature.io.loginIO import appendToFile
from com.revature.io.logoutIO import logoutIO


def logoutServ(account):
    data = rd.read_file()
    for log in data['users']:
        if account['account']['account_number'] == log['account']['account_number']:
            if log['account']['status'] == 'Open' and log['account']['enabled'] == 'True':
                log['account']['status']='Close'
    appendToFile(data, account)