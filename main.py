#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

import threading
from src.data import Data

def main():
    data = Data()
    data.read_log()
    
    for i in range(len(data.packets)):
        print(data.packets[i])

if __name__ == "__main__":
    main()
