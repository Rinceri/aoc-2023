
def iterate_right(line: str) -> str:
    temp_str = ""
    for x in line:
        temp_str += x
        if x.isnumeric():
            return x

        for num in number_names.keys():
            if num in temp_str:
                return number_names[num]

def iterate_left(line: str) -> str:
    temp_str = ""
    for x in line[::-1]:
        temp_str += x
        if x.isnumeric():
            return x
        
        for num in number_names.keys():
            if num in temp_str[::-1]:
                return number_names[num]


f = open("day 1/day1.txt", "r")
arr = f.readlines()
f.close()

number_names = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
sum = 0

for line in arr:
    sum += int(iterate_right(line) + iterate_left(line))

print(sum)
