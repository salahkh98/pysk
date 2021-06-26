import random

    
class Creature():
    def __init__(self , name):
        self.level = 0
        self.name = name
        self.round = 0
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food_inventory = 2
        self.awake = True
        self.choice = 0
        self.die = False


    def draw_info(self):
        print("\nround #"   + str(self.round))
        print("Creature Name "  + self.name.title())
        print("Hunger (0-10) "  + str(self.hunger))
        print("Boredom (0-10) " + str(self.boredom))
        print("Tiredness (0-10) " + str(self.tiredness))
        print("Dirtiness (0-10) " + str(self.dirtiness))
        print("\nFood Inventory  " + str(self.food_inventory))
        if self.awake == False:
            self.awake = "sleeping"
        elif self.awake == True:
            self.awake = "awake"
        print("Current Status "  + str(self.awake))


    def choices(self):
        print("\nEnter (1) to eat.")
        print("Enter (2) to play.")
        print("Enter (3) to sleep.")
        print("Enter (4) to take a bath.")
        print("Enter (5) to forage for food.")
        self.choice = int(input("\nwhat is your choice: "))
        while self.choice <= 0 or self.choice > 5:
            print("this not in the list......")
            self.choice = int(input("\nwhat is your choice: "))
        return self.choice


    def level_diffculty(self):
        self.level = int(input("please choose a difficulty level (1-5): " ))
        while self.level <= 0 or self.level > 5:
            print("this not available level....")
            self.level = int(input("please choose a difficulty level (1-5): " ))
        return self.level


    def dead(self):
        if self.dirtiness >= 10:
            print("R.I.P.")
            print("\n"+self.name +  " has suffered an infection and died....")
            self.die = True
            if self.die == True:
                print("\n"+self.name + " survived a total of " + str(self.round) + " rounds.")

        elif self.hunger >= 10:
            print("R.I.P.")
            print(self.name +  " has died of starvation....")
            self.die = True
            if self.die == True:
                print("\n"+self.name + " survived a total of " + str(self.round) + " rounds.")


    def eat(self):
        if self.hunger == 0:
            print("\n"+self.name + " he is not hungry!!")
        elif self.hunger <= 10:
            if self.food_inventory != 0:
                print("\nYumm! "  + self.name +  " ate a great meal !")
                self.hunger -= 1
                self.food_inventory -= 1
            else:
                print("sorry you don't have enough food in the ")
        
    def play(self):
        if self.boredom == 0:
            print("\n"+self.name + " he don't want to play!!")

        elif self.boredom > 0 and self.boredom < 10:
            rand_num = random.randint(1,5)
            print(self.name +  " wants to play a game.")
            print(self.name +  " is thinking of a number between 1---5: ")
            guess_num = int(input("what is your guess: "))
            if guess_num != rand_num:
                print("\nWRONG! "  + self.name +  " was thinking of " + str(rand_num))
                self.boredom -= 1
            else:
                print("\ngreat you are guessing what " + self.name + " was thinking")
                self.boredom -= 2
        

    def auto_sleep(self):
        if self.tiredness >= 10:
            self.awake = False
            self.tiredness = 0
        elif self.boredom >= 10:
            self.awake = False
            self.boredom = 0

        
    def sleep(self):
        if self.tiredness > 0 and self.tiredness < 10:
            self.awake = False
            print(self.name +  " is sleeping now")
            print("zzzzzzzz ,zzzzzzzzzzzz ,zzzzzzzzz")
            self.tiredness -=1



    def wake_up(self):
        if self.awake == False:
            input("\npress Enter to try and wake up")
            rand_num_sleep = random.randint(0,2)
            while rand_num_sleep == 0:
                input("press Enter to try and wake up")
                rand_num_sleep = random.randint(0,2)
            if rand_num_sleep != 0:
                print(self.name +  "just woke up!")
                self.awake = True


    def take_bath(self):
        if self.dirtiness == 0:
            print("\n"+self.name + " no need to take bath....")
        elif self.dirtiness < 10:
            print("\n"+self.name +  " has taken a bath. All clean")
            self.dirtiness = 0

    def forge_food(self):
            rand_inventory = random.randint(1,4)
            print("\n"+self.name + " found " + str(rand_inventory) + " pieces of food!")
            self.food_inventory += rand_inventory
            self.dirtiness = 2

        

    def round_increase(self , level):
        if self.round > 0:
            if level == 1:
                ran_num = random.randint(0,1)
                self.hunger += ran_num
                ran_num2 = random.randint(0,1)
                self.boredom += ran_num2
                ran_num3 = random.randint(0,1)
                self.tiredness += ran_num3
                ran_num4 = random.randint(1,1)
                self.dirtiness += ran_num4


            elif level == 2:
                ran_num = random.randint(0,2)
                self.hunger += ran_num
                ran_num2 = random.randint(0,2)
                self.boredom += ran_num2
                ran_num3 = random.randint(0,2)
                self.tiredness += ran_num3
                ran_num4 = random.randint(1,2)
                self.dirtiness += ran_num4
                
            elif level == 3:
                ran_num = random.randint(1,2)
                self.hunger += ran_num
                ran_num2 = random.randint(1,2)
                self.boredom += ran_num2
                ran_num3 = random.randint(1,3)
                self.tiredness += ran_num3
                ran_num4 = random.randint(2,3)
                self.dirtiness += ran_num4
                
            elif level == 4:
                ran_num = random.randint(1,3)
                self.hunger += ran_num
                ran_num2 = random.randint(1,3)
                self.boredom += ran_num2
                ran_num3 = random.randint(1,3)
                self.tiredness += ran_num3
                ran_num4 = random.randint(1,4)
                self.dirtiness += ran_num4
                
            elif level == 5:
                ran_num = random.randint(2,3)
                self.hunger += ran_num
                ran_num2 = random.randint(2,3)
                self.boredom += ran_num2
                ran_num3 = random.randint(2,3)
                self.tiredness += ran_num3
                ran_num4 = random.randint(2,5)
                self.dirtiness += ran_num4

    def summary(self):
        print("\nround #"+ str(pet.round) + " summary")
        print("Creature Name "  + self.name.title())
        print("Hunger (0-10) "  + str(self.hunger))
        print("Boredom (0-10) " + str(self.boredom))
        print("Tiredness (0-10) " + str(self.tiredness))
        print("Dirtiness (0-10) " + str(self.dirtiness))
        print("\nFood Inventory  " + str(self.food_inventory))
        if self.awake == False:
            self.awake = "sleeping"
        elif self.awake == True:
            self.awake = "awake"
        print("Current Status "  + str(self.awake))


