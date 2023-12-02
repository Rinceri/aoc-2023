import re

arr = open("day2.txt").readlines()
# 12 r, 13 g, 14 b

def get_num(line: str) -> int:
    """
    Takes a line and returns 0 or game number if game possible
    """
    nums = re.findall(r'Game \d+|\d+ [rgb]', line)
    # example: ["Game 27", "2 r", "4 g", "6 b", ...]    
    curr = True

    for x in nums[1::]:
        i, t = x.split()
        i = int(i)

        if (t == 'r' and i > 12)\
            or (t == 'g' and i > 13)\
            or (t == 'b' and i > 14):
            curr = False
        
        if not curr:
            return 0
        
    return int(re.search(r'\d+', nums[0]).group())


print(sum(map(get_num, arr)))