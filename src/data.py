#!/usr/bin/env python3


# Import libraries
import sys
import pathlib
import ast
import os


class Data:
    def __init__(self):
        # # Get currently running OS
        # os = sys.platform
        # # Get user's home directory
        # self.user_home = input("User home dir name: ")
        # # Set log_path based on detected OS
        # if os == "linux":
        #     self.log_path = "/home/{}/.config/unity3d/Nomoon/Mindnight/Player.log".format(self.user_home)
        # elif (os == "win32"):
        #     self.log_path = "%\\{}%\\AppData\\LocalLow\\Nomoon\\Mindnight\\Player.log".format(self.user_home)
        # else: # If unable to detect OS, ask for manual input
        #     print("Unable to detect OS for log file path, please input it manually.")
        #     self.log_path = input("Path: ")
        # # Check if player.log exists in given file path
        # if not pathlib.Path(self.log_path).exists():
        #     sys.exit("The file can't be found in the given log path. This is most likely because you entered your home dir incorrectly.")

        # Declare packet list
        self.packets = []  # Empty list to append packets to

    def parse(self, log_path):
        with open(log_path, 'r') as log:  # Open player.log as log
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

    def add_labels(self, hackers):
        self.new_list = []

        for packet in self.packets:
            new_dict = {}

            votesforpacket = packet['VotesFor']
            votesagainstpacket = packet['VotesAgainst']

            if 0 in votesforpacket:  # can be improved
                new_dict['VotesFor0'] = 1
            else:
                new_dict['VotesFor0'] = 0
            if 1 in votesforpacket:
                new_dict['VotesFor1'] = 1
            else:
                new_dict['VotesFor1'] = 0
            if 2 in votesforpacket:
                new_dict['VotesFor2'] = 1
            else:
                new_dict['VotesFor2'] = 0
            if 3 in votesforpacket:
                new_dict['VotesFor3'] = 1
            else:
                new_dict['VotesFor3'] = 0
            if 4 in votesforpacket:
                new_dict['VotesFor4'] = 1
            else:
                new_dict['VotesFor4'] = 0

            if 0 in votesagainstpacket:
                new_dict['VotesAgainst0'] = 1
            else:
                new_dict['VotesAgainst0'] = 0
            if 1 in votesagainstpacket:
                new_dict['VotesAgainst1'] = 1
            else:
                new_dict['VotesAgainst1'] = 0
            if 2 in votesagainstpacket:
                new_dict['VotesAgainst2'] = 1
            else:
                new_dict['VotesAgainst2'] = 0
            if 3 in votesagainstpacket:
                new_dict['VotesAgainst3'] = 1
            else:
                new_dict['VotesAgainst3'] = 0
            if 4 in votesagainstpacket:
                new_dict['VotesAgainst4'] = 1
            else:
                new_dict['VotesAgainst4'] = 0

            new_dict["Hackers"] = [0, 0, 0, 0, 0]

            for hacker in hackers:
                new_dict["Hackers"][hacker] = 1

            if new_dict['VotesFor0'] == 0 and new_dict['VotesFor1'] == 0 and new_dict['VotesFor2'] == 0 and new_dict['VotesFor3'] == 0 and new_dict['VotesFor4'] == 0:
                for i in range(5):
                    new_dict.pop("VotesFor{}".format(i))
                    new_dict.pop("VotesAgainst{}".format(i))
                new_dict.pop("Hackers")
            elif new_dict['VotesAgainst0'] == 0 and new_dict['VotesAgainst1'] == 0 and new_dict['VotesAgainst2'] == 0 and new_dict['VotesAgainst3'] == 0 and new_dict['VotesAgainst4'] == 0:
                for i in range(5):
                    new_dict.pop("VotesFor{}".format(i))
                    new_dict.pop("VotesAgainst{}".format(i))
                new_dict.pop("Hackers")

            self.new_list.append(new_dict)

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
