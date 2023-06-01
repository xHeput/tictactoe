# write your code here
user_input = input("write your game: ")

print("---------")
print("|", user_input[0], user_input[1], user_input[2], "|")
print("|", user_input[3], user_input[4], user_input[5], "|")
print("|", user_input[6], user_input[7], user_input[8], "|")
print("---------")

x_win = 0
o_win = 0
not_win_num = 0
# checks for win in diagonal axes
for i in ["X", "O"]:
    if user_input[0] == i and user_input[4] == i and user_input[8] == i:
        print(i, "wins")
    elif user_input[2] == i and user_input[4] == i and user_input[6] == i:
        print(i, "wins")
    else:
        not_win_num += 1


# checks for win in horizontal = poziomy line
for i in [0, 3, 6]:
    if user_input[i] == "X" and user_input[i + 1] == "X" and user_input[i + 2] == "X":
        x_win += 1
    elif user_input[i] == "O" and user_input[i + 1] == "O" and user_input[i + 2] == "O":
        o_win += 1
    else:
        not_win_num += 1


# checks for win in vertical = pionowy line
for j in range(3):
    if user_input[j] == "X" and user_input[j + 3] == "X" and user_input[j + 6] == "X":
        x_win += 1
    elif user_input[j] == "O" and user_input[j + 3] == "O" and user_input[j + 6] == "O":
        o_win += 1
    else:
        not_win_num += 1

x_number = 0
o_number = 0
# checking if there are a lot more X's than O's or vice versa
for i in range(9):
    if user_input[i] == "X":
        x_number += 1
    elif user_input[i] == "O":
        o_number += 1
if (x_number - o_number) >= 2 or (o_number - x_number) >= 2:
    print("Impossible")
    exit()

# prints who won
if o_win > 0 and x_win > 0:
    print("Impossible")
    exit()
elif x_win == 1:
    print("X wins")
elif o_win == 1:
    print("O wins")

# checking for missing poles and draw
number_of_dashes = 0
if not_win_num >= 8:
    for i in range(len(user_input)):
        if user_input[i] == "_":
            print("Game not finished")
            number_of_dashes += 1
            exit()
    if number_of_dashes == 0:
        print("Draw")
