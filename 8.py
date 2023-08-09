k = int(input())

class dot:
    def __init__(self, pair):
        self.x = int(pair[0])
        self.y = int(pair[1])
    
    def __str__(self):
        return f"{self.x} {self.y}"

dots = []
for _ in range(k):
    pair = input().strip().split()
    new_dot = dot(pair)
    dots.append(new_dot)

dots.sort(key=lambda dot_: dot_.y)
dots.sort(key=lambda dot_: dot_.x)

min_x = min(dots, key=lambda dot_: dot_.x).x
min_y = min(dots, key=lambda dot_: dot_.y).y
max_x = max(dots, key=lambda dot_: dot_.x).x
max_y = max(dots, key=lambda dot_: dot_.y).y
    
print(min_x, min_y, max_x, max_y)