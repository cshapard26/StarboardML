import classes.KB
import random
import itertools



key_dataset = ["B", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y", "Z",
               "BL", "BR", "DR", "FL", "FR", "GL", "GR", "KH", "KL/CL", "KR", "PL", "PR", "SH", "SK", "SF", "SL", "SM", "SN", "SP", "SQ", "ST", "SW", "TH", "TR", "TW",
               "SHR", "STR", "SPL", "SKR", "SPR", "SKH", "THR"]

empty_key_coefficient = 0.5

def generate_combinations(*lists):
    # Generate the Cartesian product of the input lists
    product = itertools.product(*lists)
    
    return list(product)


def initialize_population(size, seed=None):
    # Initalize
    if seed is not None:
        random.seed(seed)

    initial_dataset = key_dataset
    raw_population = []

    # Generate members
    for i in size:
        id = random.randint(10000000, 99999999)
        columns = random.randint(1, 4)
        rows = random.randint(1, 4)

        # Generate each kb matrix
        keyboard_matrix = []
        for column in columns:
            row_list = []
            for row in rows:
                if random.random() < empty_key_coefficient:
                    random_key = random.choice(initial_dataset)
                    row_list.append(random_key)
                    initial_dataset.remove(random_key)
                else:
                    row_list.append("")
            keyboard_matrix.append(row_list)

        # Generate possible combos
        key_combo_sets = [] # list of list of sets
        for col in keyboard_matrix:
            col_set_list = []
            for i in col:
                if i is not "":
                    col_set_list.append(set(i))
            for i in range(len(col) - 1):
                if col[i] is not "" and col[i + 1] is not "":
                    col_set_list.append(set([col[i], col[i + 1]]))
            key_combo_sets.append(col_set_list)
        
        # Key combo sets now contains a list of lists of the sets of items in each column, with doubles


        member = KB(id, 1, keyboard_matrix)



def update_population(size, parents, offspring):
    pass #combine parents and offspring