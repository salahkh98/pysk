print("welcome to Temperatur converter program")

temp_col = float(input("what is the given Temperatur in degrees Fahrenheit >>> "))

count_Celsius = round((temp_col - 32) * 5/9)

count_Kelvin = round((temp_col + 459.67) * 5/9)

print("degrees Fahrenheit " , temp_col , "°F")
print("degrees Celsius " , count_Celsius , "°C")
print("degrees Kelvin " , count_Kelvin , "K")

