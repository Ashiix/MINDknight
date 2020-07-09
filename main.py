#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

# Import libraries
import os
from src.model import Model
from src.data import Data
from src.collect_data import Collect

# Instantiate classes
data = Data()
collect = Collect()
model = Model()


# Main function
def main():
    # Welcome
    print("MINDknight alpha\nAn AI (helper) for MINDNIGHT")
    # Ask user for course of action
    should_parse = input("\nParse data?\n[Y/n]\n> ")
    # Parse if user says to
    if should_parse.lower() == 'y' or should_parse == '':
        num_games = 0
        for file in os.listdir('src/games/'):
            if file[0:4] == 'game' and file[-4:] == '.txt':
                num_games += 1
        print("\nParsing data from game files...")
        data.getfilenum()
        collect.data()
        print("Done!")
        # Run model
        print("\nRunning model...")
        model.data_format()
        model.log_regression()
        model.analysis()

    # Just run model, don't parse
    else:
        # Run model
        print("\nRunning model...")
        model.data_format()
        model.log_regression()
        model.analysis()


if __name__ == "__main__":
    main()
