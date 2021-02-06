import random
print("welcome to Guess my number app.")

name = str(input("what is your name: "))

ran_num = int(input("what the range of numbers would you like to play with: "))
print("hello",name,"I am thinking of a number between 1 and "+str(ran_num))

ran = random.randint(1,ran_num)

guess_counter = []

for r in range(5):
    guess = int(input("Take a Guess: "))
    guess_counter.append(guess)
    if guess > ran:
        print("too high")

    elif guess < ran:
        print("too low")

    else:
        break

if guess == ran:
    print("good job",name,"you guessed my number in",len(guess_counter),"guesses")

else:
    print("Game Over . the number i was thinking of was",str(ran),".")
