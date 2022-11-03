
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



def order_food(elts: list[str]) -> None:
    """The think to note here is,
    We create a `PaytechPaymentHandler` object.
    Something that should not be the responsibility of this function
    """
    total = sum([PRICES[elt] for elt in elts])
    print(f"You order amount is {total} XOF.")
    payment_handler = PaytechPaymentHandler()
    payment_handler.handle_payment(total)
    print("Thank you for trusting us.")


def main():
    order_food(["tacos", "sandwich", "juice"])


if __name__=="__main__":
    main()
