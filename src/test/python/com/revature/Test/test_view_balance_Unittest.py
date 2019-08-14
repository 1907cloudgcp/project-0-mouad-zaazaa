import unittest

from com.revature.service.ViewBalanceServ import ViewBalanceServ
from com.revature.service.loginServ import loginServ


class Test(unittest.TestCase):


    def test_login(self):
        self.assertEqual(loginServ(), ('11324212', 'Open'), "this should return the account number and open the session")

    def test_view_balance(self):
        self.assertEqual(ViewBalanceServ('11324212'), ('zaazaa', '490.0'), "Should be (name,Balance)")

if __name__ == '__main__':
    unittest.main()