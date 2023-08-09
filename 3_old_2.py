file = open("input.txt", "r")

n = int(file.readline())

diegos_stickers = set()
for _ in range(n):
    number = ""
    symbol = ""
    while symbol not in (" ", "\n"):
        symbol = file.read(1)
        number += symbol
    diegos_stickers.add(int(number))
diegos_stickers = sorted(diegos_stickers)

k = int(file.readline())

lenth = len(diegos_stickers)
for _ in range(k):

    at_least_number = ""
    symbol = ""
    while symbol not in (" ", "\n"):
        symbol = file.read(1)
        at_least_number += symbol
    at_least_number = int(at_least_number)

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