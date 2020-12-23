import os
dir_path = os.path.dirname(os.path.realpath(__file__))

fname = 'verhaal.txt'
f = open(f'{dir_path}/{fname}', 'rt')

lines = [l for l in f]

total = {
    'lines': len(lines),
    'words': 0,
    'chars': 0
}

for line in lines:
    total['words'] += len(line.split())
    total['chars'] += len(line)

print('{} {} {} {}'.format(total['lines'],
                           total['words'], total['chars'], fname))
