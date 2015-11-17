from copy import deepcopy
from collections import OrderedDict


class Atm(object):
    def __init__(self, bills={}):
        self.bills = self.sort_bills(bills)

    def sort_bills(self, bills):
        return OrderedDict(sorted(bills.items(), key=lambda t: t[0], reverse=True))

    def consume_bill(self, value, bill, quantity, bills_to_give):
        while value / bill > 0 and quantity > 0:
            bills_to_give.append(bill)
            quantity -= 1
            value = value - bill

        return value, quantity

    def withdraw(self, value):
        available_bills = deepcopy(self.bills)
        bills_to_give = []
        
        for bill, quantity in available_bills.items():
            value, new_quantity = self.consume_bill(value, bill, quantity, bills_to_give)
            available_bills[bill] = new_quantity
        
        if value == 0:
            self.bills = available_bills
        else:
            raise Exception('Not enought bills available.')

        return " ".join([str(bill) for bill in bills_to_give])
