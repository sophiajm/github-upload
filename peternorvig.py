## solving every sudoku puzzle, by Peter Norvig
## http://www.norvig.com/sudoku.html

## two ideas applied: constraint propagation and search

## r = row
## c = column
## s = square
## d = digit
## u = unit
## grid is a grid, 81 non-blank chars
## solution is dictionary of possible solution, e.g. {'A1':'12349','A2':'8',...}

def cross(A,B):
    print("Cross product of elements in A and elements in B.")
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows,cols)
unitlist = ([cross(rows,c) for c in cols] + [cross(r,cols) for r in rows] +
            [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

# test
#print(squares)
print("UNITLIST")
print(unitlist)
print("UNITS")
print(units)
print("PEERS")
print(peers)
#
# print(len(squares))
# print(len(unitlist))
# print(all(len(units[s]) == 3 for s in squares))
# print(all(len(peers[s]) == 20 for s in squares))

# def test():
#     "A set of unit tests."
#     assert len(squares) == 81
#     assert len(unitlist) == 27
#     assert all(len(units[s]) == 3 for s in squares)
#     assert all(len(peers[s]) == 20 for s in squares)
#     assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
#                            ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
#                            ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
#     assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
#                                'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
#                                'A1', 'A3', 'B1', 'B3'])
#     print 'All tests pass.'

print("All elements defined.")
# next, define the playing grid
# grid = textual format specifying the initial state of the puzzle - digit as string, and period specifying empty
# solution = internal representation of current state of the puzzle - gives possible values remaining for each square

# parse the grid into a solution dict
# start with every square can be any digit, then assign values from the given grid
solution = dict((s,digits) for s in squares)
# print(solution)

def parse_grid(grid):
    print("Convert grid to dict of possible values, {square: digits}, return False if contradiction detected")
    for s,d in grid_values(grid).items():
        if d in digits and not assign(solution,s,d):
            return False # if value d cannot be assigned to square s, return false
    return solution

def grid_values(grid):
    print("Convert grid into a dict of {square: char} with 0 or period for empty squares")
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    # print(dict(zip(squares,chars)))
    return dict(zip(squares,chars))

# Constraint Propagation
# using assign(solution, s, d)
    # instead of solution[s]=d because:
# Two Important Sudoku Strategies:
    # (1) if a square only has one possible value, eliminate that value from the square's peers
    # (2) if a unit has only one possible place for a value, put the value there
# following these strategies to update the rows,cols,boxes is called constraint propagation
# the function assign(solution,s,d) will return the updated solution dictionary, updated using constraint propagation as above
    # the function will return False if it hits a contradiction

# the fundamental operation is not assigning a value, but rather eliminating possible values one by one from a square
# implement elimination with a function eliminate(solution, s, d)
# with this function, assign(solution,s,d) can be defined as "eliminate all the values from s except d"

# Define these functions
def assign(solution,s,d):
    #print("assign function called with square {} ,digit {}".format(s,d))
    #print("Eliminate all values except d from solution[s] and propagate. return solution, return False if contradiction detected")
    # for value at key s, replace digit d with empty string, assign the remaining digits to other_values
    # the original solution dictionary will contain the full possible digits
    other_values = solution[s].replace(d,'')
    # iterate through remaining possible values for that square, eliminating each
    # if all successfully eliminated, return original solution dict with only the assigned digit d remaining for that square
    if all(eliminate(solution,s,d2) for d2 in other_values):
        return solution
    else:
        return False

def eliminate(solution,s,d2):
    #print("eliminate function called with square {} , digit {}".format(s,d2))
    #print("Eliminate d2 from solution[s]; propagate when values <= 2 (only one possible value left). Return solution, return False if contradiction detected")
    ## if already eliminated return the solution dict
    if d2 not in solution[s]:
        #print("eliminate function returned")
        return solution
    ## otherwise, eliminate the digit
    solution[s] = solution[s].replace(d2,'')

    ## (1) if a square s is reduced to one value d3, then eliminate d3 from its peers
    if len(solution[s]) == 0:
        return False ## Contradiction check: last value removed from square
    elif len(solution[s]) == 1:
        d3 = solution[s] # one value left
        if not all(eliminate(solution,s2,d3) for s2 in peers[s]):
            return False
    #elif len(solution[s]) == 2

    ## (2) if a unit u is reduced to only one possible place for digit d, then assign it there
    for u in units[s]:
        dplaces = [s for s in u if d2 in solution[s]]
        if len(dplaces) == 0:
            return False ## Contradiction check: no place for this digit
        elif len(dplaces) == 1:
            # one place left for this digit, assign it there
            if not assign(solution,dplaces[0],d2):
                return False
    #print("eliminate function returned")
    return solution



# visually display the puzzle
def display(grid):
    print("Display the values as a 2-D grid.")
    width = 1+max(len(grid[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(grid[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': print(line)
    print()


# possible add-ons for more difficult puzzles

# (3) Twins strategy - look for two squares in same unit that have the same two possible digits
    # e.g., Given {'A5':'26','A6':26', ...}, eliminate 2 and 6 from every other square in the A row unit
# add an elif len(solution[s]) == 2 in eliminate function

# Search algorithm
# first make sure there is not already a solution or a contradiction
# if not, choose one unfilled square and consider all its possible values
# try assigning a possible digit to the square one at a time, and search from resulting
# if the search leads to failed position, go back and consider another possible digit d
# recursive search
# depth-first search - recursively consider all possibilities of d for one square s before moving on to another square s

# create a new copy of solutions for each recursive call to search
# this makes each branch of search tree independent
# this is why digits were made as strings - easily use .copy()
# alternative would be backtracking search - keep track of change to solution and undo the change when hit dead end

# to implement the search, choose an order
    # variable ordering = which square do we try first?
    # value ordering = which digit do we try first for the square?
# for variable ordering - use heuristic 'minimum remaining values'
# for value ordering - just consider digits in ascending numeric order

def solve(grid):
    print("called solve function")
    result = search(parse_grid(grid))
    print("RESULT CREATED")
    print(result)
    return result

def search(solution):
    print("called search function")
    #print("Using depth-first search and propagation, try all possible values")
    if solution is False:
        return False ## Contradiction already found
    if all(len(solution[s]) == 1 for s in squares):
        return solution ## grid already solved

    ## variable ordering - choose an unfilled square with fewest possibilities
    n,s = min((len(solution[s]),s) for s in squares if len(solution[s])>1)
    print("DISPLAY IN SEARCH")
    display(solution)
    return some(search(assign(solution.copy(),s,d)) for d in solution[s])

def some(sequence):
    print("called some function")
    #print("Return some element of sequence that is true")
    for element in sequence:
        if element: return element
    return False

grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid_ClassicHard4 = '009040600270000049800000001000908000300000005000307000100000004430000078002010500'
display(grid_values(grid_ClassicHard4))
#display(parse_grid(grid_ClassicHard4))
display(solve(grid_ClassicHard4))
