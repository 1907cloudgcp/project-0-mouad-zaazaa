import re
from getpass import getpass

'''gets username and password from the user '''
def login():
    print("Welcome !! \n please Enter the login Informations :")

    login = str(input("Enter Your Username :"))
    password = getpass(prompt="Enter Your Password :")
    info = [login, password]
    return info