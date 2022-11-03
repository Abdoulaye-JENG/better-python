import unittest
from unittest import TestCase
from unittest.mock import patch

from after_inversion import AuthorizerRobot, AuthorizerSMS, Order, PaymentProcessor


class OrderTestCase(TestCase):
    def test_init(self):
        order =  Order()
        self.assertEqual(order.status,"open")

    def test_order_status(self):
        order = Order()
        order.set_status("paid")
        self.assertEqual(order.status, "paid")

class SMS_Authorizer_TestCase(TestCase):
    def test_init_authorized(self):
        authorizer  = AuthorizerSMS()
        self.assertFalse(authorizer.is_authorized())

    def test_code_numeric(self):
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        self.assertTrue(authorizer.code.isnumeric())

    def test_authorize_success(self):
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        with patch("builtins.input", return_value=authorizer.code):
            authorizer.authorize()
            self.assertTrue(authorizer.is_authorized())

    @patch("builtins.input", return_value="00000")
    def test_authorize_fail(self, mocked_input):
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        authorizer.authorize()
        self.assertFalse(authorizer.is_authorized())

class Robot_Authorizer_TestCase(TestCase):
    def test_init_authorized(self):
        authorizer = AuthorizerRobot()
        self.assertFalse(authorizer.is_authorized())
    
    @patch("builtins.input", return_value="n")
    def test_authorization_success(self, mocked_input):
        authorizer = AuthorizerRobot()
        authorizer.authorize()
        self.assertTrue(authorizer.is_authorized())
    
    @patch("builtins.input", return_value="y")
    def test_authorization_fail(self, mocked_input):
        authorizer = AuthorizerRobot()
        authorizer.authorize()
        self.assertFalse(authorizer.is_authorized())
     
class PaymentProcessor_TestCase(TestCase):
    def test_init(self):
        auth = AuthorizerSMS()
        p = PaymentProcessor(auth)
        self.assertEqual(p.authorizer, auth)
        
    def test_payment_success(self):
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        with patch("builtins.input", return_value=authorizer.code):
            payment = PaymentProcessor(authorizer)
            order = Order()
            payment.pay(order)
            self.assertEqual(order.status, "paid")
            
    def test_payment_fail(self):
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        with patch("builtins.input", return_value="000000"):
            payment = PaymentProcessor(authorizer)
            order = Order()
            self.assertRaises(Exception,payment.pay,order)
            

if __name__ == "__main__":
    unittest.main()
