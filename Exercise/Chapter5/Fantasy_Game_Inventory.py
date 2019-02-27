# Fantasy Game Inventory

# this is a dictionary which means it has Keys instead of index and it points to some value 
stuff = {'rope': 1, 'touch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# this function will display all the item in the dictionary along with its value
# and the number of total item present in the dictionary 
def displayInventory(inventory):
    print('Inventory: ')

    # setting a counter 
    total_item = 0

    # loop which get key and value from inventory
    for k,v in inventory.items():

        # used to count total number of items
        total_item = total_item + v;
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(total_item))

# calling the function 
displayInventory(stuff)
