print("welcome to the Favorite Teachers Program.")

teachers = []

teachers.append(str(input("\nWho is your first favorite eachers: ")))
teachers.append(str(input("Who is your second favorite eachers: ")))
teachers.append(str(input("Who is your third favorite eachers: ")))
teachers.append(str(input("Who is your fourth favorite eachers: ")))

print("\nyour favorite teachers ranked are >>> ",teachers)
print("your favorite teachers alphabetically are >>>",sorted(teachers))
print("your favorite teachers in reverse alphabetically order are >>>",sorted(teachers,reverse=True))

print("\nyour top two teachers are:",teachers[0],"and",teachers[1])
print("your next favorite teachers are:",teachers[2],"and",teachers[3])
print("your last favorite teacher is:",teachers[3])
print("you have a total" , str(len(teachers)) , "favorite teachers")

add_teacher = str(input("\noops, " + teachers[0].upper() +" is no longer your first favorite teacher. who is your new FAVORITE techer: "))
teachers.insert(0,add_teacher)

print("\nyour favorite teachers ranked are >>> ",teachers)
print("your favorite teachers alphabetically are >>>",sorted(teachers))
print("your favorite teachers in reverse alphabetically order are >>>",sorted(teachers,reverse=True))


print("\nyour top two teachers are:",teachers[0],"and",teachers[1])
print("your next favorite teachers are:",teachers[2],"and",teachers[3])
print("your last favorite teacher is:",teachers[4])
print("you have a total" , str(len(teachers)) , "favorite teachers")

remove_teacher = str(input("\nyou've decided you no longer like a teacher. which teacher would you like to remove from your list: "))
teachers.remove(remove_teacher)


print("\nyour favorite teachers ranked are >>> ",teachers)
print("your favorite teachers alphabetically are >>>",sorted(teachers))
print("your favorite teachers in reverse alphabetically order are >>>",sorted(teachers,reverse=True))

print("\nyour top two teachers are:",teachers[0],"and",teachers[1])
print("your next favorite teachers are:",teachers[2],"and",teachers[3])
print("your last favorite teacher is:",teachers[3])
print("you have a total" , str(len(teachers)) , "favorite teachers")