class CreditCardPayment:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class DebitCardPayment:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card")


class UpiPayment:

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        # Allows switching the payment method at runtime
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


p = PaymentProcessor(CreditCardPayment())
p.process_payment(1500)

p = PaymentProcessor(DebitCardPayment())
p.process_payment(750)

p = PaymentProcessor(UpiPayment())
p.process_payment(1000)

p = PaymentProcessor(CashPayment())
p.process_payment(2500)
