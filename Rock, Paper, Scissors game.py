import random
print("Welcome to rock paper scissors.")

game_store = ["Rock","Paper","Scissors"]

plyer = 0
computer = 0

round_games = int(input("\nhow many round would you like to play: "))

for i in range(1,round_games+1):
    print("\nround "+str(i))
    print("player: "+str(plyer),"\tcomputer: "+str(computer))


    player_select = str(input("\nTime to pick....rock , paper , scissors: ").title().lstrip())
    computer_select = random.choice(game_store)
    
    print("computer: ",str(computer_select))
    print("player: ",str(player_select))
    
    if player_select == computer_select:
        print("\nIt is a tie")

    elif player_select == game_store[0] and computer_select == game_store[1]:
        computer += 1
        print("\ncomputer win")

    elif player_select == game_store[0] and computer_select == game_store[2]:
        plyer += 1
        print("\nyou win in this round")


    elif player_select == game_store[1] and computer_select == game_store[0]:
        plyer += 1
        print("\nyou win in this round")
        

    elif player_select == game_store[2] and computer_select == game_store[0]:
        computer += 1
        print("\nthe computer win")

    else:
        print("\nThat is not a valid game option \ncomputer gets the point")
        computer +=1



if plyer < computer:
    result = "computer win"
    
elif plyer > computer:
    result = "you win"
else:
    result = "equalize"

print("\nFinal Game results. "+"\n\t\tRounds Played: "+str(round_games),"\n\t\tplayer score: "+str(plyer),"\n\t\tcomputer score: "+str(computer),"\n\t\t"+str(result))

