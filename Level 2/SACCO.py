member_name = input("Enter Member Name: ")
member_id = input("Enter Member ID: ")

contributions = []

print("Enter contributions for 6 months:")
for i in range(1, 7):
    amount = float(input(f"Month {i}: "))
    contributions.append(amount)

total_savings = sum(contributions)

print(f"\n--- SACCO Statement ---")
print(f"Member: {member_name} (ID: {member_id})")
print(f"Total Savings: KES {total_savings}")