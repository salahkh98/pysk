print("Welcome to the Even and odd number sorter app.")


running  = True

while running:
    ran = input("enter the string of numbers separated by a comma (,): ")
    ran = ran.replace(" ","")
    new_list = ran.split(",")
    even = []
    odd = []
    for i in new_list:
        new = int(i)
        if new % 2 ==0:
            even.append(new)
            print("\nthis even number: "+str(new))

        else:
            odd.append(new)
            print("\nthis odd number: "+str(new))


    print("\nthe even numbers are: ")
    for i in even:
        print(i)
    print("\nthe odd numbers are: ")
    for i in odd:
        print(i)

    choice = input("run again (y/n): ")
    if choice != "y":
        running = False