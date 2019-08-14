from com.revature.io import loginIO
def loginServ():
    info=loginIO.login()
    while info == 0:
        info=loginIO.login()
    return info
