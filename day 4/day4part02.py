import re

FILENAME = "day4.txt"

lines = open(FILENAME).readlines()

def get_commons(line: str) -> int:
    # finding all str(int) of numbers in the two rows
    all_nums, my_nums = \
        [re.findall(r'\d+', x) for x in line.split(':')[1].split('|', 1)]

    # number of commons in both lists
    return len(set(all_nums).intersection(my_nums))


all_points = list(map(get_commons, lines))
max_cardno = len(all_points)

# number of new cards from a card
def get_cardnos(card_no: int, commons: int):
    # base case
    if commons == 0:
        return commons
    
    # recursive
    start = card_no + 1
    stop = card_no + commons + 1
    total = commons

    for x in range(start, stop):
        total += get_cardnos(x, all_points[x - 1])
    
    return total

# total number of new cards
new_cards = sum(map(get_cardnos, range(1, max_cardno + 1), all_points))

# current amount of cards plus total new cards
print(new_cards + max_cardno, "cards")