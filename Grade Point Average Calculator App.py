print("welcome to the grade calculator.")

name = input("\nwhat is your name: ")

inp_grade = int(input("\nenter the number of the grades: "))

list_grades = []
for num in range(1,inp_grade+1):
    value_grade = int(input("Enter grade: "))
    list_grades.append(value_grade)

list_grades.sort(reverse=True)

print("\nthe grades from highest to lowest:")

for num in list_grades:
    print("\t",num)


print("\n",name,"grade summary")
print("\tTotal of grades is: ",str(len(list_grades)))
print("\tthe highest grade is: ",list_grades[0])
print("\tthe lowest grade is: ",list_grades[-1])
average = sum(list_grades)/len(list_grades)
print("\tAverage: ",round(average,2))

desired = float(input("what is your desired grade: "))

avrage = desired*len(list_grades) - sum(list_grades)

print("\nGood luck",name.title())

print("you will need to get",avrage,"to earn a",int(desired),"average.")

change_value = int(input("what grade would you like to change: "))
change_value2 = int(input("\nwhat grade would you like to change "+str(change_value)+" to: "))

add = change_value + change_value2
list_grades.remove(change_value)
list_grades.append(add)


list_grades.sort(reverse=True)
print("new grades from highest to lowest:")

for num in list_grades:
    print("\t",num)


print("\n",name,"new grade summary:")

print("\ttotal number of grades:",len(list_grades))
print("\tthe highest grade:",list_grades[0])
print("\tthe lowest grade:",list_grades[-1])
average2 = sum(list_grades)/len(list_grades)
print("\tAverage:",round(average2,2))

print("your new average is",average2,"compared to your real average of",average,"!")
changes = average2 - average
print("that is change of",float(changes),"points")