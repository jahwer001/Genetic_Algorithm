import numpy
#implemetation de l'alghorithme genetique
y=44.1
#Fitness assignment(calcull de la fonction fitenss)
def cal_pop_fitness(dataset,population):
    y_pred = numpy.sum(population*dataset,axis=1)
    fitness = 1/numpy.abs(y_pred-y)
    return fitness

