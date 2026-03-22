VALID_USER = "adminKE"
VALID_PASS = "254Secure"

def login():
    user_input = input("Enter Username: ")
    pass_input = input("Enter Password: ")

    if user_input == VALID_USER and pass_input == VALID_PASS:
        print("Access Granted")
    else:
        print("Invalid Credentials")

if __name__ == "__main__":
    login()