def collect():
    import ast
    import os

    #numfiles = int(input("How many files are you exporting from? (Please input an integer) \n>"))

    final_data = 'final_data.txt'

    def add_data():
        for file in os.listdir('src/games/'):
            if file[0:6] == 'e_game' and file[-4:] == '.txt':
                with open(('src/games/{}'.format(file)), 'r') as f:
                    with open(final_data, 'a') as export:
                        # translate read file into the list it really is
                        f_list = ast.literal_eval(f.read())
                        for item in f_list:
                            # write each item, putting a , afterwards.
                            export.write((str(item) + ','))

    with open(final_data, 'w') as final:  # startthe list with open bracket
        final.write('[')

    # add data to open list, get size in bytes, remove a single char worth of bytes (removes list comma), and end list ]
    with open(final_data, 'a') as final:
        add_data()
        final.seek(0, 2)
        size = final.tell()  # size in bytes
        # subtract last charc (truncate will change file to defined size)
        final.truncate(size - 1)
        # add extra ] to make it into a list, allowing us to do for item in file when creating data frame.
        final.write("]")

    final.close()
