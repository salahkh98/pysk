import random

#this class to take data for the simulation
class Simulation():

    def __init__(self):

        self.days = 1

        #take population size
        print("To simulate an apidemic outbreak , we must know the population size.")
        self.pop_size = int(input("----Enter the population size: "))

        #take the percentage of the infected people will start with
        print("\nwe must first start by the infecting a portion of the population.")
        self.infection_precentage = float(input("----Enter the precentage (0-100) of the population to initially infect: "))
        self.infection_precentage /= 100

        #take the risk of the infection
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("----Enter the probability (0-100) that a person gets infected when exposed to the disease: "))

        #take the duration infection 
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("----Enter the duration (in days) of the infection: "))

        #take the mortality rate
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("----Enter the mortality rate (0-100) of the infection: "))

        #take how long the simulation will run in days
        print("\nWe must know how long to run the simulation")
        self.sim_days = int(input("----Enter the number of days to simulate: "))



class Person():

    def __init__(self , simulation):
        self.sim = simulation
        self.is_infected = False
        self.is_dead = False

        self.infected_days = 0
    
    def infect(self):

        if random.randint(0 , 100) < self.sim.infection_probability:
            self.is_infected = True    

    def heal(self):
        self.is_infected = False
        self.infected_days = 0

    def die(self):
        self.is_dead = True

    def update(self):

        if self.is_dead == False:
            if self.is_infected:
                self.infected_days += 1
            elif random.randint(0,100) < self.sim.mortality_rate:
                self.die()
            elif self.infected_days == self.sim.infection_duration:
                self.heal

            if self.is_infected:
                self.die()
            elif self.is_infected and not self.is_dead:
                self.heal()



class Population():

    def __init__(self , simulation):

        self.population = []

        for i in range(simulation.pop_size):
            person = Person(simulation)
            self.population.append(person)
    
    def initial_infection(self , simulation):

        count_infected  = int(simulation.infection_precentage * simulation.pop_size)
        
        for i in range(count_infected):
            self.population[i].is_infected = True
            self.population[i].infected_days = 1

        random.shuffle(self.population)


    def spread_infection(self):

        for i in range(len(self.population) - 1):

            if self.population[i].is_dead == False:
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect()
                elif i < len(self.population)-1:
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect()
                elif i == len(self.population)-1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect()


    def update(self , simulation):

        simulation.days += 1

        for person in self.population:
            person.update()


    def display_info(self , simulation):

        total_infected_people = 0
        total_deaths_people = 0

        for person in self.population:
            if person.is_infected:
                total_infected_people +=1
            elif person.is_dead:
                total_deaths_people +=1
        
        infection_percent  = round(100*(total_infected_people / simulation.pop_size) , 4)
        death_percent = round(100*(total_deaths_people / simulation.pop_size) , 4)

        print("----day " + str(simulation.days) + "----")
        print()
        print("population size : " + str(simulation.pop_size))
        print()
        print("total infected : " + str(total_infected_people) + "/" + str(simulation.pop_size))
        print()
        print("total deths : " + str(total_deaths_people) + "/" + str(simulation.pop_size))
        print()
        print("infected percentage : " + str(infection_percent) + "/" +  " %100")
        print()
        print("deaths percentage : " + str(death_percent) + "/" + " %100")
        print()

    def graphic(self):

        population_char = []
        infection = 'O'
        heal = 'I'
        die = 'X'

        for person in self.population:
            if person.is_infected:
                population_char.append(infection)
            elif person.is_dead:
                population_char.append(die)
            else:
                population_char.append(heal)

        for letter in population_char:
            print(letter , end="-")



sim = Simulation()

population = Population(sim)

input("press enter to begin the simulation: ")
for i in range(sim.sim_days):
    population.initial_infection(sim)
    population.spread_infection()
    population.display_info(sim)
    population.update(sim)
    population.graphic()
    input("Press enter to advanced to the next day: ")




        