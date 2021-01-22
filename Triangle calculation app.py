import math 
print("welcom to the Triangle calculation app")
a = True
while a is True:
    first_inp = float(input("what is the first leg of triangle : "))
    second_inp = float(input("what is the second leg of triangle : "))

    calculation_hypotenuse = first_inp ** 2 + second_inp **2 
    result_sqr = math.sqrt(calculation_hypotenuse)
    hypotenuse_round = round(result_sqr , 3)

    calculation_area = 0.5 * (first_inp * second_inp)
    area_round = round( calculation_area , 3)

    
    print("the hypotenuse of triangle is : " , hypotenuse_round)
    print("the area of triangle is : " , area_round)
    print("----------------------")