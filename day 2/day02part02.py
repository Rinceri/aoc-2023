import re

arr = open("day2.txt").readlines()

def get_power(line: str) -> int:
    
    nums = re.findall(r'\d+ [rgb]', line)
    max_red, max_green, max_blue = 0, 0, 0
    # example: ["2 r", "4 g", "6 b", ...]

    for x in nums:
        i, t = x.split()
        i = int(i)

        if t == 'r' and i > max_red:
            max_red = i            
        elif t == 'g' and i > max_green:
            max_green = i
        elif t == 'b' and i > max_blue:
            max_blue = i

    return max_red * max_green * max_blue

print(sum(map(get_power, arr)))