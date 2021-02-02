print("Welcome to Shipping Accounts Program")

uesers = ["salahkh98","noorkh20"]

username_inp = str(input("hello, what is your username: "))

a_0_100 = 5.10
a_100_500 = 5.00
a_500_1000 = 4.95
a_over_1000 = 4.80

if username_inp in uesers:
    print("Hello " + username_inp + "." + "welcome to you account.")
    print("current shipping prices are as follows:")
    print("\nShipping oredrs 0 to 100","\t\t$"+str(a_0_100))
    print("Shipping oredrs 100 to 500","\t\t$"+str(a_100_500))
    print("Shipping oredrs 500 to 1000","\t\t$"+str(a_500_1000))
    print("Shipping oredrs over 1000","\t\t$"+str(a_over_1000))
    quantity = int(input("\nHow many items would you like to ship: "))
    if quantity <= 100:
        cal = float(quantity * a_0_100)
        print("to ship "+str(quantity)+" items it will cost you $"+str(round(cal,2))+" at $"+str(round(a_0_100,2)) + " per item")
    
    elif quantity <= 500:
        cal = float(quantity * a_100_500)
        print("to ship "+str(quantity)+" items it will cost you $"+str(round(cal,2))+" at $"+str(round(a_100_500,2)) + " per item")
    
    elif quantity <= 1000:
        cal = float(quantity * a_500_1000)
        print("to ship "+str(quantity)+" items it will cost you $"+str(round(cal,2))+" at $"+str(round(a_500_1000,2)) + " per item")
    
    elif quantity > 1000:
        cal = float(quantity * a_over_1000)
        print("\nto ship "+str(quantity)+" items it will cost you $"+str(round(cal,2))+" at $"+str(round(a_over_1000,2)) + " per item")




    confirmation = str(input("would you like to place this order (y/n): "))
    if confirmation is 'y':
        print("okay. Shipping your",str(quantity),"items.")
    elif confirmation is 'n':
        print("okey. your order canceled")

    else:
        print("value error")

else:
    print("sorry you doin't have account")