import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

fname = 'verhaal.txt'
f = open(f'{dir_path}/{fname}', 'rt')

counts = {}

for index, lines in enumerate(f):
    for word in lines.rstrip().split():
        stripped_word = word.lower().strip().translate(
            str.maketrans('', '', string.punctuation))
        if not stripped_word in counts:
            counts[stripped_word] = {'total': 0, 'lines': []}
        counts[stripped_word]['total'] += 1
        counts[stripped_word]['lines'].append(index + 1)

for word, ob in counts.items():
    print('{}: {} ({})'.format(word, ob['lines'], ob['total']))
