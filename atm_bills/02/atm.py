
class Atm(object):
    def __init__(self, bills):
        self.bills = bills

    def withdraw(self, value):
        bills_to_give = []
        
        for bill, quantity in self.bills.items():
            while value > 0:
                value = value - bill 
                self.bills[bill] = quantity = quantity - 1
                bills_to_give.append(bill)

        return " | ".join([str(bill) for bill in bills_to_give])

