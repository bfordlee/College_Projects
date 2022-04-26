#Hint: Larger numbers make larger trees

stump = raw_input('What keyboard character should the stump be?:')
width = input('How wide should this trees base be? (enter an odd integer):')
tree_char = raw_input('What character do you want for the tree?:')
ornaments = raw_input('Input character for your ornaments:')
orn_row = input('Which row should the ornament go in?:')
orn_col = input('Which column should the ornament go in?:')

print "\n"

while width % 2 == 0:
    print "We need an odd integer for tree width, try again."
    width = input('How wide should this trees base be? (enter an odd integer):')

space_num = (width / 2)
number = 1
row_count = 1
row_list = []

while number <= width:
    row = " " * space_num + tree_char * number
    lrow = list(row)
    if row_count == orn_row:
        lrow[orn_col - 1 + space_num] = ornaments
    row_count += 1
    row = ''.join(lrow)
    print row
    row_list.append(row)
    number += 2
    space_num -= 1

stump_space = (width / 2) - 1
print " " * stump_space + 3 * stump  # prints the 1x3 stump