print("welcome to the voter registrations app.")

inp_name = str(input("\nwhat is your name: "))
inp_age = int(input("what is your age: "))

parteis = ["Republican","Democratic","Independent","Libertarian","Green"]
if inp_age >= 18:
    print("congratulations "+ inp_name.title() + "! you are old enough to register to vote.")
    print("\nhere is a list of political parties to join.")
    
    for party in parteis:
        print("\t-",party)

    chosen_party = str(input("what party would you like to join: ").title().lstrip())

    if chosen_party in parteis:
        print("Congratulations",inp_name,"you have join the",chosen_party,"party")
        if chosen_party == 'Republican' or chosen_party == "Democratic":
            print("thate is major party !")

        elif chosen_party == 'Independent':
            print("you are independent person !")

        else:
            print("that is not major party")

    else:
        print("this not in the parteis list.")


else:
    print("you are not old enough to vote")