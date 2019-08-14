from controller.Signup import Signup
from service.loginServ import loginServ

#from main.python.com.revature.controller.control_account_menu import control_account_menu

'''here we take the import and call the appropriate method'''

def control_menu(code):
    try:
        if code == 0:
            return loginServ()
        elif code == 1:
            Signup()
        elif code == 2:
            return exit()
        else:
            print("Service has been interrupted please retry")
    except ValueError:
        print("please enter a number instead of strings")