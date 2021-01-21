print("welcom to the letter counter app .")
name = input("enter your name >>> ")
print("hi ",name , "\ni will count the number of times that a specific occurs in a massage")

inmassage = input("enter your massage here >>> ")

leter_choice = input("which letter would you like to count >>> ")

counle = inmassage.count(leter_choice)

print(name , "," , "your massage has" , counle, leter_choice ,"in it")
