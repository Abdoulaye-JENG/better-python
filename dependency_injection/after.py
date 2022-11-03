
PRICES = {
    "kebab":3_600_00,
    "tacos":4_000_00,
    "sandwich": 1_200_00,
    "burger":2_200_00,
    "juice":1_200_00
}


class PaytechPaymentHandler:
    def handle_payment(self,amount:int):
        print(f"Charging {amount/100:.2f} XOF using PayTech")



def order_food(elts: list[str], payment_handler) -> None:
    """Now Here, instead of creating a `PaytechPaymentHandler`,
    The payment object will be a parameter.
    In this way, no mattter how we pay (the payment method),
    The client will be charged.
    """
    total = sum([PRICES[elt] for elt in elts])
    print(f"You order amount is {total} XOF.")
    payment_handler.handle_payment(total)
    print("Thank you for trusting us.")


def main() -> None:
    paytech_payment_handler = PaytechPaymentHandler()
    order_food(elts=["tacos", "sandwich", "juice"],payment_handler=paytech_payment_handler )


if __name__=="__main__":
    main()
