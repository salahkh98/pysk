
print("Welcome to the Factor Generator app")


running = True

while running:
    
    a = []
    
    number = int(input("enter the number: "))

    for i in range(1,number+1):
        if number % i == 0:
            a.append(i)
            

    print("the factor of "+str(number)+" are: ")
    for i in a:
        print(i)

    print("in summary: ")
    for i in range(int(len(a)/2)):
        print(str(a[i]) + " * " +str(a[-i-1]) + " = " +str(number))

    choice = input("\nrun again (y/n): ")
    if choice !="y":
        running = False