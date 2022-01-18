#!/usr/bin/env python3

# Import libraries
import sys
import pathlib
import ast
import os


class Data:
    def __init__(self):
        # Get user's home directory
        self.user_home = os.system("whoami")
        # Set log path
        self.log_path = "/home/{}/.config/unity3d/Nomoon/Mindnight/Player.log".format(self.user_home)
        # Check if player.log exists in given file path
        if not pathlib.Path(self.log_path).exists():
            sys.exit("Log not found.")

        # Declare packet list
        self.packets = []

    def parse(self, log_path):
        # Open player.log as log
        with open(log_path, 'r') as log:
            for line in enumerate(log):
                a_line = line[1].split(" ", 4)
                try:
                    if len(a_line[1]) == 9 and not a_line[1][2] == ".":
                        time = a_line[1]
                        cur_dict = ast.literal_eval(
                            a_line[-1:][0].split(":", 1)[1].replace("false", "False").replace("true", "True"))
                        if cur_dict["Type"] == 307:
                            cur_dict.pop("Type")
                            cur_dict.pop("Passed")
                            self.packets.append(cur_dict)
                except:
                    pass
                last_line = line

            hackers = (str(last_line).split(":", 4)[
                       4][:-4].replace('\"\"', '\"').replace("false", "'False'").replace("true", "'True'"))
            hackers = list(hackers.split("Canceled", 1))[0][:-2] + '}'
            hackers = ast.literal_eval(hackers)['Hackers']

            return hackers

    def export(self, file):
        with open(file, 'w+') as f:
            f.write(str(self.new_list))

    def getfilenum(self):
        for file in os.listdir('src/games/'):
            if file[0:4] == 'game' and file[-4:] == '.txt':
                game_num = (file[:-4])[4:]
                log_path = 'src/games/game{}.txt'.format(game_num)
                hackers = self.parse(log_path)
                if len(hackers) > 2 or hackers[0] == 5 or hackers[1] == 5:
                    continue
                else:
                    self.add_labels(hackers)
                    self.export('src/games/e_game{}.txt'.format(game_num))
