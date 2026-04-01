class Patient:
    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number
        self.__co_payment_rate = 0.10  # Encapsulated (Private attribute)

    def calculate_claim(self, bill_amount):
        """
        Calculates the amount NHIF pays after a 10% co-payment.
        """
        co_payment = bill_amount * self.__co_payment_rate
        payable_amount = bill_amount - co_payment
        return payable_amount