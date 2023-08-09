n = int(input())
k = int(input())
petya_row = int(input())
if input() == "1":
    petya_number = 2*petya_row - 1
else:
    petya_number = 2*petya_row
    
if petya_number <= k:
    petya_variant = petya_number
else:
    petya_variant = petya_number % k
    if petya_variant == 0:
        petya_variant = k

best_up_number = 2e9
best_down_number = -2e9
if petya_number + k <= n:
    best_up_number = petya_number + k
if petya_number - k >= 1:
    best_down_number = petya_number - k

if best_up_number % 2 != 0:     vasya_up_row = best_up_number // 2 + 1
else:                           vasya_up_row = best_up_number // 2

if best_down_number % 2 != 0:   vasya_down_row = best_down_number // 2 + 1
else:                           vasya_down_row = best_down_number // 2

if (vasya_up_row - petya_row) <= (petya_row - vasya_down_row):
    best_number = best_up_number
else:
    best_number = best_down_number

if best_number % 2 == 1:
    vasya_row = best_number // 2 + 1
    vasya_side = 1
else: 
    vasya_row = best_number // 2
    vasya_side = 2

if best_up_number == 2e9 and best_down_number == -2e9:
    print(-1)
else:
    print(vasya_row, vasya_side)