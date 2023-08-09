string = input().strip()
lenth = len(string)
chars_counter_dict = dict()

for i, char in enumerate(string):
    number_from_left = i + 1
    number_from_right = lenth - i
    min_number = min(number_from_left, number_from_right)

    n = min_number
    a1 = lenth
    an = lenth - 2 * (n - 1)
    Sn = int((a1 + an) * n / 2)

    if char not in chars_counter_dict:
        chars_counter_dict[char] = Sn
    else:
        chars_counter_dict[char] += Sn

ordered_chars = sorted(chars_counter_dict)
for char in ordered_chars:
    print(f"{char}: {chars_counter_dict[char]}")