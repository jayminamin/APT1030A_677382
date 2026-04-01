#include <iostream>
#include <iomanip>

using namespace std;

const double BASE_FARE = 200.0;
const double COST_PER_KM = 50.0;

int main() {
    double distance;
    
    cout << "Enter the trip distance in KM: ";
    cin >> distance;

    double totalFare = BASE_FARE + (distance * COST_PER_KM);

    cout << fixed << setprecision(2);
    cout << "Total Ride Fare: " << totalFare << " KES" << endl;

    return 0;
}