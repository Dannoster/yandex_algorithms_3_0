def main():
    file = open("input.txt", "r")

    bracket = file.read(1)
    if bracket in ")]":
        print("no")
        return 1
    string = ""

    pair_to = {"}":"{",
               ")":"(",
               "]":"[",}

    while bracket in "()[]{}":
        if bracket in "([{":
            string += bracket
        else:
            if string and string[-1] == pair_to[bracket]:
                string = string[:-1]
            else:
                string += "e"
                break

        bracket = file.read(1)

    if not string:
        print("yes")
    else:
        print("no")

main()