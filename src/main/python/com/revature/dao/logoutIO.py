from dao import read_data as rd


def logoutIO(accountNumber):
    data = rd.generate_data()
    for account in data['users']:
        if account['account']['account_number'] == accountNumber:
            if account['account']['enabled'] == "True":
                return account
            else:
                print("Account closed Please connect with us")
