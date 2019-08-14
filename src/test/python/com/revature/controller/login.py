import re
from getpass import getpass

'''this method takes data from the user '''
def login():
    print("Welcome !! \n please Enter the login Informations :")

    login = str(input("Enter Your Username :"))
    password = str(input("Enter Your Password :"))
    info = [login, password]
    return info