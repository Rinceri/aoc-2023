import re

FILENAME = "day3.txt"

with open(FILENAME) as f:
    temp = f.read().splitlines()

# to make sure proper index checking when finding symbols
lines = [f".{line}." for line in temp]
max_index = len(lines) - 1
global_stars1 = [("","")]
global_stars2 = [("","")]


def all_stars(prevline: str|None, line: str, line_idx: int, nextline: str|None) -> None:
    
    # finding all numbers, and their start/stop indices
    nums = re.finditer(r'\d+', line)
        
    # finding symbols adjacent to the numbers spotted
    for x in nums:
        # check for adjacent cells in the same line [.123.]
        num = int(x.group())
        start = x.span()[0] - 1
        stop = x.span()[1] + 1

        # find all * parts on the same line
        curr = line[start: stop]
        for star in re.finditer(r'\*', curr):
            # append them to global stars if no repeats
            append_global(star, start, line_idx, num)
            
        # find all * parts above
        if prevline is not None:
            curr = prevline[start: stop]
            for star in re.finditer(r'\*', curr):
                append_global(star, start, line_idx - 1, num)

        # find all * parts on below line
        if nextline is not None:
            curr = nextline[start: stop]
            for star in re.finditer(r'\*', curr):
                append_global(star, start, line_idx + 1, num)
        
        
def append_global(star: re.Match, start: int, line_idx: int, num: int) -> None:
    # [(x,y), #num]
    loc = (star.start() + start, line_idx)
    if loc not in [x for x,y in global_stars1]:
        global_stars1.append([loc, num])
        
    elif loc not in [x for x,y in global_stars2]:
        global_stars2.append([loc, num])

def double_total():
    # [(x,y), #num]
    total = 0

    for x,y in global_stars1[1:]:
        for m,n in global_stars2[1:]:
            if x == m:
                total += y * n

    print(total)

for i, line in enumerate(lines):
    prevline = lines[i-1] if i > 0 else None
    nextline = lines[i+1] if i < max_index else None
    
    all_stars(prevline, line, i, nextline)
    
double_total()