import numpy as np
import random 


class Atoms():
    def __init__(self, atoms, probability, step):
        "initialise the array, lamda, and the time step"
        self.atoms = atoms
        self.probability = probability 
        self.step = step

    def __str__(self):
        "print function"
        n = int(np.sqrt(len(self.atoms))) #define the ength of each side 
        grid = self.atoms.reshape(n, n) #creates an NxN grid of atoms 
        output = ""
        for row in grid: 
            for point in row:
                output += f"{point} " # prints each atom in the list row by row
            output += "\n"

        output += (
            f"\ninitial number of undecayed atoms = {len(self.atoms)}"
            f"\nfinal number of undecayed atoms = {len(self.atoms)- self.decayed}"
            f"\nsimulated half life =  {round(self.time, 2)} minutes" 
            f"\npredicted half life = {round((np.log(2)/ (self.probability/self.step)), 2)} minutes"
        )     
        return output

    

    def decay(self):
        """simulates decay of the atoms"""
        self.decayed = 0 
        self.time = 0


        while self.decayed < len(self.atoms)//2: #loop until count is half of the total
            self.time += self.step #add 1 to step 
            for i in range(len(self.atoms)): 
                if self.atoms[i] != 0: #if atom hasnt already decayed
                    if random.random() < self.probability: #decide if it should decay
                        self.atoms[i] = 0 # update to decayed state
                        self.decayed += 1 
                       
                    else:
                       pass 
                else:
                    pass

    
def main():

    length = int(input("enter length of side (N)"))
    lamda_per_min = float(input("enter value of lamda per min"))
    step = float(input("enter value of timestep"))
    #lamda_per_min = 0.02775
    #step = 0.01
    #length = 50
    lamdaSimulation = lamda_per_min * step #calculates lamda for timestep
    n_of_atoms = length**2 #NxN length of array 

    array = Atoms(np.ones(n_of_atoms, dtype=int),  lamdaSimulation, step) # initialises the atomsas an array of all ones 
    array.decay()
    print(array)



if __name__ == "__main__":
    main()
    



