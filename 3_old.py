n = int(input())
diegos_stickers = sorted(int(number) for number in input().split())
lenth = len(diegos_stickers)

k = int(input())
# coll_numbers = [int(number) for number in input().split()]
coll_numbers = input().split()

for at_least_number in coll_numbers:
    at_least_number = int(at_least_number) ###
    left_index = 0
    right_index = lenth - 1
    if at_least_number > diegos_stickers[right_index]:
        result = len(set(diegos_stickers))
        print(result)
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

        while diegos_stickers[left_index] == diegos_stickers[right_index] and left_index != right_index:
            if left_index != 0:
                left_index -= 1
                right_index -= 1
            else:
                right_index -= 1
                break
        
        result = len(set(diegos_stickers[:right_index]))
        # print(right_index)
        print(result)