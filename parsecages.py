def all_sq():
    rows = 'ABCDEFGHI'
    cols = '123456789'
    squares = [a+b for a in rows for b in cols]
    return squares

def get_cages():
    ## receive the information about killer sudoku cages
    squares = all_sq()
    print(squares)
    used_squares = []

    ## after user has inputted a square as belonging to a cage, remove it from squares list
    ## use try and return error if user makes error

    cages_dict = {}
    cages_dict = {('A1', 'A2', 'B1'): 11, ('A3', 'B3'): 17, ('A4', 'A5'): 9, ('A6', 'A7'): 3,
    ('A8', 'A9', 'B8'): 19, ('B2', 'C2', 'C3'): 15, ('B4', 'B5'): 11, ('B6', 'C6'): 10,
    ('B7', 'C7', 'D7'): 10, ('B9', 'C9'): 16, ('C1', 'D1', 'E1'): 16, ('C4', 'D4'): 14,
    ('C5', 'D5', 'D6'): 16, ('C8', 'D8', 'D9'): 8, ('D2', 'E2'): 8, ('D3', 'E3'): 5,
    ('E4', 'E5', 'E6'): 14, ('E7', 'F7'): 12, ('E8', 'F8'): 13, ('E9', 'F9', 'G9'): 15,
    ('F1', 'F2', 'G2'): 16, ('F3', 'G3', 'H3'): 12, ('F4', 'F5', 'G5'): 13, ('F6', 'G6'): 13,
    ('G1', 'H1'): 7, ('G4', 'H4'): 9, ('G7', 'G8', 'H8'): 16, ('H2', 'I1', 'I2'): 22,
    ('H5', 'H6'): 11, ('H7', 'I7'): 15, ('H9', 'I9', 'I8'): 9, ('I3', 'I4'): 10, ('I5', 'I6'): 10}

    used_squares = ['A1', 'A2', 'B1', 'A3', 'B3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
    'B8', 'B2', 'C2', 'C3', 'B4', 'B5', 'B6', 'C6', 'B7', 'C7', 'D7', 'B9', 'C9', 'C1',
    'D1', 'E1', 'C4', 'D4', 'C5', 'D5', 'D6', 'C8', 'D8', 'D9', 'D2', 'E2', 'D3', 'E3',
    'E4', 'E5', 'E6', 'E7', 'F7', 'E8', 'F8', 'E9', 'F9', 'G9', 'F1', 'F2', 'G2', 'F3',
    'G3', 'H3', 'F4', 'F5', 'G5', 'F6', 'G6', 'G1', 'H1', 'G4', 'H4', 'G7', 'G8', 'H8',
    'H2', 'I1', 'I2', 'H5', 'H6', 'H7', 'I7', 'H9', 'I9', 'I8', 'I3', 'I4', 'I5', 'I6']

    while len(used_squares) < 81:
        sqrs = input("Enter the squares belonging to the unit, format as a1,a2,b2, 'remove' to remove last entry: ")
        if sqrs.lower() == 'remove':
            r = used_squares[-1]
            keys = [list(k) for k in list(dic.keys())]
            k = [e for k in keys for e in k if r in k]
            #remove the boxes from used_squares
            [used_squares.remove(e) for e in k]
            cages_dict.pop(tuple(k))
            continue

        c_sqrs = input("User entered: {}. If correct, press Enter. Otherwise, re-enter: ".format(sqrs))
        if len(c_sqrs) != 0:
            sqrs = c_sqrs
        print("User entered: {}".format(sqrs))

        print(type(sqrs))

        check1 = any(s1 in 'abcdefghi123456789,' for s1 in sqrs)
        print(check1)

        while check1 is False:
            sqrs = input("Try entering the list of squares again, in simple format as a1,a2,b2: ")

        cagesum = input("Enter the sum of the squares entered above, as an integer, or enter 'again' to start this entry over: ")
        if cagesum == 'again':
            sqrs = input("Try entering the list of squares again, in simple format as a1,a2,b2: ")

        ## function needs to split user input into strings,
        list_sqrs = sqrs.split(',')
        print(list_sqrs)

        ## check if it is valid
        check = any(s in used_squares for s in list_sqrs)
        if check is True: ## square has already been used
            print("ERROR, squares already entered. Try a new cage. ")
            continue
            ## what is a good way to handle this? a while loop? a continue? a try-exception?

        ## good idea would be to have try/except type check for user error in entering
        try:
            cagesum = int(cagesum)
        except:
            cagesum = input("Try entering the sum again, as a simple integer: ")
        print("User entered sum {}".format(cagesum))

        ## remove from all squares, or add to used squares
        used_squares.extend(list_sqrs)

        ## create a tuple
        list_sqrs = [s.upper() for s in list_sqrs]
        #tup_sqrs = tuple(list_sqrs)

        ## function needs to append an entry to the dictionary
        cages_dict[tuple(list_sqrs)] = int(cagesum)
        print(list_squares)
        print(cages_dict)

    print(len(used_squares))
    print(all(s in used_squares for s in squares))
    print("COMPLETE - all squares used")
    print(cages_dict)
    display_sums(grid_sum(cages_dict)

    return cages_dict

#get_cages()

# visually display the puzzle
def display_sums(grid_dict):
    print("Display the values as a 2-D grid.")
    squares = all_sq()
    rows = 'ABCDEFGHI'
    cols = '123456789'
    width = 1+max(len(grid_dict[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(grid_dict[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': print(line)
    print()

def grid_sum(cages_dict):
    print("Convert grid into a dict of {square: sum}")
    grid_dict = {}
    for key in cages_dict:
        for e in list(key):
            grid_dict[e] = str(cages_dict[key])
    #chars = [c for c in grid if c in digits or c in '0.']
    assert len(list(grid_dict.keys())) == 81
    # print(dict(zip(squares,chars)))
    print(grid_dict)
    return grid_dict

#grid_sum(get_cages())
#display_sums(grid_sum(get_cages()))
