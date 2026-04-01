rainfall = float(input("Enter rainfall (mm): "))
temperature = float(input("Enter temperature (°C): "))

if rainfall < 200:
    print("Irrigation Required")
elif rainfall >= 200 and temperature > 30:
    print("Monitor Soil")
else:
    print("Normal Conditions")