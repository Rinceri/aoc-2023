FILENAME = "day1.txt"

f = open(FILENAME, "r")
arr = f.readlines()
f.close()

temp_array = []
sum = 0

for x in arr:
    temp_array = []
    for i in x:
        if i.isnumeric():
            temp_array.append(i)
        
    sum += int(temp_array[0] + temp_array[-1])

print(sum)