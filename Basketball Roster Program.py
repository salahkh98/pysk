print("welcome to Basketball Roster Program.")

player = []

player.append(str(input("\nWho is your point guard: ").title()))
player.append(str(input("Who is your shooting guard: ").title()))
player.append(str(input("Who is your small forward: ").title()))
player.append(str(input("Who is your power forward: ").title()))
player.append(str(input("Who is your center: ").title()))


print("\n\tYour starting "+str(len(player))+" for the upcoming basketball season" )

print("\t\tPoint Guard:\t\t"+str(player[0]))
print("\t\tShooting Guard:\t\t"+str(player[1]))
print("\t\tSmall Forward:\t\t"+str(player[2]))
print("\t\tPower Forward:\t\t"+str(player[3]))
print("\t\tCenter:\t\t\t"+str(player[4]))

print("Oh no, "+str(player[2])+" injured.")
print("Your roster only has 4 players.")
replace_player = str(input("Who will take " + player[2] +" spot: "))
player.pop(2)

player.insert(2,replace_player)

print("\t\tPoint Guard:\t\t"+str(player[0]))
print("\t\tShooting Guard:\t\t"+str(player[1]))
print("\t\tSmall Forward:\t\t"+str(player[2]))
print("\t\tPower Forward:\t\t"+str(player[3]))
print("\t\tCenter:\t\t\t"+str(player[4]))

print("Good luck "+str(player[2])+" you will do great!")
print("Your roster now has "+str(len(player))+" players.")