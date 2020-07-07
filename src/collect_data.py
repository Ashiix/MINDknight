def collect(num_files):
    import ast
    import os

    #numfiles = int(input("How many files are you exporting from? (Please input an integer) \n>"))

    final_data = 'final_data.txt'


    def add_data(num_files):
        for i in range(num_files):
            with open(('src/games/e_game{}.txt'.format(i)),'r') as f:
                with open(final_data, 'a') as export:
                    f_list = ast.literal_eval(f.read()) # translate read file into the list it really is
                    for item in f_list:
                        export.write((str(item)+',')) # write each item, putting a , afterwards.

    with open(final_data, 'w') as final: # startthe list with open bracket
        final.write('[')

    with open(final_data, 'a') as final: # add data to open list, get size in bytes, remove a single char worth of bytes (removes list comma), and end list ]
        add_data(num_files)
        final.seek(0,2)
        size = final.tell() # size in bytes
        final.truncate(size-1) # subtract last charc (truncate will change file to defined size)
        final.write("]") # add extra ] to make it into a list, allowing us to do for item in file when creating data frame.

    final.close()
