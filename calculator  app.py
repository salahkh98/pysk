print("welcom to the calculater app")

def sums(x,y):
    return x + y

def multiply(x,y):
    return x * y


def devision(x,y):
    return x / y

def subtract(x,y):
    return x - y


def fibonacci(x):
    fib = [1,1]
    for i in range(x-2):
        new_fib = fib[i]+fib[i+1]
        fib.append(new_fib)
    return fib


running = True

while running:
    print("opreation number 1 is (+)")
    print("opreation number 2 is (-)")
    print("opreation number 3 is (*)")
    print("opreation number 4 is (/)")
    print("opreation number 5 is (fibonacci)")
    opreation = int(input("enter the opreation: "))
    
    if opreation == 1: 
        first_number = int(input("enter the first number: "))
        second_number = int(input("enter the second number: "))
        sum1 = sums(first_number,second_number)
        print("\n"+str(first_number)+" + "+str(second_number)+" = ",str(sum1))

    elif opreation == 2:
        first_number = int(input("enter the first number: "))
        second_number = int(input("enter the second number: "))       
        subtract1 = subtract(first_number,second_number)
        print("\n"+str(first_number)+" - "+str(second_number)+" = "+str(subtract1))

    elif opreation == 3:
        first_number = int(input("enter the first number: "))
        second_number = int(input("enter the second number: "))
        mul = multiply(first_number,second_number)
        print("\n"+str(first_number)+" * "+str(second_number)+" = "+str(mul))

    elif opreation == 4:
        first_number = int(input("enter the first number: "))
        second_number = int(input("enter the second number: "))
        dev = devision(first_number,second_number)
        print("\n"+str(first_number)+" / "+str(second_number)+" = "+str(dev))

    elif opreation == 5:
        rang_fib = int(input("enter the rang of the fibonacci: "))
        fib = fibonacci(rang_fib)
        for i in fib:
            print(i)

    else:
        print("worng value")
        running = False
        break