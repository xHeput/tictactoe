# write your code here
user_input = input("write your game: ")

print("---------")
print("|", user_input[0], user_input[1], user_input[2], "|")
print("|", user_input[3], user_input[4], user_input[5], "|")
print("|", user_input[6], user_input[7], user_input[8], "|")
print("---------")


# checks for win in diagonal axes
for i in ["X", "O"]:
    if user_input[0] == i and user_input[4] == i and user_input[8] == i:
        print(i, "wins")
        exit()
    elif user_input[2] == i and user_input[4] == i and user_input[6] == i:
        print(i, "wins")
        exit()

# checks for win in horizontal line
for i in [0, 3, 6]:
    if user_input[i] == "X" and user_input[i + 1] == "X" and user_input[i + 2] == "X":
        print("X wins")
        exit()
    elif user_input[i] == "O" and user_input[i + 1] == "O" and user_input[i + 2] == "O":
        print("O wins")
        exit()

# checks for win in vertical line
for j in range(3):
    if user_input[j] == "X" and user_input[j + 3] == "X" and user_input[j + 6] == "X":
        print("X wins")
        exit()
    elif user_input[j] == "O" and user_input[j + 3] == "O" and user_input[j + 6] == "O":
        print("O wins")
        exit()

for i in range(len(user_input)):
    if user_input[i] == "_":
        print("Game not finished")
        exit()

print("Draw")