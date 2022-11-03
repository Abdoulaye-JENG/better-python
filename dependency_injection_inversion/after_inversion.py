import random
import string
from abc import ABC, abstractmethod


class Authorizer(ABC):
    @abstractmethod
    def authorize(self):
        ...
    @abstractmethod
    def is_authorized(self):
        ...



# -- SMSAUTHORIZER Class
class AuthorizerSMS(Authorizer):
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


class AuthorizerRobot(Authorizer):
    def __init__(self) -> None:
        self.authorized: bool = False

    def authorize(self) -> None:
        robot = ""
        while robot not in ["y","n"]:
            robot = input("Are you a robot (y/n) ?")
        self.authorized = robot == "n"

    def is_authorized(self):
        return self.authorized
# -- ORDER Class
class Order:
    def __init__(self):
        self.id = "".join(random.choices(string.ascii_lowercase, k=12))
        self.status = "open"
        
    def set_status(self, status):
        self.status = status


# -- PAYMENTPROCESSOR Class
class PaymentProcessor:
    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer
        
    def pay(self, order) -> None:
        """ Handle Order Payment"""
        # Check whether the payor has the Authorization
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception("You are not authorized")
        print(f"Processing payment of the order {order.id}")
        order.set_status("paid")
