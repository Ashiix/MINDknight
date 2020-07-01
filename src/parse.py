#!/usr/bin/env python3

import re
import sys
import pathlib
import ast

os = sys.platform

user_home = input("User home dir name: ")
if os == "linux":
    log_path = "/home/{}/.config/unity3d/Nomoon/Mindnight/Player.log".format(user_home)
elif (os == "win32"):
    log_path = "%\\{}%\\AppData\\LocalLow\\Nomoon\\Mindnight\\Player.log".format(user_home)
else:
    print("Unable to detect OS for log file path, please input it manually.")
    log_path = input("Path: ")

if not pathlib.Path(log_path).exists():
    sys.exit("The file can't be found in the given log path. This is most likely because you entered your home dir incorrectly.")

with open(log_path, 'r') as log:
    for line in enumerate(log):
        line = line[1].split()
        try: print(ast.literal_eval(line[-1:][0].split(":",1)[1].replace("false","False").replace("true","True")))
        except: pass
log.close()
