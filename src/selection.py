import math

def rank_population(evaluated_population):
    return sorted(evaluated_population, key=lambda member: member.score)

def kill_unfit(ranked_population, kill_coefficent):
    return ranked_population[:math.floor(len(ranked_population) * (1 - kill_coefficent))]

def pair_parents(thinned_population):
    pass #pair up best parents varied according to some parameters