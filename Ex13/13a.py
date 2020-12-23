

def doubles(list):
    originals = set()
    indices = []

    for i, v in enumerate(list):
        if v in originals:
            indices.append(i)
        else:
            originals.add(v)

    return indices


l = ['jan', 'piet', 'henk', 'els', 'piet',
     'els', 'john', 'els', 'jan', 'els', 'henk']
print(doubles(l))
