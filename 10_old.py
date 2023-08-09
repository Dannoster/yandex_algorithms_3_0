with open("input.txt", "r") as file:
    char = " "
    chars_counter_dict = dict()
    while char:
        char = file.read(1)
        # print(char)
        if char not in ("\n", " ", ""):
            if char not in chars_counter_dict:
                chars_counter_dict[char] = 1
            else:
                chars_counter_dict[char] += 1
print(chars_counter_dict)
ordered_chars = sorted(chars_counter_dict)
print(ordered_chars)
for char in ordered_chars:
    print(f"{char}: {chars_counter_dict[char]}")