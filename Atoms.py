import numpy as np
import random 

class Atoms():
    def __init__(self, atoms, lamda):
        self.atoms = atoms
        self.lamda = lamda 

    

    def decay(self):
        """simulates decay of the atoms"""
        count = 0 
        while count < len(self.atoms)/2: #loop until count is half of the total
            for i in range(len(self.atoms)): #loop for all atoms 
                if self.atoms[i] != 0: #if atom hasnt already decayed
                    if random.random() < self.lamda: #decide if it should decay
                        self.atoms[i] = 0 # update to decayed state
                        count += 1 #update how many have decayed
                    else:
                       pass 
                else:
                    pass

        return self.atoms
         


if __name__ == "__main__":
    
    array = Atoms(np.ones((5,5), dtype=int))
    lamda = 0.2

    a1 = array.decay(lamda)

    print(a1)


