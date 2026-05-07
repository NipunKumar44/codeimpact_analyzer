def validate_user(user_id):

    print("Validating user")

    return True


def validate_card(card_number):

    print("Validating card")

    return True


def calculate_total(cart_items):

    print("Calculating cart total")

    return 500


def process_payment(user_id, card_number, amount):

    validate_user(user_id)

    validate_card(card_number)

    print("Processing payment")

    return True


def generate_invoice(user_id, amount):

    print("Generating invoice")

    return "INV-001"


def send_email(user_id):

    print("Sending confirmation email")


def checkout(user_id, card_number, cart_items):

    amount = calculate_total(cart_items)

    payment_success = process_payment(
        user_id,
        card_number,
        amount
    )

    if payment_success:

        generate_invoice(user_id, amount)

        send_email(user_id)

        print("Checkout completed")


def refund_payment(payment_id):

    validate_user(payment_id)

    print("Refund initiated")