# Character Picture Grid

grid = [['.','.','.','.','.','.'],
        ['.','O','O','.','.','.'],
        ['O','O','O','O','.','.'],
        ['O','O','O','O','O','.'],
        ['.','O','O','O','O','O'],
        ['O','O','O','O','O','.'],
        ['O','O','O','O','.','.'],
        ['.','O','O','.','.','.'],
        ['.','.','.','.','.','.']]

# x co-ordinate 
for x in range(len(grid[0])):
    # y co-ordinate
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print('\n')

