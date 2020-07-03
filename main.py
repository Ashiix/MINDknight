#!/usr/bin/env python3

# MINDknight - an AI (helper) for MINDNIGHT
# Developed by Ashiix and etfriedman
# Original concept by Nik-Novak and Ashiix

from src.parse import Parse

def main():
    parse = Parse()
    parse.read_log()

if __name__ == "__main__":
    main()
