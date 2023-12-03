import re

FILENAME = "day3.txt"

with open(FILENAME) as f:
    temp = f.read().splitlines()

# to make sure proper index checking when finding symbols
lines = [f".{line}." for line in temp]
max_index = len(lines) - 1

def check_upper(prevline: str|None, curr_x: re.Match) -> bool:
    if prevline is None:
        return False

    start = curr_x.span()[0] - 1
    stop = curr_x.span()[1] + 1
    line = prevline[start: stop]
    if re.search("[^.|0-9]", line) is None:
        return False
    return True

def check_lower(nextline: str|None, curr_x: re.Match) -> bool:
    if nextline is None:
        return False

    start = curr_x.span()[0] - 1
    stop = curr_x.span()[1] + 1
    line = nextline[start: stop]
    if re.search("[^.|0-9]", line) is None:
        return False
    return True


def line_total(prevline: str|None, line: str, nextline: str|None) -> int:
    total = 0
    
    # finding all numbers, and their start/stop indices
    nums = re.finditer(r'\d+', line)
        
    # finding symbols adjacent to the numbers spotted
    for x in nums:
        # check for adjacent cells in the same line [.123.]
        num = x.group()
        start = x.span()[0] - 1
        stop = x.span()[1] + 1

        curr = line[start: stop]
        if re.search("[^.|0-9]", curr) is None:
            if not check_upper(prevline, x):
                if not check_lower(nextline, x):
                    continue

        # group() str -> int
        total += int(num)

    return total

total = 0
for i, line in enumerate(lines):
    prevline = lines[i-1] if i > 0 else None
    nextline = lines[i+1] if i < max_index else None
    total += line_total(prevline, line, nextline)
    
print(total)