file = open("input.txt", "r")

file.readline()
diegos_stickers= tuple(sorted(set(int(item) for item in file.readline().split())))
file.readline()
coll_numbers = [int(item) for item in file.readline().split()]

lenth = len(diegos_stickers)
for at_least_number in coll_numbers:

    left_index = 0
    right_index = lenth - 1

    if at_least_number > diegos_stickers[right_index]:
        print(lenth)
    elif at_least_number <= diegos_stickers[left_index]:
        print(0)
    else:
        while not (left_index + 1 == right_index):
            middle_index = int( left_index + (right_index - left_index) / 2 )
            if at_least_number > diegos_stickers[middle_index]:
                left_index = middle_index
            elif at_least_number < diegos_stickers[middle_index]:
                right_index = middle_index
            elif at_least_number == diegos_stickers[middle_index]:
                right_index = middle_index
                break
        print(right_index)

file.close()