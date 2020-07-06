#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

from src.data import Data

def main():
    temp = Data() # temp, will usually equal Model()
    temp.parse()
    temp.add_labels()
    temp.export('src/games/e_game2.txt')

if __name__ == "__main__":
    main()