name = input("what name would you like to give your pet: ")
pet = Creature(name)
level = pet.level_diffculty()
pet.draw_info()
choice = pet.choices()
pet.round = 1
running = True
while running:

    if choice == 1:
        pet.dead()
        if pet.die:
            running = False
            break
        else:
            pet.auto_sleep()
            pet.wake_up()
            pet.eat()
            pet.summary()
            input("\nPress (enter) to continue....")
            pet.round += 1
            pet.round_increase(level)
            pet.draw_info()
            choice = pet.choices()
            

    elif choice == 2:
        pet.dead()
        if pet.die:
            running = False
            break
        else:
            pet.auto_sleep()
            pet.wake_up()
            pet.play()
            pet.summary()
            input("\nPress (enter) to continue....")
            pet.round += 1
            pet.round_increase(level)
            pet.draw_info()
            choice = pet.choices()


    elif choice == 3:
        pet.dead()
        if pet.die:
            running = False
            break
        else:
            pet.auto_sleep()
            pet.sleep()
            pet.wake_up()
            pet.summary()
            input("\nPress (enter) to continue....")
            pet.round += 1
            pet.round_increase(level)
            pet.draw_info()
            choice = pet.choices()
            
    elif choice == 4:
        pet.dead()
        if pet.die:
            running = False
            break
        else:
            pet.auto_sleep()
            pet.wake_up()
            pet.take_bath()
            pet.summary()
            input("\nPress (enter) to continue....")
            pet.round += 1
            pet.round_increase(level)
            pet.draw_info()
            choice = pet.choices()

    elif choice == 5:
        pet.dead()
        if pet.die:
            running = False
            break
        else:
            pet.auto_sleep()
            pet.wake_up()
            pet.forge_food()
            pet.summary()
            input("\nPress (enter) to continue....")
            pet.round += 1
            pet.round_increase(level)
            pet.draw_info()
            choice = pet.choices()

    

    


        
