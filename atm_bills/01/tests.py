import unittest
from atm_machine import Atm


class TestSuccessfulWithdraw(unittest.TestCase):
    def test_bills_setup(self):
        bills = {50: 1, 20: 1}
        atm = Atm(bills)
        self.assertEquals(bills, atm.bills)
    
    def test_returns_single_bill_for_exact_value_50(self):
        bills = {50: 1}
        atm = Atm(bills)
        self.assertEquals('50', atm.withdraw(50))
        self.assertEquals(atm.bills, {50: 0})
        
    def test_return_two_bills_different_values(self):
        bills = {50: 1, 20: 1}
        atm = Atm(bills)
        self.assertEquals('50 20', atm.withdraw(70))
        self.assertEquals(atm.bills, {50: 0, 20: 0})

    def test_return_two_bills_same_value(self):
        bills = {50: 2}
        atm = Atm(bills)
        self.assertEquals('50 50', atm.withdraw(100))
        self.assertEquals(atm.bills, {50: 0})

    def test_return_three_bills_different_values(self):
        bills = {50: 2, 20: 1}
        atm = Atm(bills)
        self.assertEquals('50 50 20', atm.withdraw(120))
        self.assertEquals(atm.bills, {50: 0, 20: 0})

    def test_validates_bills_quantity(self):
        bills = {20: 0, 10: 2}
        atm = Atm(bills)
        self.assertEquals('10 10', atm.withdraw(20))
        self.assertEquals(atm.bills, {20: 0, 10: 0})


class TestWithdrawErros(unittest.TestCase):
    def test_no_bills(self):
        bills = {20: 0}
        atm = Atm(bills)
        self.assertRaises(Exception, atm.withdraw, 20)
        self.assertEquals(atm.bills, {20: 0})

    def test_not_enough_bills(self):
        bills = {20: 1, 10: 0}
        atm = Atm(bills)
        self.assertRaises(Exception, atm.withdraw, 30)
        self.assertEquals(atm.bills, {20: 1, 10: 0})


if __name__ == '__main__':
    unittest.main()
