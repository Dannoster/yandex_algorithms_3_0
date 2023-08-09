count_of = dict()
maximun_value = 1
with open("input.txt") as file:
    for line in file:
        line = line.strip().replace(" ", "")
        if not line:
            continue
        for char in line:
            if char in count_of:
                count_of[char] += 1
                if count_of[char] > maximun_value:
                    maximun_value = count_of[char]
            else:
                count_of[char] = 1
chars_list = sorted(count_of)
for i in range(maximun_value):
    y_axis = maximun_value - i
    for char in chars_list:
        if count_of[char] >= y_axis:
            print("#", sep="", end="")
        else:
            print(" ", sep="", end="")
    print()
print(*chars_list, sep="")