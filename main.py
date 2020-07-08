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
    num_games = 1
    if should_parse == 'y':
        data = Data()
        #num_games = int(input("How many games we parsin?\n> "))
        while True:
            if not os.path.isfile('src/games/e_game{}.txt'.format(num_games)):
                break
            num_games += 1
        def getfilenum(num_games):
            for i in range(num_games):
                log_path = data.filepath(i)
                hackers = data.parse(log_path)
                print(i)
                data.add_labels(hackers)
                data.export('src/games/e_game{}.txt'.format(i))
        getfilenum(num_games)
        collect(num_games)
    else:
        pass

if __name__ == "__main__":
    main()
