"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!                                                                                                                                                                                                                                                                                                                                                            
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_slide, print_swing

def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
    print(data)
    
    board_dict = {}
    for key in data.keys():
        for i in data[key]:
            if key == "upper":
                board_dict[(i[1], i[2])] = "({})".format(i[0].upper())
            elif key == "lower":
                board_dict[(i[1], i[2])] = "({})".format(i[0].lower())
            else:
                board_dict[(i[1], i[2])] = "Block"
   
    print_board(board_dict)