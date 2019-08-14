from com.revature.io import CreateusrIO as cuio
from com.revature.service import CreateusrServ as cuser

def Signup():
    info = ['', '', '', '','']
    info[0] = str(input("Enter Your Username :"))

    info[1] = str(input("Enter Your Email :"))
    info[2] = str(input("Enter Your Birthday (yyyy-dd-mm) :"))
    info[3] = str(input("Enter Your Password :"))
    info[4] = cuser.random_with_N_digits(7)
    while cuser.CreateUsrServ(info) == None:
        info = ['', '', '', '','']
        info[0] = str(input("Enter Your Username :"))

        info[1] = str(input("Enter Your Email :"))
        info[2] = str(input("Enter Your Birthday (yyyy-dd-mm) :"))
        info[3] = str(input("Enter Your Password :"))
        info[4]= cuser.random_with_N_digits(7)
    cuio.CreateusrIO(info)
