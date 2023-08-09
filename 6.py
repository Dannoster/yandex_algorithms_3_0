m = int(input())
n = int(input())

sectors = []    
for _ in range(n):
    left, right = ( int(pair) for pair in input().split() )
    new_sector = {"left" : left, "right" : right}
    number_of_sectors = len(sectors)
    for i, old_sector in enumerate(reversed(sectors)):
        if new_sector["left"] > old_sector["right"] or new_sector["right"] < old_sector["left"]:
            pass
        else:
            del sectors[number_of_sectors - 1 - i]
    sectors.append(new_sector)

print(len(sectors))






#
    # sector_pairs.append(input().split())


# sector_pairs.sort(key=lambda item: item[1]) # сортировка по правой границе

# max_right = sector_pairs[0][1]
# del sector_pairs[0]
# counter = 1
# for pair in sector_pairs:
#     if pair[0] >


