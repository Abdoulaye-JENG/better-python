import unittest
import unittest.mock
from unittest import TestCase
from unittest.mock import patch

from after import AuthorizerSMS, Order, PaymentProcessor


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

    def test_code_decimal(self):
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
    def test_authorize_fail(self,mocked_input):
        authorizer = AuthorizerSMS()
        authorizer.generate_sms_code()
        authorizer.authorize()
        self.assertFalse(authorizer.is_authorized())

class PaymentProcessor_TestCase(TestCase):
    def test_payment_success(self):
        # ????
        self.assertTrue(1)
        
    def test_payment_fail(self):
        # ???
        self.assertFalse(True)


if __name__ == "__main__":
    unittest.main()
