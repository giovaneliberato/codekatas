import unittest
from atm import Atm


class TestAtm(unittest.TestCase):
    def test_initialization(self):
        atm = Atm({50: 1})
        self.assertEquals(atm.bills, {50: 1})

    def test_withdraw_single_bill(self):
        atm = Atm({50: 1})
        result = atm.withdraw(50)
        self.assertEquals(result, '50')
        self.assertEquals(atm.bills, {50: 0})

    def test_withdraw_two_bills_same_value(self):
        atm = Atm({50: 2})
        result = atm.withdraw(100)
        self.assertEquals(result, '50 | 50')
        self.assertEquals(atm.bills, {50: 0})

    def test_withdraw_two_bills_different_values(self):
        atm = Atm({50: 1, 20: 1})
        result = atm.withdraw(70)
        self.assertEquals(result, '50 | 20')
        self.assertEquals(atm.bills, {50: 0, 20: 0})

if __name__ == '__main__':
    unittest.main()
