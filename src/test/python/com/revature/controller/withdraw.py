from com.revature.io import withdrawIO as wd
from com.revature.service import withdrawServ
'''take the amount and send it to service withdraw to handle it'''
def withdraw(accountNumber):
    amount= input("Please Enter the amount :")
    data = wd.withdraw(accountNumber,amount)
    if data != 0:
        account = data[0]
        current_Balence=data[1]
        withdrawServ.withdrawServ(account,current_Balence,amount)
