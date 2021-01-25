print("welcom to the Binary/Hexadecimal converter app.")

numbers = int(input("\ncompute binary and hexadecimal values up to the following decimal number: "))

decimal = list(range(1,numbers + 1))
binary = []
hexadecimal = []
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))



print("\nGenerating list.....complete!")

print("\nusing slices, we will now show you a portion of each list.")

start_number = int(input("what decimal number would you like to start at: "))
stop_number = int(input("what decimal number would you like to stop at: "))

print("\nDecimal values from " + str(start_number) + " to " + str(stop_number) + " :")

for num in decimal[start_number:stop_number]:
    print(num)

print("\nBinary values from " + str(start_number) + " to " + str(stop_number) + " :")

for num in binary[start_number:stop_number]:
    print(num)


print("\nHexadecimal values from " + str(start_number) + " to " + str(stop_number ) + " :")

for num in hexadecimal[start_number:stop_number]:
    print(num)
    

all_values_massage = input("\nPress Enter to see all values from 1 " +"to "+ str(numbers) + ".")


print("Decimal---------Binary--------Hexadecimal")



for de , bi , hexa in zip(decimal, binary , hexadecimal):
    print(str(de) , "-----------", str(bi) , "------------",str(hexa))