#!/usr/bin/env python3

import sys
import pathlib
import ast
from datetime import datetime

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

cur_time = str(datetime.now()).split()[1].split(".")[0] # gets current time in same format as player.log timestamp
print(cur_time)

# def get_time(type):
#     with open('parsed_packets.txt', 'r') as export_log:
#         for findline in export_log:
#             pass
#     #player.log file
#     if type == 'log':
#         last_export_time = findline.split()[1][:-1] # gets most recent log time, removes extra chars etc.
#         print(last_export_time)
#     #export file
#     elif type == 'e_log':
#         last_export_time = findline.split()[0][:-1]
#         print(last_export_time)
#
#     else: print("use log or e_log depending on where you want to read time from")


with open(log_path, 'r') as log:
    for line in enumerate(log):
        line = line[1].split(" ",4)
        try:
            with open("parsed_packets.txt",'a') as f:
                #print("im here")
                if len(line[1]) == 9 and not line[1][2] == ".":
                    time = line[1]
                    cur_dict = ast.literal_eval(line[-1:][0].split(":",1)[1].replace("false","False").replace("true","True"))
                    if cur_dict["Type"] == 307 or cur_dict["Type"] == 311 or cur_dict["Type"] == 205 or cur_dict["Type"] == 304:
                        #print("printing line...")
                        f.write("{} {}\n".format(time, cur_dict))
        except: pass


#when reading data from exported file (after exporting specific
#data to that file) use old_time to get
#the last time data was exported, use this
#when giving data to model (or putting in CSV)
#in order to not repeat data, we could also check if certain times have been exported?
