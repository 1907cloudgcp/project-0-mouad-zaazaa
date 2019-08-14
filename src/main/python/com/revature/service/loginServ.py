from dao import loginIO
def loginServ():
    info=loginIO.login()
    while info == 0:
        info=loginIO.login()
    return info
