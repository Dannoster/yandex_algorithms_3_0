file = open("input.txt", "r")

square_counter = 0
round_counter = 0
bracket = file.read(1)

while bracket in "()[]":
    
    if bracket == "(":
        round_counter += 1
    
    elif bracket == ")":
        if square_counter % 2 != 0:
            break
        else:
            round_counter -= 1
            if round_counter < 0:
                break

    elif bracket == "[":
        square_counter += 1
    
    elif bracket == "]":
        if round_counter % 2 != 0:
            break
        else:
            square_counter -= 1
            if square_counter < 0:
                break

    bracket = file.read(1)

if square_counter == 0 and round_counter == 0:
    print("yes")
else:
    print("no")