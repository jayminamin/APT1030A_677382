def calculate_claim(amount):
    """
    Deducts 10% co-payment from the total bill.
    """
    co_payment = amount * 0.10
    return amount - co_payment

patient_data = {
    "name": "Jaymin",
    "policy_number": "NHIF-778899"
}

bill = 5000
payout = calculate_claim(bill)

print(f"Processing for: {patient_data['name']}")
print(f"NHIF Payout: {payout} KES")