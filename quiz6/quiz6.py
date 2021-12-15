# quiz6.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Quiz 6... Quiz 5 continued


import re
import math
import sys
import tkinter



def get_sentences(line: str) -> list[list[str]]:
    'Returns a list with list of each sentence'
    line = re.sub(r',|-|—|:|;', ' ', line.lower())
    sentences = re.split(r'\.|\?|!', line)
    return [s.split() for s in sentences]



def get_word_vectors(sentences: list[list[str]], word_set: set[str]) -> dict[str, dict[str]]:
    '''
    Returns a count of every other word that appears in the same sentence
    '''
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
    'Runs the Synonym Question Checker'
    print('Welcome to the Synonym Question Checker by Van Nguyen.\n')

    try:
        with open(sys.argv[1], 'r') as file:
            passage = file.read()
    except:
        print(f'Quiz text file "{sys.argv[1]}" does not exist.')
        sys.exit()


    try:
        if len(passage.split()) < 3:
            raise ValueError
    except ValueError:
        print('Quiz text file must be at least 3 words long.\n')
        sys.exit()


    sentences = get_sentences(passage)
    flat_list = [word for sentence in sentences for word in sentence]
    word_set = set(flat_list)
    word_vecs = get_word_vectors(flat_list, word_set)
    

    try:
        questions = []
        lines = 0

        with open(sys.argv[2], 'r') as file:
            for line in [line.split() for line in file]:
                lines += 1
                if len(line) == 6:
                    word, *answers, correct_ans = line
                    if (len(set(answers)) == 4 and 
                        correct_ans in answers and
                        set(answers).issubset(word_set)):
                        questions.append((word, answers, correct_ans))
    except:
        print(f'Quiz question file "{sys.argv[2]}" does not exist.')
        sys.exit()
        
    
    for question in questions:
        word, answers, correct_ans = question
        print(f'\nTest question word: {word}')
        
        highest = 0
        calc_ans = None
        for answer in answers:
            sim = cosine_similarity(word_vecs[word], word_vecs[answer])
            if sim > highest:
                highest = sim
                calc_ans = answer

        print(f'Computed Answer: {calc_ans} Test Answer: {correct_ans}')

    print(f'\nTotal lines in file: {lines}')
    print(f'Total questions processed: {len(questions)}')
    print(f'Total skipped lines: {lines - len(questions)}')


if __name__ == '__main__':
    main()
    
