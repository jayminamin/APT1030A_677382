#include <iostream>
#include <string>

int main() {
    std::string validUser = "adminKE";
    std::string validPass = "254Secure";

    std::string userInput, passInput;

    std::cout << "Enter Username: ";
    std::cin >> userInput;

    std::cout << "Enter Password: ";
    std::cin >> passInput;

    if (userInput == validUser && passInput == validPass) {
        std::cout << "Access Granted" << std::endl;
    } else {
        std::cout << "Invalid Credentials" << std::endl;
    }

    return 0;
}