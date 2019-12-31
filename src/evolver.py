from arm import Arm
from pie import Pie
from random import random, seed, shuffle, uniform
from rod import Rod
from testlab import TestLab
from time import time
from util import clamp
from vec import Vec

seed(time())

class Dna:
    def __init__(self, rod_count):
        self.rod_count = rod_count
        self.genes = []
        for i in range(self.rod_count):
            self.genes.append(uniform(1, 160))
            self.genes.append(uniform(0, 160))
            self.genes.append(uniform(0, 40))
            self.genes.append(uniform(0, 1))
    
    def mutatedCopy(self):
        copy_genes = []
        for i in range(self.rod_count):
            copy_genes.append(clamp(self.genes[4*i+0] + uniform(-1, 1), 1, 160))
            copy_genes.append(clamp(self.genes[4*i+1] + uniform(-1, 1), 0, 160))
            copy_genes.append(clamp(self.genes[4*i+2] + uniform(-1, 1), 0, 40))
            copy_genes.append(clamp(self.genes[4*i+3] + uniform(-0.0001, 0.0001), 0, 1))
        
        copy = Dna(self.rod_count)
        copy.genes = copy_genes

        return copy

    def crossedWith(self, mate):
        result1_genes, result2_genes = [], []

        for i in range(len(self.genes)):
            if random() > 0.5:
                result1_genes.append(self.genes[i])
                result2_genes.append(mate.genes[i])
            else:
                result1_genes.append(mate.genes[i])
                result2_genes.append(self.genes[i])
        
        result1, result2 = Dna(self.rod_count), Dna(self.rod_count)
        result1.genes = result1_genes
        result2.genes = result2_genes

        return result1, result2
    
    def as_arm(self):
        arm = Arm([])
        for i in range(int(len(self.genes) / 4)):
            arm.rods.append(Rod(
                self.genes[4*i+0],
                self.genes[4*i+1],
                self.genes[4*i+2],
                self.genes[4*i+3]
            ))
        return arm

class Evolver:
    def __init__(self, generations, population_size, lab_params):
        self.generations = generations
        self.population_size = population_size
        self.lab_params = lab_params
    
    def evolve(self):
        population = [Dna(2) for i in range(self.population_size)]

        for g in range(self.generations):
            population.sort(key=lambda x: self.fitness(x), reverse=True)

            daughters = []
            survivors = population[:int(len(population)/2)]

            shuffle(survivors)

            for i in range(int(len(survivors) / 2)):
                mate1 = survivors[2*i+0]
                mate2 = survivors[2*i+1]

                result1, result2 = mate1.crossedWith(mate2)
                daughters.append(result1.mutatedCopy())
                daughters.append(result2.mutatedCopy())
            
            population = survivors + daughters
        
        return max(population, key=lambda x: self.fitness(x)).as_arm()

    def fitness(self, dna):
        lab = TestLab(self.lab_params, dna.as_arm(), Pie())

        while not lab.has_ended():
            lab.update()
                
        return -lab.min_distance
