# quiz5.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Quiz 5 Dictionaries in action


import re
import math



def get_sentences(line: str) -> list[list[str]]:
    'Returns a list with list of each sentence'
    line = re.sub(r',|-|—|:|;', ' ', line.lower())
    sentences = re.split(r'\.|\?|!', line)
    return [s.split() for s in sentences]


def get_word_vectors(sentences: list[list[str]]) -> dict[str, dict[str]]:
    '''
    Returns a count of every other word that appears in the same sentence
    '''
    flat_list = [word for sentence in sentences for word in sentence]
    word_set = set(flat_list)

    word_vecs = {}

    for key in word_set:
        word_vecs[key] = {}
        for sentence in sentences:
            if key in sentence:
                for word in sentence:
                    if key != word:
                        word_vecs[key][word] = word_vecs[key].get(word, 0) + 1

    return word_vecs



def cosine_similarity(v1: dict[str, int], v2: dict[str, int]) -> float:
    '''
    Gets the cosine similarity between two words, Credit: Marie Tsaasan
    '''

    numerator_words = set(v1.keys()).intersection(set(v2.keys()))

    numerator = 0.0
    for word in numerator_words:
        numerator += v1[word] * v2[word]

    denominator = math.sqrt(magnitude(list(v1.values())) * magnitude(list(v2.values())))

    return numerator/denominator



def magnitude(values: list[int]) -> int:
    'Gets the magnitude of a set of integers'
    sum = 0
    for x in values:
        sum += x**2
    return sum



def main() -> None:
    'Runs the Cosine Similarity Calculator program'
    print('Welcome to the Cosine Similarity Calculator by Van Nguyen.\n')

    while True:
        try:
            passage = input('Please input a passage of text:\n')

            if len(passage.split()) < 3:
                raise ValueError
            break
        except ValueError:
            print('Input must be at least 3 words long.\n')

    word_vecs = get_word_vectors(get_sentences(passage))

    while True:
        try:
            words = input('\nPlease input three words separated by a space: ').split()

            for word in words:
                if not word in passage:
                    raise ValueError('Words must be in the given passage.')
            
            if len(words) != 3:
                raise ValueError('Input must be exactly three words.')

            break
        except ValueError as e:
            print(e)
    
    
    print(f'\nCosine similarity between "{words[0]}" and "{words[1]}": '
        f'{cosine_similarity(word_vecs[words[0]], word_vecs[words[1]])}')

    print(f'Cosine similarity between "{words[1]}" and "{words[2]}": '
        f'{cosine_similarity(word_vecs[words[1]], word_vecs[words[2]])}')



def testing() -> None:
    'Tests the Cosine Similarity Calculator program'

    passage = (
        'I am a sick man. I am a spiteful man. I am an unattractive man. ' 
        'I believe my liver is diseased. However, I know nothing at all '
        'about my disease, and do not know for certain what ails me.')
    word_vecs = get_word_vectors(get_sentences(passage))

    assert cosine_similarity(word_vecs['man'], word_vecs['liver']) == 0.2631174057921088



if __name__ == '__main__':
    testing()
    main()
    
