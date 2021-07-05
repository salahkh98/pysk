import random

class Pykemon():

    #def the main attributs of the pykemon
    
    def __init__(self , name , element  , health , speed):

        self.name = name.title()

        self.element = element

        self.current_health = health

        self.max_health = health

        self.speed = speed


        self.is_alive = True


    def light_attack(self , enemy):

        damage = random.randint(15 , 25)

        print("\nPykemon " + self.name + " used " + self.moves[0])
        print("Its dealt " + str(damage) + " damage.") 

        enemy.current_health -= damage


    def heavy_attack(self , enemy):

        damage = random.randint(0 , 50)

        print("\nPykemon " + self.name + "used " + self.moves[1])
        
        if damage < 10:
            print("\nthe attack missed!!!")
        else:
            print("\nIts dealt " + str(damage) + " damage.")
            enemy.current_health -= damage



    def restor(self):
        heal = random.randint(15 , 30)

        print("\nPykemon " + self.name + " used " + self.moves[2])
        print("Its healed " + str(heal) + " health point.")

        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health



    def faint(self):

        if self.current_health <= 0:
            self.is_alive = False
            print("\nOH NO !!! Pykemon " + self.name  + " has fainted")
            input("Press enter to continue: ")

        

    def show_info(self):

        print("\nName : " + self.name)
        print("_________________________")
        print("\nElement type : " + self.element)
        print("_________________________")
        print("\nHealth : " + str(self.current_health) + " / " + str(self.max_health))
        print("_________________________")
        print("\nSpeed : " + str(self.speed))
        print("_________________________")



    
class Fire(Pykemon):

    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)

        self.moves = ["normall"  , "hard attack " , "restor health " , " special attack"]


    def special_attack(self , enemy):

        print("\n\nPykemon " + self.name + " used " + self.moves[3])
        if enemy == "GRASS":
            print("Its SUPER effective!!!")
            damage = random.randint(30 , 50)
        elif enemy == "WATER":
            print("Its not very effective.......")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10 , 25)
            

        print("\nIts dealt " + str(damage) + " damage.")
        enemy.current_health -= damage


    def move_info(self):

        
        print("\n" + self.name + " Moves: ")

        #light attack
        print("-- " + self.moves[0] + " --")
        print("\tAn efficent attack....")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        #heavy attack
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack.....")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # restore move
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move....")
        print("\tGuaranteed to heal your pykemon 15 to 25 damage points.")

        #special attack
        print("-- " + self.moves[2] + " --")
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")

        print()
        print("---------------------------------------------------------------------------------------------")


class Water(Pykemon):

    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)

        self.moves = ["normal" , " hard attack " , " restor health" , "special attack"]


    def special_attack(self , enemy):

        print("\n\nPykemon " + self.name + " used " + self.moves[3])
        if enemy == "FIRE":
            print("Its SUPER effective!!!")
            damage = random.randint(30 , 50)
        elif enemy == "GRASS":
            print("Its not very effective.......")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10 , 25)
            

        print("\nIts dealt " + str(damage) + " damage.")
        enemy.current_health -= damage


    def move_info(self):

        
        print("\n" + self.name + " Moves: ")

        #light attack
        print("-- " + self.moves[0] + " --")
        print("\tAn efficent attack....")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        #heavy attack
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack.....")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # restore move
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move....")
        print("\tGuaranteed to heal your pykemon 15 to 25 damage points.")

        #special attack
        print("-- " + self.moves[2] + " --")
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")


        print()
        print("---------------------------------------------------------------------------------------------")



class Grass(Pykemon):

    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)

        self.moves = ["normal" , " hard attack " , " restor health" , "special attack"]

    def special_attack(self , enemy):

        print("\n\nPykemon " + self.name + " used " + self.moves[3])
        if enemy == "WATER":
            print("Its SUPER effective!!!")
            damage = random.randint(30 , 50)
        elif enemy == "FIRE":
            print("Its not very effective.......")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10 , 25)
            

        print("\nIts dealt " + str(damage) + " damage.")
        enemy.current_health -= damage


    def move_info(self):

        
        print("\n" + self.name + " Moves: ")

        #light attack
        print("-- " + self.moves[0] + " --")
        print("\tAn efficent attack....")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        #heavy attack
        print("-- " + self.moves[1] + " --")
        print("\tAn risky attack.....")
        print("\tCould deal damage up to 50 damage points or as little as 0 damage points.")

        # restore move
        print("-- " + self.moves[2] + " --")
        print("\tA restorative move....")
        print("\tGuaranteed to heal your pykemon 15 to 25 damage points.")

        #special attack
        print("-- " + self.moves[2] + " --")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")


        print()
        print("---------------------------------------------------------------------------------------------")


