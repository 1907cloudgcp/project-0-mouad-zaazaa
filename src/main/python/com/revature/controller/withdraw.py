from dao import withdrawIO as wd
from service import withdrawServ


def withdraw(accountNumber):
    amount = input("Please Enter the amount :")
    data = wd.withdraw(accountNumber, amount)
    if data != -1:
        account = data[0]
        current_Balence = data[1]
        withdrawServ.withdrawServ(account, current_Balence, amount)
