#!/usr/bin/env python3
import sys

from controller.Menu import account_menu
from controller.control_account_menu import control_acc_menu

sys.path.append('C:\\Users\\mouad\\Documents\\GitHub\\project-0-mouad-zaazaa\\src\\main\\python\\com\\revature\\controller')
from controller.run import run_app
'''
This is your main script, this should call several other scripts within your packages.
'''
def main():
	while True:
		return run_app()


if __name__ == '__main__':
	main()

	#if info==1 or info ==1

	#acc=account_menu(info[0],info[1])
	#info=control_acc_menu(acc)
