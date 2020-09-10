## Killer Sudoku, based on Peter Norvig's sudoku puzzle
import parsecages as parsecages

# the initial grid is empty for the more difficult versions -- so do we need a starting grid?
# instead, will need an input showing the sum boundaries
    # maybe dict with {sum1:[A1,A2,A3], sum2:[A4,B1], ...}

# to units and peers, add sum boxes

# now, every square has 4 units
    # 1. column
    # 2. row
    # 3. box
    # 4. sumbox

def cross(A,B):
    print("Cross product of elements in A and elements in B.")
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows,cols)
cages = parsecages.get_cages()

unitlist0 = ([cross(rows,c) for c in cols] + ## all rows
            [cross(r,cols) for r in rows] + ## all columns
            [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] ## all boxes
            )

## cages = {('A1','A2','B1']:sum1, ('B2','C2'):sum2],
unitlist1 = (unitlist + [list(cage) for cage in cages.keys()])

units0 = dict((s, [u for u in unitlist if s in u]) for s in squares)

# would need to bring in sum information - constraints (e.g., 3 can only be 2,1) ?
# the alternative is to iteratively try all sums

## could add a check for those sums that have only one possible combination
    ## e.g. sum=3 in len(cage)=3 --> only 1,2 possible
    ## e.g. sum=24 in len(cage)=4 --> only 7,8,9 possible

## could start with a check for size 2 cages that come with a hint

grid1_nums = '000000000000000000000607000000000000000000000000000000000708000000000000000000000'
grid1_cages = parsecages.get_cages()
