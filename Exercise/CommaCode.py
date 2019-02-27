# Comma Code program

# function that takes in List
# and prints the list item in single line with last item on the list
# seperated by and.
def printWithComma(aList):
    for position in range(len(aList)):
        if(position == (len(aList) - 1)):
            print('and ' + aList[position], end='')
        else:
            print(aList[position] +', ',end ='')

spam = ['apple', 'banana', 'tofu', 'cat']
printWithComma(spam)
