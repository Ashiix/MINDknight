#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

from src.model import Model

def main():
    model = Model()
    model.data_format()
    model.log_regression()
    model.predict()

if __name__ == "__main__":
    main()
