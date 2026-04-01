def record_session():
    patient_id = "PAT-9901" # Local scope
    print(f"Inside function: {patient_id}")

record_session()

# Attempting access outside
print(f"Outside function: {patient_id}")
