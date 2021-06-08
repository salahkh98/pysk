from matplotlib import pyplot

def get_loan_info():
    loan = {}
    loan["princaple"] = float(input("enter the loan: "))
    loan["rate"] = float(input("enter the intrest rate: "))/100
    loan["monthly payment"] = float(input("enter the monthly payment: "))
    loan["money paid"] = 0
    return loan

def show_info(loan , number):
    print("-----------loan information in " , str(number) , "-----------------")
    for k , v in loan.items():
        print(str(k.title()) + " : "+ str(v))

def collect_intrest(loan):
    loan["princaple"] = loan["princaple"] + loan["princaple"]*loan["rate"]/12


def make_monthly_payment(loan):
    loan["princaple"] = loan["princaple"] - loan["monthly payment"]
    if loan["princaple"] > 0:
        loan["money paid"] += loan["monthly payment"]

    else:
        loan["money paid"] += loan["monthly payment"] + loan["princaple"]
        loan["princaple"] = 0

def summuraize_loan(loan , number , initial_princaple):
    print("\ncongraulations you have paid off your loan in" + str(number) + " months.")
    print("your initial loan was $" + str(initial_princaple) + " at a rate of " + str(100 * loan["rate"]) + "%.")
    print("your monthly payment $" + str(loan["monthly payment"]) + ".")
    print("you spent $" + str(round(loan["money paid"] , 2)) + " in total")
    interest = round(loan["money paid"] - initial_princaple , 2)
    print("you spent $" + str(interest) + " on interest.")

def creat_graph(data , loan):
    x_values = []
    y_values = []

    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])
    
    pyplot.plot(x_values,y_values)
    pyplot.title(str(100*loan["rate"]) + "% interest with $" + str(loan["monthly payment"]) + " monthly payment")
    pyplot.xlabel("month number")
    pyplot.ylabel("princaple of loan")
    
    pyplot.show()


print("welcome to loan calculator APP")

month_number = 0
my_loan = get_loan_info()
starting_princaple = my_loan["princaple"]
data_to_plot = []
show_info(my_loan , month_number)
input("Press ENTER TO begin paying off your loan")

while my_loan["princaple"] > 0:
    if my_loan["princaple"] > starting_princaple:
        break
    month_number += 1
    collect_intrest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number , my_loan["princaple"]))
    show_info(my_loan , month_number)



if my_loan["princaple"] <= 0:
    summuraize_loan(my_loan , month_number , starting_princaple)
    creat_graph(data_to_plot , my_loan)

else:
    print("you will never pay off the loan!!!!")
    print("you cannot get ahead of the interest")