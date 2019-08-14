from controller.Menu import account_menu
from error.excep import TypingError
from dao.logoutIO import logoutIO
from service import ViewBalanceServ as vserv
from service import TransactionServ as tser
from controller import deposit as dep
from controller import withdraw as w
from service.logoutServ import logoutServ

''' '''
def control_acc_menu(info):
    try:
        if info[0] == 0:
            data=vserv.ViewBalanceServ(info[1])
            print(" Hello "+data[0]+" your balance is :"+data[1]+"$")
        elif info[0] == 1:
            w.withdraw(info[1])

        elif info[0] == 2:
            dep.deposit(info[1])
        elif info[0] == 3:
            tser.TransactionServ(info[1])
        elif info[0] == 4:
            print("Thanks for your visit")
            logoutServ(logoutIO(info[1]))
            return
        elif info[1] == -1:
            print("For security matter your account has been closed")
            return

        else:
            print("Service has been interrupted please retry")
        exit = input("Enter 0 if you want to exit or 1 to go to the menu")
        if int(exit) == 0:
            print("Thanks for your visit")
            logoutServ(logoutIO(info[1]))
            return
        else:
            control_acc_menu(account_menu(info[1], 'Open'))
    except:
        print("Service has been interrupted please retry later")
        try:
            raise TypingError("please enter a valid number")
        except TypingError as x:
            control_acc_menu(account_menu(info[1], 'Open'))
