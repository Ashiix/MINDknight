#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

import os
from src.model import Model
from src.data import Data
from src.collect_data import Collect
data = Data()
collect = Collect()
model = Model()


def main():
    should_parse = input("Parse data?\n[Y/n]\n> ")
    if should_parse.lower() == 'y' or should_parse == '':
        num_games = 0
        for file in os.listdir('src/games/'):
            if file[0:4] == 'game' and file[-4:] == '.txt':
                num_games += 1
        print("\nParsing data from game files...")
        data.getfilenum()
        collect.data()
        print("\nDone!")
        model.data_format()
        model.log_regression()
        model.analysis()

    else:
        model.data_format()
        model.log_regression()
        model.analysis()


if __name__ == "__main__":
    main()
