import math
import random

def rank_population(evaluated_population):
    return sorted(evaluated_population, key=lambda member: member.score)

def kill_unfit(ranked_population, kill_coefficent):
    return ranked_population[:math.floor(len(ranked_population) * (1 - kill_coefficent))]

def pair_parents(thinned_population, total_population_count):
    if total_population_count < 3:
        raise Error("Total population must be at least 3.")
    if len(thinned_population) < 2:
        raise Error("Thinned population less than 2. Cannot pair.")

    pairs = []
    pairs.append((thinned_population[0], thinned_population[1]))

    while len(pairs) < total_population_count:
        rand_parent_1 = random.selection(thinned_population)
        rand_parent_2 = random.selection(thinned_population)
        if rand_parent_1 == rand_parent_2:
            continue
        pairs.append((rand_parent_1, rand_parent_2))
    
    return pairs