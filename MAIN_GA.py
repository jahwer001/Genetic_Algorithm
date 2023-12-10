import numpy
#import GA_Genetic_algorithm
'y=w1*x1+w2*x2+w3*x3+w4*x4+w5*x5+w6*x6'
# data set
# parame
#les parametre d'un alghorime genetique:
#1. Nombre de solution par population
#2. Taille de la poppuletion
#3. le nombre des parents
#4. Intervalle des valeurs a generer
#5. Nombre des generations
#importation des donnes
Data_inputs=[4,-2,7,5,11,1]
#definir le nombe des poids
num_weights=len(Data_inputs)
#taille de la popullation
solution_per_population=6
#mating pool size
num_parents_mating=3
#definir la taille de la population
Population_size=(solution_per_population,num_weights)
#1. initialisation (la generation aleatoire de la premier population)
new_population = numpy.random.uniform(low=-8.0 , high=8.0 , size = Population_size) 

nombre_des_generation=100


for generation in range (nombre_des_generation):
    print ("C'est la generation:",generation)
    #2. Fitness assignmentt (calcul de la fonction fitness)
    fitness= GA_Genetic_algorithm.cal_pop_fitness (Data_inputs,new_population)
    print ("Fitness",fitness)
    #3. Selection
    
    #parent=GenaticAlgorithm.select.mating_pool()
    #4. Crossover
    #5. Mutation