from src.population import *
from src.fitness import *
from src.selection import *


def main():
    population = initialize_population(100)
    population1 = evaluate_population(population)
    population2 = rank_population(population1)
    population3 = kill_unfit(population2, 0.75)
    for i in population3:
        print(i.score)

if __name__ == "__main__":
    main()
