#!/usr/bin/env python3

# Import libraries
import ast
import os


class Collect:
    # Data collection function
    def data(self):

        final_data = 'final_data.txt'

        def add_data():
            for file in os.listdir('src/games/'):
                if file[0:6] == 'e_game' and file[-4:] == '.txt':
                    with open(('src/games/{}'.format(file)), 'r') as f:
                        with open(final_data, 'a') as export:
                            # Fit read file into a list
                            f_list = ast.literal_eval(f.read())
                            for item in f_list:
                                # Export each item in list
                                export.write((str(item) + ','))

        with open(final_data, 'w') as final:
            final.write('[')

        # Add data to open list, get size in bytes, remove a single char worth of bytes (removes list comma), and end list ]
        with open(final_data, 'a') as final:
            add_data()
            final.seek(0, 2)
            size = final.tell()  # Size in bytes
            # Subtract last char (truncate will change file to defined size)
            final.truncate(size - 1)
            # Add extra ] to make it into a list, allowing us to do for item in file when creating dataframe
            final.write("]")

        final.close()
