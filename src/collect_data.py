import ast
import os

numfiles = int(input("How many files are you exporting from? (Please input an integer) \n>"))

final_data = 'final_data.txt'


def add_data():
    for i in range(1, numfiles+1):
        with open(('games/e_game{}.txt'.format(i)),'r') as f:
            with open(final_data, 'a') as export:
                f_list = ast.literal_eval(f.read()) # translate read file into the list it really is
                for packet in f_list:
                    packet.pop("Type") # remove Type, dont need in data
                    packet.pop("Passed")
                #print(f_list)
                for item in f_list:
                    export.write((str(item)+','))

with open(final_data, 'w') as final:
    final.write('[')

with open(final_data, 'a') as final:
    add_data()
    final.seek(0,2)
    size = final.tell() # size in bytes
    final.truncate(size-1) # subtract last charc (truncate will change file to defined size)
    final.write("]") # add extra ] to make it into a list, allowing us to do for item in file when creating data frame.

final.close()
