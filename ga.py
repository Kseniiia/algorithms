# -*- coding: utf-8 -*-

import random
population=[]        # популяция
population_size=10   # размер популяции 
chromosomes_length=3 # число генов (количество переменных в уравнении)
tournament_size=3    # число особей для турнирной селекции
crossover_rate=0.8   # процент особей для скрещивания
mutation_rate=0.5    # процент особей для мутации

# Начальная популяция (генерируется случайным образом)
for i in range(population_size):
    population.append([random.randint(0,30) for i in range(chromosomes_length)])

# Функция приспособленности (fitness function)
def evaluation(population):
    fitness=[]
    f_objective=[]
    for individual in population:
        # кубическое уравнение
        f_objective.append((individual[0]**3)+(individual[1]**3)+(3*individual[0]**2*individual[1])+(3*individual[0]*individual[2]**2)-27)

    for health in f_objective:
        fitness.append(1.0/(1+health))

    return fitness

# Проверка, найдено ли решение
def check(fitness,population,iteration):
    for health in fitness:
        if health==1:
            print("The solution is found after %d generations:"%(i))
            print(population[fitness.index(1)])
            return 1
        else: 
            return 0

# Турнирная селекция
def tournament(probablity,population):
    gen=[]
    parents=[]
    for j in range(population_size):
        team=[]
        for i in range(tournament_size):
            x=random.randint(0,population_size-1)
            team.append(probablity[x])
        gen.append(max(team))
        del team
    for parent in gen:
        parents.append(population[probablity.index(parent)])
    return parents

# Функция селекции
def selection(fitness):
    probablity=[]
    total_fitness=sum(fitness)
    for fit in fitness:
        probablity.append(fit/total_fitness)
    parents=tournament(probablity,population)  
    return parents

# Функция скрещивания 
def crossover(parents):
    i=0
    cross_number=int(crossover_rate*population_size)    
    for i in range(cross_number):
        cross_location=random.randint(0,chromosomes_length-1)
        father=random.randint(0,len(parents)-1)
        mother=random.randint(0,len(parents)-1)
        if mother != father:
            geneF=parents[father][cross_location]
            geneM=parents[mother][cross_location]
            parents[father][cross_location]=geneM
            parents[mother][cross_location]=geneF    
    return parents

# Функция мутации
def mutation(parents):
    for i in range(int(population_size*mutation_rate)):
        mutant=random.randint(0,len(parents)-1)
        mutant_gene=random.randint(0,chromosomes_length-1)
        parents[mutant][mutant_gene]=random.randint(0,30)
        return parents

# Алгоритма
for i in range(5000):  
    fitness=evaluation(population)     # оценка приспособдленности
    parents=selection(fitness)         # селекция
    parents=crossover(parents)         # скрещивание
    parents=mutation(parents)          # мутация
    population[:]=parents[:]           # формирование новой популяции
    if check(fitness,population,i)==1: # проверка результата
        break