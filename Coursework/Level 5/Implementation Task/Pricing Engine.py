class PricingEngine:
    def __init__(self, base_fare, cost_per_km):
        self.base_fare = base_fare
        self.cost_per_km = cost_per_km

    def calculate_total(self, distance):
        return self.base_fare + (distance * self.cost_per_km)

nairobi_engine = PricingEngine(base_fare=200, cost_per_km=50)

try:
    user_dist = float(input("Enter distance for Nairobi trip (KM): "))
    print(f"Total Fare: {nairobi_engine.calculate_total(user_dist):.2f} KES")
except ValueError:
    print("Please enter a valid numerical distance.")