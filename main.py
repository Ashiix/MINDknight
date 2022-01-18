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


if __name__ == "__main__":
    main()
