BASE_FARE = 200
COST_PER_KM = 50

compute_fare = lambda dist: BASE_FARE + (dist * COST_PER_KM)

try:
    dist_input = float(input("Enter KM distance: "))
    print(f"Total Fare: {compute_fare(dist_input):.2f} KES")
except ValueError:
    print("Invalid input. Please enter a number.")