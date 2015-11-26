
class Atm(object):
    def __init__(self, bills):
        self.bills = bills

    def withdraw(self, value):
        bills_to_give = []
        operators = []

        for bill, quantity in self.bills.items():
            amount = value / bill
            if amount > 0 and self._has_enough_bills(bill, amount):
                value = self._do_operation(bill, amount, value)
                bills_to_give.extend([bill] * amount)
                operators.append((bill, amount))

        if value != 0:
            self._undo_operations(operators)
            raise ValueError('Not enough bills.')

        return " | ".join([str(bill) for bill in bills_to_give])

    def _undo_operations(self, operators):
        for bill, amount in operators:
            self.bills[bill] = self.bills[bill] + amount

    def _do_operation(self, bill, amount, value):
        self.bills[bill] = self.bills[bill] - amount
        return value - (bill * amount)

    def _has_enough_bills(self, bill, value):
        return self.bills[bill] >= value
