#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

import threading
from src.model import Data

def main():
    model = Data()
    model.read_log()
    model.add_labels()

if __name__ == "__main__":
    main()
