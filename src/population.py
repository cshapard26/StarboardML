from classes.kb import *
import random
import itertools



key_dataset = ["B", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y", "Z",
               "BL", "BR", "DR", "FL", "FR", "GL", "GR", "KH", "KL/CL", "KR", "PL", "PR", "SH", "SK", "SF", "SL", "SM", "SN", "SP", "SQ", "ST", "SW", "TH", "TR", "TW",
               "SHR", "STR", "SPL", "SKR", "SPR", "SKH", "THR"]

empty_key_coefficient = 0.5


def initialize_population(size, seed=None):
    # Initalize
    if seed is not None:
        random.seed(seed)

    raw_population = []

    # Generate members
    for i in range(size):
        initial_dataset = key_dataset.copy()
        id = random.randint(10000000, 99999999)
        columns = random.randint(1, 4)
        rows = random.randint(1, 4)

        # Generate each kb matrix
        keyboard_matrix = []
        for column in range(columns):
            row_list = []
            for row in range(rows):
                if random.random() < empty_key_coefficient:
                    random_key = random.choice(initial_dataset)
                    row_list.append(random_key)
                    initial_dataset.remove(random_key)
                else:
                    row_list.append("")
            keyboard_matrix.append(row_list)

        # Generate possible combos
        col_sets = [] # list of list of sets
        for col in keyboard_matrix:
            col_set_list = []
            for i in col:
                if i != "":
                    col_set_list.append(set([i]))
            for i in range(len(col) - 1):
                if col[i] != "" and col[i + 1] != "":
                    col_set_list.append(set([col[i], col[i + 1]]))
            
            if col_set_list == []:
                columns -= 1
            else:
                col_sets.append(col_set_list)
        
        if len(col_sets) == 0:
            continue
        
        # col_sets now contains a list of lists of the sets of items in each column, with pairs
        key_combo_list = [set.union(*tup) for tup in list(itertools.product(*col_sets))]

        # Pair unused keyboard keys to random combos in the list
        combo_key_dict = dict()
        for combo in key_combo_list:
            combo_key_dict[frozenset(combo)] = []
        
        for key in initial_dataset:
            random_combo = random.choice(list(combo_key_dict.keys()))
            combo_key_dict[random_combo].append(key)

        # Add layout to current population
        raw_population.append(KB(id, 1, keyboard_matrix, combo_key_dict))


def update_population(size, parents, offspring):
    pass #combine parents and offspring


if __name__ == "__main__":
    initialize_population(100)