import pandas
import numpy
import matplotlib
from src.population import *
from src.fitness import *


def main():
    population = initialize_population(100)
    evaluate_population(population)

if __name__ == "__main__":
    main()
