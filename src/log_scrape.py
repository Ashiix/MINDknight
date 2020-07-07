#!/usr/bin/env python3

import sys
import os.path

home = "ash"

log_path = "/home/{}/.config/unity3d/Nomoon/Mindnight/Player.log".format(home)
print(log_path)
line_num = 0
in_game = False
game = []

game_num = 1
while True:
    if not os.path.isfile('games/game{}.txt'.format(game_num)):
        break
    game_num += 1

with open(log_path, 'r') as log:
    for line in enumerate(log):
        line_txt = line[1].replace("\n", "")
        if "GameStart" in line_txt or in_game == True:
            in_game = True
            game.append(line_txt)
            if "Received GameEnd" in line_txt:
                with open("games/game{}.txt".format(str(game_num)), "a") as game_file:
                    for line_game in enumerate(game):
                        game_file.write(line_game[1]+"\n")
                print("Wrote game to file.")
                game_num += 1
                in_game = False
                game = []
        line_num += 1
