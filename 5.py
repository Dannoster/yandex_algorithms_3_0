n = int(input())
numbers_of_letters = []
for _ in range(n):
    numbers_of_letters.append(int(input()))

good_count = 0

minimum = min(numbers_of_letters)
if minimum != 0:
    good_count += minimum * (n - 1)
    numbers_of_letters = [item - minimum for item in numbers_of_letters]

while sum(numbers_of_letters):

    drop_zeros = [num for num in numbers_of_letters]
    while min(drop_zeros) == 0:
        drop_zeros.remove(0)
    start_len = len(drop_zeros)

    prev_number_exist = False
    cur_good_count = 0
    for i, number in enumerate(numbers_of_letters):
        if number and prev_number_exist:
            cur_good_count += 1
            numbers_of_letters[i] -= 1
        elif number and not prev_number_exist:
            numbers_of_letters[i] -= 1
            prev_number_exist = True
        elif not number:
            prev_number_exist = False

    if sum(numbers_of_letters) != 0:
        drop_zeros = [num for num in numbers_of_letters]
        while min(drop_zeros) == 0:
            drop_zeros.remove(0)
        minimum = min(drop_zeros)
        if len(drop_zeros) == start_len:
            good_count += cur_good_count * (minimum + 1)
            numbers_of_letters = [item - minimum for item in numbers_of_letters if item != 0]
        else:
            good_count += cur_good_count
    else:
        good_count += cur_good_count

print(good_count)