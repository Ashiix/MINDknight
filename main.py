#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

import os
from src.model import Model
from src.data import Data
from src.collect_data import collect

def main():

    should_parse = input("Parse data?\n[ y / n]\n> ")
    if should_parse == 'y':
        data(should_parse)
    else:
        model = Model()
        model.data_format()
        model.log_regression()
        model.predict()


def data(should_parse):
    num_games = 0
    if should_parse == 'y':
        data = Data()
        #num_games = int(input("How many games we parsin?\n> "))
        for file in os.listdir('src/games/'):
            if file[0:4] == 'game' and file[-4:] == '.txt':
                print(file)
                num_games += 1

        #print(num_games)
        def getfilenum():
            for file in os.listdir('src/games/'):
                if file[0:4] == 'game' and file[-4:] == '.txt':
                    game_num = (file[:-4])[4:]
                    log_path = 'src/games/game{}.txt'.format(game_num)
                    #log_path = data.filepath(game_num)
                    hackers = data.parse(log_path)
                    #data.remove_5_plus()
                    #print(hackers)
                    if len(hackers) > 2 or hackers[0] == 5 or hackers[1] == 5:
                        continue
                    else:
                        #print("test")
                        data.add_labels(hackers)
                        data.export('src/games/e_game{}.txt'.format(game_num))
        getfilenum()
        collect()
    else:
        pass

if __name__ == "__main__":
    main()
