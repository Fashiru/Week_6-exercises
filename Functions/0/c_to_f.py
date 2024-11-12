def conv_c_to_f(celsuis):
    fahrenheit = celsuis * 9 / 5 + 32
    return round(fahrenheit)

#Test
celsuis_values = [100, 45, 19, 0, -7, -40]
for temp in celsuis_values:
    current_temp_F = conv_c_to_f(temp)
    print(f"{temp}°C is {current_temp_F}°F")
    