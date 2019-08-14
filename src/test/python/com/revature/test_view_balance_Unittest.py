import unittest

from com.revature.service.ViewBalanceServ import ViewBalanceServ


class Test_View_Balance(unittest.TestCase):

    def test_view_balance(self):
        self.assertEqual(ViewBalanceServ('11324212'), ('zaazaa', '1612.0'), "Should be 6")


if __name__ == '__main__':
    unittest.main()