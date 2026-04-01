rainfall = float(input("Enter rainfall (mm): "))
temperature = float(input("Enter temperature (°C): "))

if rainfall < 200:
    print("Irrigation Required")
else:
    # This block only runs if rainfall >= 200
    if temperature > 30:
        print("Monitor Soil")
    else:
        print("Normal Conditions")