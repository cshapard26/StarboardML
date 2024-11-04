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
        
        
        # TODO: add splits and mistrokes and weight by n-gram frequency
        splits = 1
        mistrokeability = 1

        homerow_score = 0
        homerow_index = math.ceil(member.rows / 2)
        ngramdata = NGramData()
        for col in member.direct_keys:
            homerow_score += 1 #ngramdata.ngram_rankings[col[homerow_index]]

        unused_chords = 0
        for chords in member.key_dict.values():
            if len(chords) == 0:
                unused_chords += 1

        # TODO: Add movement test
        finger_movement = 1000
        
        
        member.score = (
            (math.floor(4 * math.exp(-1 * unused_chords) + 1) * (
                (2 * overlaps + 1) *
                (finger_movement + 30 * splits) + 
                (100 * duplicates)
            ) // (
                homerow_score + 
                (n_gram_consistency ** 2) + 
                1
            ) + mistrokeability ) **
            columns
        )
    
    return population


if __name__ == "__main__":
    from classes.kb import NGramData
else:
    from src.classes.kb import NGramData