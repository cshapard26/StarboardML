import math

def evaluate_population(population):
    for member in population:
        columns = member.columns
        rows = member.rows

        overlaps = 0
        for chords in member.key_dict.values():
            if len(chords) >= 2:
                overlaps += len(chords) - 1
        
        duplicates = 0
        seen_keys = set()
        for chords in member.key_dict.values():
            for chord in chords:
                if chord in seen_keys:
                    duplicates += 1
                else:
                    seen_keys.add(chord)
        
        n_gram_consistency = 0
        for combo, chords in member.key_dict.items():
            for chord in chords:
                for key in combo:
                    if chord in key:
                        n_gram_consistency += 1
                        break
        print(n_gram_consistency)
        
        
        
        '''member.score = (
            4 * math.exp()


        )'''