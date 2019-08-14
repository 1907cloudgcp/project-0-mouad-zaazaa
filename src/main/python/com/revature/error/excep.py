# define Python user-defined exceptions
import logging


class FileNotFound(Exception):
    def __init__(self, m):
        logging.basicConfig(level=logging.DEBUG, filename="main/resources/file1.log")
        self.message = m
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
