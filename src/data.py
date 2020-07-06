#!/usr/bin/env python3

# 205 - Message
# 102 - GameFound
# 201 - GameStart
# 202 - SpawnPlayer
# 304 - SelectPhaseEnd
# 307 - VotePhaseEnd
# 311 - MissionPhaseEnd
# 203 - GameEnd

# Import libraries
import sys
import pathlib
import ast

# Create class Parse
class Data:
    # Init
    def __init__(self):
        # Get currently running OS
        os = sys.platform
        # Get user's home directory
        self.user_home = input("User home dir name: ")
        # Set log_path based on detected OS
        if os == "linux":
            self.log_path = "/home/{}/.config/unity3d/Nomoon/Mindnight/Player.log".format(self.user_home)
        elif (os == "win32"):
            self.log_path = "%\\{}%\\AppData\\LocalLow\\Nomoon\\Mindnight\\Player.log".format(self.user_home)
        else: # If unable to detect OS, ask for manual input
            print("Unable to detect OS for log file path, please input it manually.")
            self.log_path = input("Path: ")
        # Check if player.log exists in given file path
        if not pathlib.Path(self.log_path).exists():
            sys.exit("The file can't be found in the given log path. This is most likely because you entered your home dir incorrectly.")

        self.log_path = 'src/games/game1.txt'
        # Declare packet list
        self.packets_test = open(log_path, 'r')
        self.packets_train = open(log_path, 'r')
        self.packets = []

    # Read log in realtime (WIP)
    def read_log(self):
        with open(self.log_path, 'r') as log: # Open player.log in using log_path
            for line in enumerate(log):
                line = line[1].split(" ",4)
                try:
                    if len(line[1]) == 9 and not line[1][2] == ".":
                        time = line[1]
                        cur_dict = ast.literal_eval(line[-1:][0].split(":",1)[1].replace("false","False").replace("true","True"))
                        if cur_dict["Type"] == 307 or cur_dict["Type"] == 311 or cur_dict["Type"] == 205 or cur_dict["Type"] == 304:
                            self.packets.append(cur_dict)
                except: pass

    def add_labels(self):
        print(self.packets)
