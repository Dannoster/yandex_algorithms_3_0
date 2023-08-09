string = input().strip()

chars_counter_dict = dict()
for left_it in range(len(string)):
    left_index = left_it
    for right_it in range(len(string)):
        right_index = len(string) - right_it
        for char in string[left_index : right_index]:
            if char not in chars_counter_dict:
                chars_counter_dict[char] = 1
            else:
                chars_counter_dict[char] += 1

ordered_chars = sorted(chars_counter_dict)
for char in ordered_chars:
    print(f"{char}: {chars_counter_dict[char]}")