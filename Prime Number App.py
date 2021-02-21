import time
print("Welcome to prime number app")

running = True

while running:

    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("choice the option 1 or 2: ").lstrip()
    if choice == "1":
        choice1 = int(input("Enter a number to determine if it a prime number or not: "))

        prime_status = True
        for i in range(2,choice1):
            if choice1 % i == 0:
                prime_status = False
                break
      
        if prime_status:
            print(str(choice1)+" is prime number")

        else:
            print(str(choice1)+" not prime number")

        stop_app = input("would you like to run again (y/n)").lower().lstrip()
        if stop_app != "y":
            running = False

    
    elif choice == "2":
        prime = []
        lower_range = int(input("ente the lower number in range: "))
        upper_range = int(input("ente the upper number in range: "))
        start_time = time.time()
        for i in range(lower_range+1,upper_range+1):
            prime_status = True
            for a in range(2,i):
                if i % a == 0:
                    prime_status = False
                    break
            if prime_status:
                prime.append(i)
        print("\nall prime number from "+str(lower_range)+" to "+str(upper_range))
        for i in prime:
            print(i)
        end_time = time.time()

        delta = round(start_time - end_time , 4)

        print("calculations took a total of "+str(delta)+" seconds.")
        stop_app = input("would you like to run again (y/n)").lower().lstrip()
        if stop_app != "y":
            print("Goodbye")
            running = False