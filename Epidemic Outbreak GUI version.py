import tkinter
import random
import math

class Simulation():

    def __init__(self):

        self.days = 1

        #take population size
        print("To simulate an apidemic outbreak , we must know the population size.")
        self.pop_size = int(input("----Enter the population size: "))

        root = math.sqrt(self.pop_size) 
        if int(root + .5)**2 != self.pop_size:
            root = round(root , 0)
            self.grid_size = int(root)
            self.pop_size = self.grid_size**2
            print("the perfect sqrt is " + str(self.pop_size) + " for visual purpose")
        else:
            self.grid_size = int(math.sqrt(self.pop_size))


        print("\nwe must first start by the infecting a portion of the population.")
        self.infection_precentage = float(input("----Enter the precentage (0-100) of the population to initially infect: "))
        self.infection_precentage /= 100

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("----Enter the probability (0-100) that a person gets infected when exposed to the disease: "))

        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("----Enter the duration (in days) of the infection: "))

        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("----Enter the mortality rate (0-100) of the infection: "))

        print("\nWe must know how long to run the simulation")
        self.sim_days = int(input("----Enter the number of days to simulate: "))



class Person():

    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.infected_days = 0

    
    def infect(self , sim):

        if random.randint(0 , 100) < sim.infection_probability:
            self.is_infected = True    

    def heal(self):
        self.is_infected = False
        self.infected_days = 0

    def die(self):
        self.is_dead = True

    def update(self , sim):

        if self.is_dead == False:
            if self.is_infected:
                self.infected_days += 1
                if random.randint(0,100) < sim.mortality_rate:
                    self.die()
                elif self.infected_days == sim.infection_duration:
                    self.heal()



class Population():

    def __init__(self , simulation):
        self.population = []

        for i in range(simulation.grid_size):
            row = []
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            
            self.population.append(row)
                

    def initial_infection(self , simulation):

        infected_count = int(round(simulation.infection_precentage * simulation.pop_size  , 0))

        infections = 0

        while infections < infected_count:

            #x represent the row number and y represent the persom=n inside the row 
            x = random.randint(0 , simulation.grid_size -1)
            y = random.randint(0 , simulation.grid_size -1)

            if self.population[x][y].is_infected == False:

                self.population[x][y].is_infected = True
                self.population[x][y].infected_days = 1

                infections +=1
            


    def spread_infection(self ,  simulation):

        for i in range(simulation.grid_size):
            for j in range(simulation.grid_size):
                if not self.population[i][j].is_dead:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                            
                        elif j == simulation.grid_size -1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)


                    if i == simulation.grid_size -1:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                            
                            elif j == simulation.grid_size -1:
                                if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)

                            else:
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)
                        
                    else:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                            
                        elif j == simulation.grid_size -1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)

                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
  



    def update(self , simulation):

        simulation.days +=1

        for row in self.population:
            for person in row:
                person.update(sim)


    def display_statistace(self , simulation):

        total_infected_count = 0
        total_death_count = 0

        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected_count +=1
                    if person.is_dead:
                        total_death_count +=1

        infected_percent = round(100*(total_infected_count/simulation.pop_size))
        deths_percent = round(100*(total_death_count/simulation.pop_size))


        print("\n---------Day #" + str(simulation.days) + "-----------")
        print("\nPopulation size : " + str(simulation.pop_size))
        print("\nInfected people : " +  str(total_infected_count) + "/" + str(simulation.pop_size))
        print("\nDeaths people : " +  str(total_death_count) + "/" + str(simulation.pop_size))
        print("\nInfection percent : " + str(infected_percent) + " / %100")
        print("\ndeaths percent : " + str(deths_percent) + " / %100")

        
def graphics(simulation , population , canvas):

    squar_dimension = 600//simulation.grid_size

    for i in range(simulation.grid_size):
        y = i*squar_dimension


        for j in range(simulation.grid_size):
            x = j*squar_dimension

            if population.population[i][j].is_dead:
                canvas.create_rectangle(x , y , x+squar_dimension , y+squar_dimension , fill="red")

            else:
                if population.population[i][j].is_infected:
                    canvas.create_rectangle(x , y , x+squar_dimension , y+squar_dimension , fill="yellow")
                else:
                    canvas.create_rectangle(x , y , x+squar_dimension , y+squar_dimension , fill="green")
        

sim = Simulation()

window_width = 600
window_height = 600

sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canves = tkinter.Canvas(sim_window , width=window_width , height=window_height , bg='lightblue')
sim_canves.pack(side=tkinter.LEFT)

pop = Population(sim)


pop.initial_infection(sim)
pop.display_statistace(sim)

input("Press enter to begin simulation.")
for i in range(1 , sim.sim_days):

    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistace(sim)
    graphics(sim , pop , sim_canves)


    sim_window.update()
    if i != sim.sim_days-1:
        sim_canves.delete("all")
    
