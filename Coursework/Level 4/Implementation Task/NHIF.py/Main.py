from Insurance import Patient

# Create a patient instance
patient_1 = Patient("Jaymin", "NHIF-778899")

bill = 5000
payout = patient_1.calculate_claim(bill)

print(f"Patient: {patient_1.name}")
print(f"Total Bill: {bill} KES")
print(f"NHIF Payout (after 10% co-pay): {payout} KES")