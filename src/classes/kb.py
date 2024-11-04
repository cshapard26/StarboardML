class KB:
    def __init__(self, id, generation, direct_keys, key_dict, columns, rows):
        self.id = id
        self.generation = generation
        self.direct_keys = direct_keys
        self.key_dict = key_dict
        self.columns = columns
        self.rows = rows

        self.score = 0

class NGramData:
    def __init__(self):
        self.ngram_rankings = dict() 
        #{S: 10
        # T: 10
        # P: 9
        # ...    
        # SCH = 0
        #}
        
        
    
