import sys
from error.excep import TypingError
from dao.withdrawIO import withdraw
from dao import depositIO as dio
from dao import TransactionIO as tio
from dao import CreateusrIO as cuio
from service import CreateusrServ as cuser

from service import TransactionServ as tser


from service import depositServ as dser

from service import withdrawServ as wser
from getpass import getpass

'''shows the Main Menu to the client'''
def menu_main():
    try:
        while True:
            print("MENU : \n 0: Login \n 1: Create new Account: \n 2: Exit :")
            req=int(input("Enter your Request "))
            if req == 0 or req ==1 or req ==2:
                return req
            else :
                print("please inter a 0 or 1")
    except:
        try:
            raise TypingError("Request was not recognized")
        except TypingError as x:
            print(x)
            return menu_main()

'''show the account menu if session is open'''
def account_menu(accountnum,status):
    req=-1
    try:
        if status=='Open':
            while True:
                print("Account Menu : \n 0: View Balance \n 1: Withdraw Money \n 2: Deposit Money \n 3: View transactions \n 4: Exit ")
                req=int(input("Enter a Requester :"))
                if req == 0 or req == 1 or req==2 or req == 3 or req ==4:
                    return [req,accountnum]
                else :
                    print("Enter a correct request !")
        elif status =='Close':
            print("Your Account has been closed")
    except:
        try:
            raise TypingError("Request was not recognized")
        except TypingError as x:
            print(x)
            return account_menu(accountnum, status)
'''password input'''
def enter_password():
    #login = str(input("Enter Your password :"))
    login = getpass("Enter Your password :")
    return login