name = input("Enter student name: ")
units = int(input("Enter number of registered units: "))

status = "Overload – Approval Required" if units > 7 else "Registration Accepted"

print("\n--- Final Summary ---")
print(f"Student Name: {name}")
print(f"Units: {units}")
print(f"Status: {status}")
