def conv_f_to_c(fahrenheit):
    # Convert Farenheit to Celsuis
    celsuis = (fahrenheit - 32) * 5/9
    return round(celsuis)

# Test cases
fahrenheit_values = [212, 90, 72, 32, 0, 40]
for temp in fahrenheit_values:
    current_temp_c = conv_f_to_c(temp)
    print(f"{temp}°F is {current_temp_c}°C")