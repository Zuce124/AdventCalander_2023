import os

# Input path
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path + "\Inputs\Day2"

# Reading input
data = open(input_path, 'r')
Content = data.read()
lines = Content.split("\n")

# maxes
red_m = 12
green_m = 13
blue_m = 14

# game counter
game_c = 0
curr = 0

for i in range(len(lines)):
    checker_returns = []
    checker = True

    trash, need = lines[i].split('Game')
    curr, games = need.split(":")
    curr = curr.replace(" ", "")


    for game in games.split(";"):
        for cubes in game.split(","):
            cubes = cubes.replace(" ", "")
            if "red" in cubes:
                cubes, trash = cubes.split("red")
                if int(cubes) > red_m:
                    checker = False
                    checker_returns.append(checker)

            if "blue" in cubes:
                cubes, trash = cubes.split("blue")
                if int(cubes) > blue_m:
                    checker = False
                    checker_returns.append(checker)

            if "green" in cubes:
                cubes, trash = cubes.split("green")
                if int(cubes) > green_m:
                    checker = False
                    checker_returns.append(checker)

    if False not in checker_returns:
        game_c += int(curr)

print(game_c)