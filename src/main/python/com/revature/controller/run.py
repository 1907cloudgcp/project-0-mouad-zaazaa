from controller.Menu import menu_main, account_menu
#from controller.frontmenu import *


# If login is successful from front menu, run account menu
from controller.control_account_menu import control_acc_menu
from controller.control_menu import control_menu


def run_app():
    info= control_menu(menu_main())
    if info == 1 or info ==0 or info== None:
        return
    else:
        acc = account_menu(info[0], info[1])
        info = control_acc_menu(acc)
