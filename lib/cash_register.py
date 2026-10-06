#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def set_discount(self, value):
        if type(value) == int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for i in range(0, quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if self.previous_transactions == [] or self.total == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)
        print(f"After the discount, the total comes to ${self.total:.0f}.")
        
        self.previous_transactions.pop()

    def void_last_transaction(self):
        if self.previous_transactions == []:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions[-1]
        self.total = self.total - transaction["price"] * transaction["quantity"]
        
        self.previous_transactions.pop()
