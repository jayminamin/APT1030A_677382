def check_access(role):
    if role != "Doctor":
        raise PermissionError("Access Denied: Only Doctors can view patient records.")
    return "Access Granted: Patient Records Loading..."

# Execution
try:
    current_role = input("Enter your role: ")
    print(check_access(current_role))
except PermissionError as e:
    print(f"Security Alert: {e}")