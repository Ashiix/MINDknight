#!/usr/bin/env python3

import sys
import os.path


class Scraping:
    def __init__(self):
        home = "ash"

        self.log_path = "rawgames.csv"
        print(self.log_path)
        self.game = []

        self.game_num = 1
        while True:
            if not os.path.isfile('src/games/game{}.txt'.format(self.game_num)):
                break
            self.game_num += 1

    def external_scrape(self):
        in_game = False
        line_num = 0
        with open(self.log_path, 'r') as log:
            for line in enumerate(log):
                line_txt = line[1].replace("\n", "")
                if "GameStart" in line_txt or in_game == True:
                    in_game = True
                    self.game.append(line_txt)
                    if "Received GameEnd" in line_txt:
                        with open("src/games/game{}.txt".format(str(self.game_num)), "a") as game_file:
                            for line_game in enumerate(self.game):
                                game_file.write(line_game[1] + "\n")
                        print("Wrote game to file.")
                        self.game_num += 1
                        in_game = False
                        self.game = []
                line_num += 1
