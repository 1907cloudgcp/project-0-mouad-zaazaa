# define Python user-defined exceptions
import logging


class FileNotFound(FileNotFoundError,):
    def __init__(self, m,arg):
        logging.basicConfig(level=logging.DEBUG, filename="../error/file.log")
        self.message = m+" in this location :"+arg
        logger = logging.getLogger()
        logging.critical(str(m))
    def __str__(self):
        return self.message
class TypingError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message

# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
