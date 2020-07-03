#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

from src.data import Data

def main():
    data = Data()
    data.read_log()

    print(data.packets)

if __name__ == "__main__":
    main()
