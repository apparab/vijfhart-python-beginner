import os
dir_path = os.path.dirname(os.path.realpath(__file__))

fname = 'weer.txt'
f = open(f'{dir_path}/{fname}', 'rt')

cities = {line.split()[0]: int(line.split()[1])
          for line in f if not line.startswith('#')}

avg = sum(cities.values()) / len(cities.values())

print(avg)

lower = []
higher = []

for name, temp in cities.items():
    if temp < avg:
        lower.append((name, temp))
    else:
        higher.append((name, temp))

print('lower than average:')
print(lower)
print('higher than average:')
print(higher)
