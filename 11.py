class stack:
    def __init__(self):
        self.values = []
    def push(self, n):
        self.values.append(n)
        return "ok"
    def pop(self):
        if self.values:
            return self.values.pop()
        else:
            return("error")
    def back(self):
        if self.values:
            return self.values[-1]
        else:
            return("error")
    def size(self):
        return len(self.values)
    def clear(self):
        self.values = []
        return "ok"
    
with open("input.txt", "r") as file:
    our_stack = stack()
    command = ""
    while command != "exit":
        command = file.readline().strip()
        if command[:4] == "push":
            print(our_stack.push(int(command[5:])))
        elif command == "pop":
            print(our_stack.pop())
        elif command == "back":
            print(our_stack.back())
        elif command == "size":
            print(our_stack.size())
        elif command == "clear":
            print(our_stack.clear())
print("bye")