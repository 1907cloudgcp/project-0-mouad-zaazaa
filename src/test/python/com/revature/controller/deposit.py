from com.revature.io import depositIO as dio
from com.revature.service import depositServ
'''this method handles deposit into the account'''
def deposit(accountNumber):
    amount= input("Please Enter the amount :")
    data = dio.depositIO(accountNumber,amount)
    if data != 0:
        account = data[0]
        current_Balence=data[1]
        depositServ.depositServ(account,current_Balence,amount)
