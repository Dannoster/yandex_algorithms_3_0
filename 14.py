n = input()
carts = input().strip().split()

stack = []
already_gone = 0
for cart in carts:
    cart = int(cart)
    if cart == already_gone + 1:
        already_gone += 1
        while stack and stack[-1] == already_gone + 1:
            stack.pop()
            already_gone += 1
    else:
        stack.append(cart)

if stack:
    print("NO")
else:
    print("YES")
