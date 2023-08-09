input()
diegos_stickers = sorted(set(int(item) for item in input().split()))
input()
coll_numbers = [int(item) for item in input().split()]

lenth = len(diegos_stickers)
for at_least_number in coll_numbers:

    left_index = 0
    right_index = lenth - 1

    if at_least_number > diegos_stickers[right_index]:
        print(lenth)
    elif at_least_number <= diegos_stickers[left_index]:
        print(0)
    elif at_least_number in diegos_stickers:
        index = diegos_stickers.index(at_least_number)
        print(index)
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