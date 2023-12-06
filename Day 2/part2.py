import os

# Input path
dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path + "\Inputs\Day2"

# Reading input
data = open(input_path, 'r')
Content = data.read()
lines = Content.split("\n")

# game counter
game_c = 0
curr = 0

for i in range(len(lines)):
    # maxes
    red_m = 0
    green_m = 0
    blue_m = 0

    trash, need = lines[i].split('Game')
    curr, games = need.split(":")
    curr = curr.replace(" ", "")


    for game in games.split(";"):
        for cubes in game.split(","):
            cubes = cubes.replace(" ", "")
            if "red" in cubes:
                cubes, trash = cubes.split("red")
                red_m = max(int(cubes), red_m)

            if "blue" in cubes:
                cubes, trash = cubes.split("blue")
                blue_m = max(int(cubes), blue_m)

            if "green" in cubes:
                cubes, trash = cubes.split("green")
                green_m = max(int(cubes), green_m)

    game_c += red_m*blue_m*green_m

print(game_c)