from src import *

def main():
    population = initialize_population(10000)
    population1 = evaluate_population(population)
    population2 = rank_population(population1)
    population3 = kill_unfit(population2, 0.99)
    for i in population3:
        print(i.score)
    print(population3[0].direct_keys)

if __name__ == "__main__":
    main()
