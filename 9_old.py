n, m, k = (int(item) for item in input().strip().split())

matrix = []
for _ in range(n):
    numbers_in_string = [int(item) for item in input().strip().split()]
    matrix.append(numbers_in_string)

for _ in range(k):
    sum = 0
    x1, y1, x2, y2 = (int(item) for item in input().strip().split())
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += matrix[i - 1][j - 1]
    print(sum)