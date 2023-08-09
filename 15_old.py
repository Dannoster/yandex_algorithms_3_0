n = int(input())
prices = [int(price) for price in input().strip().split()]

result = []
for i in range(n):
    result.append(-1)
    for j in range(n - i - 1):
        if prices[i + j + 1] < prices[i]:
            result[i] = i + j + 1
            break

print(*result)