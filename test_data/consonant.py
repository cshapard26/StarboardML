import re

def detach_front(word):
    vowels = "aeiouy\n"

    for index, letter in enumerate(word):
        if letter in vowels:
            return word[:index]
    return word

def detach_back(word):
    vowels = "aeiouy\n"

    backword = word[::-1]
    for index, letter in enumerate(backword):
        if letter in vowels:
            return word[len(word) - index:]
    return ""

def cluster_consonants(text, section = 0) -> list: # Text is the name of the file and Section is the sliver of the word to grab (0 = "gr"asping, -1 = graspi"ng")
   try:
        with open(text, 'r') as data:
            cluster_count = dict()
            aplhatext = re.sub(r'[^a-zA-Z\s]', '', data.read().lower())
            word_list = aplhatext.split(' ')
            clusters = []
            if section == 0:
                clusters = [detach_front(word) for word in word_list]
            elif section == -1:
                clusters = [detach_back(word) for word in word_list]
            else:
                raise ValueError(f'No "section" of type {section}')

            for cluster in clusters:
                if cluster == '':
                    continue
                elif cluster in cluster_count:
                    cluster_count[cluster] += 1
                else:
                    cluster_count[cluster] = 1
            return sorted(cluster_count.items(), key=lambda item: item[1])

    except:
        print(f'Error reading test file "{text}"')



if __name__ == "__main__":
    testing_data = "test_data/alice_in_wonderland.txt"
    print(cluster_consonants(testing_data, -1))  