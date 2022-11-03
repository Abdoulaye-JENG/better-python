"""This module aims to play with dependency injection and dependency inversion.
It's a simple order application allwing clients to make an order and authorize payment
for the order tio be successful.
The point here is that, the `pay`  method of the PaymentProcessor class
is responsible for creating an instance of `AuthorizerSMS` which ios not really a good practice.
-- So it's what is fixed in 'after_injection.py (PaymemntProcessor class)' using dependency injection.
"""

import random
import string
from abc import ABC, abstractmethod


class Order:
    def __init__(self):
        self.id = "".join(random.choices(string.ascii_lowercase, k=12))
        self.status = "open"
        
    def set_status(self, status):
        self.status = status



class AuthorizerSMS:
    def __init__(self) -> None:
        self.authorized: bool = False
        self.code: str | None = None
    
    def generate_sms_code(self) -> None:
        self.code = "".join(random.choices(string.digits, k=7))

    def authorize(self) -> None:
        sms_code = input("Enter SMS authorization code.")
        self.authorized = self.code == sms_code

    def is_authorized(self):
        return self.authorized

class PaymentProcessor:
    def pay(self, order) -> None:
        """ Handle Order Payment"""
        # Check whether the payor has the Authorization
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        authorizer.authorize()
        if not authorizer.is_authorized():
            raise Exception("You are not authorized")
        print(f"Processing payment of the order {order.id}")
        order.set_status("paid")

