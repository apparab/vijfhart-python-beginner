uurwaarden = "673,1499,82,119341,13,996308,53,7"
total = 0
max_index_length = 0
max_value_length = 0

for i, num in enumerate(uurwaarden.split(',')):
    total += int(num)
    max_index_length = max(len(str(i)), max_index_length)
    max_value_length = max(len(num), max_value_length)

mask = 'Uur {{0:>{0}}}: {{1:>{1}}}'.format(
    max_index_length + 1, max_value_length + 1)

for i, num in enumerate(uurwaarden.split(',')):
    print(mask.format(i, num))
    total += int(num)

print('Totaal: {}'.format(total))
