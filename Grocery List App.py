import datetime
print("Welcom to the Grocery List App.")
print("Current Date and Time: ",datetime.datetime.today())
grocery_list = ["cheese","meat"]
print("You currently have",grocery_list[0],"and",grocery_list[1],"in your grocery list.")

first = grocery_list.append(input("\nType of food to add to the grocery list: ").lower())
second = grocery_list.append(input("Type of food to add to the grocery list: ").lower())
third = grocery_list.append(input("Type of food to add to the grocery list: ").lower())


print("\nHere is your grocery list:\n",grocery_list)
print("\nHere is your grocery list sorted:\n",sorted(grocery_list))
print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " , len(grocery_list),"items","\n",grocery_list)

list_buyer = input("what food did you just buy: ").lower()
while list_buyer not in grocery_list:
    print("this your list..." , grocery_list)
    list_buyer = input("what food did you just buy: ").lower()
print("Removing",list_buyer,"from list...")
grocery_list.remove(list_buyer)

print("\nCurrent grocery list: ",len(grocery_list),"items","\n",grocery_list)

list_buyer = input("what food did you just buy: ").lower()
while list_buyer not in grocery_list:
    print("this your list..." , grocery_list)
    list_buyer = input("what food did you just buy: ").lower()
print("Removing",list_buyer,"from list...")
grocery_list.remove(list_buyer)

print("\nCurrent grocery list: ",len(grocery_list),"items","\n",grocery_list)

list_buyer = input("what food did you just buy: ").lower()
while list_buyer not in grocery_list:
    print("this your list..." , grocery_list)
    list_buyer = input("what food did you just buy: ").lower()
print("Removing",list_buyer,"from list...")
grocery_list.remove(list_buyer)

print("\nCurrent grocery list: ",len(grocery_list),"items","\n",grocery_list)

grocery_list.remove("meat")
print("sorry, the store is out of meat")
instead_food = input("what food would you like instead: ").lower()
grocery_list.append(instead_food)


print("Here is what remains on your grocery list:","\n",grocery_list)
