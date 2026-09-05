#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount =0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <=100):
            print("Not a valid discount")
            return
        else:
             self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += (price * quantity)
        self.items.extend([item] * quantity)
        new_transactions = {
            "item":item, 
            "price": price, 
            "quantity": quantity
          }
        self.previous_transactions.append(new_transactions)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - (self.discount * self.total) / 100
            print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last_item = self.previous_transactions.pop()

        subtotal_to_remove = last_item["price"] * last_item["quantity"]
        self.total -= subtotal_to_remove

        for _ in range(last_item["quantity"]):
            self.items.remove(last_item["item"])

    def __repr__(self):
        return f"Discount: {self.discount}%, Total: {self.total}, Items: {self.items}, Transactions: {self.previous_transactions}"
    
