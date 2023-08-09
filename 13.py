pieces = input().strip().split()
stack = []
for piece in pieces:
    if piece.isdigit():
        stack.append(int(piece))
    elif piece == "+":
        first = stack.pop()
        second = stack.pop()
        stack.append(first + second)
    elif piece == "-":
        first = stack.pop()
        second = stack.pop()
        stack.append(second - first)
    elif piece == "*":
        first = stack.pop()
        second = stack.pop()
        stack.append(first * second)
print(*stack)