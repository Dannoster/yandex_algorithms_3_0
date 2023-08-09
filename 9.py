file = open("input.txt", "r")
n, m, k = (int(item) for item in file.readline().strip().split()) 

for _ in range(m):
    file.readline()

for _ in range(k):
    with open("input.txt", "r") as file_2:

        sum = 0
        x1, y1, x2, y2 = (int(item) for item in file.readline().strip().split())
        for _ in range(x1):
            file_2.readline()

        for i in range(x1, x2 + 1):
            string = [int(item) for item in file_2.readline().strip().split()]
            for j in range(y1, y2 + 1):
                sum += string[j - 1]

        print(sum)

file.close()