class Game():

    def __init__(self):

        self.element_pykemon = ["WATER" , "FIRE" , "GRASS"]

        self.pykemon_name = ["Chewdie" , "Spatol" , "Burnmander" , "Pykachu" , "Pyonx" , "Abbacab" ,
                             "Sweetil" , "Jampot" , "Hownstooth" , "Swagilybo" , "Muttle" , "Zantbat",
                             "Wiggly Poof" , "Rubblesaur"]

        self.battle_won = 0



    def create_pykemon(self):

        name = self.pykemon_name[random.randint(0 , len(self.pykemon_name))-1]

        element = self.element_pykemon[random.randint(0 , len(self.element_pykemon))-1]

        health = random.randint(70 , 95)

        speed = random.randint(5 , 10)

        if element == "FIRE":
            pykemon = Fire(name , element , health , speed)
        elif element == "WATER":
            pykemon = Water(name , element , health , speed)
        else:
            pykemon = Grass(name , element , health , speed)

        return pykemon

    def choose_pykemon(self):

        pykemons = []

        while len(pykemons) < 3:
            pykemon = self.create_pykemon()

            valid_pykemon = True
            for py in pykemons:
                if py.name == pykemon.name or py.element == pykemon.element:
                    valid_pykemon = False
            
            if valid_pykemon:
                pykemons.append(pykemon)

        for pyk in pykemons:
            pyk.show_info()
            pyk.move_info()

        print("\nhere a list of some pykemons you can pick one of it: ")
        print("(1) - " + pykemons[0].name)
        print("(2) - " + pykemons[1].name)
        print("(3) - " + pykemons[2].name)
        choice = int(input("which pykemon would you like to choose: "))
        while choice > 3:
            choice = int(input("which pykemon would you like to choose: "))

        print("\ngreat you choose " + pykemons[choice -1].name + " good luck with it")

        player_pykemon = pykemons[choice - 1]

        return player_pykemon


    def get_attack(self , player):
        
        print("\n\n" + "(1) - " + player.moves[0])
        print("(2) - " + player.moves[1])
        print("(3) - " + player.moves[2])
        print("(4) - " + player.moves[3])


        choice = int(input("what would you like to do: "))
        while choice > 4:
            choice = int(input("what would you like to do: "))

        return choice

    def player_attack(self , move , player , computer):

        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restor()
        elif move == 4:
            player.special_attack(computer)

        computer.faint()



    def computer_attack(self, player , computer):
        move = random.randint(1 , 4)

        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restor()
        elif move == 4:
            computer.special_attack(player)

        player.faint()


    
    def battle(self , player , computer):
        move = self.get_attack(player)
        
        if player.speed > computer.speed:
            self.player_attack(move , player , computer)
            if computer.is_alive:
                self.computer_attack(player , computer)
        else:
            self.computer_attack(player , computer)
            if player.is_alive:
                self.player_attack(move , player , computer)



input("\nPress Enter to choose your Pykemon!")

run = True
while run:
    game = Game()

    player = game.choose_pykemon()
    player.show_info()
    
    input("\nPress enter to start the fight: ")
    while player.is_alive:
        computer = game.create_pykemon()

        print("\nOh No!! your enemy is " + computer.name + " be careful.......")
        computer.show_info()

        while player.is_alive and computer.is_alive:
            game.battle(player , computer)

            if player.is_alive and computer.is_alive:
                player.show_info()
                print()
                print()
                computer.show_info()


        if player.is_alive:
            game.battle_won += 1
            
    print("\nyour pykemon " + player.name + " has faint!!")
    print("your pykemon has won " + str(game.battle_won) + " battles")        


    play_again = input("\nwould you like to play again (y / n):  ")

    if play_again != "y":
        run = False
        print("thank you for playing pykemon!")


                








