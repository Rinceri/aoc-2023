import re

FILENAME = "day4.txt"

lines = open(FILENAME).readlines()

def get_points(line: str) -> int:
    # finding all str(int) of numbers in the two rows
    all_nums, my_nums = \
        [re.findall(r'\d+', x) for x in line.split(':')[1].split('|', 1)]

    # finding common ones and counting them, then finding score
    return int(2**(len(set(all_nums).intersection(my_nums)) - 1))

print(sum(map(get_points, lines)))