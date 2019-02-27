#! python3
# tablePrinter.py - takes a list of lists of strings and dispalys it in a well
# organized table with each column right-justified.

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(listOfData):
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = len((max(listOfData[i], key=len)))
        
    row = (len(tableData[0]))
    column =(len(colWidths))
    
    for x in range(row):
        for y in range(column):
            print(' '+tableData[y][x].rjust(colWidths[y]), end='')
            if(y == 2):
                print('\n',end='')

printTable(tableData)
