import random

print("Welcome to the coin Toss App.")
print("\ni will flip a coin a set number of times.")

HEADS = 0
TAILS = 0

flip_times = int(input("\nhow many times would you like me to flip the coin: "))

for i in range(flip_times):
    coin = random.randint(0,1)
    if coin == 0:
        HEADS +=1
        print("HEADS")

    else:
        TAILS +=1
        print("TAILS")

    if HEADS == TAILS:
        print("At "+str(i+1)+" flips, the number of heads and tails were equal at "+str(HEADS)+" each.")

print("\nResults Of Flipping A Coin "+str(flip_times)+" Times")

resulte_option = str(input("\nwould you like to see the resule of each flip (y/n): "))

heads = round(100*HEADS/flip_times,2)
tails = round(100*TAILS/flip_times,2)

if resulte_option is 'y':
    print("\nSide------------Count----------Percentage")
    print("Heads\t\t"+ str(HEADS)+"/"+str(flip_times)+"\t\t"+str(heads)+"%")
    print("Tails\t\t"+ str(TAILS)+"/"+str(flip_times)+"\t\t"+str(tails)+"%")

if resulte_option is 'n':
    print("Goodbye")


    
