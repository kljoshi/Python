
# function to add items into dictionary if it doesnt exist else increment the counter value
# if the item exists. 
def addToInventory(inventory, addedItems):

    # loop through items in the dragonLoot, which is a list
    for item in addedItems:

        # condition to check if item in the dragonLoost already exists in inventory 
        if(inventory.get(item)):

            # if item exits increment the counter and update the value 
            inventory[item] = inventory.get(item)+1

        # if item doesn't exits in the dictionary add it to the inventory    
        else:
            inventory[item] = 1

    # return the new updated inventory
    return inventory
                

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
    print("\nTotal number of items: " + str(total_item))

# declared a dictionary  
inv = {'gold coin': 42, 'rope': 1}

# declared a list 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# call the function addToInventory
inv = addToInventory(inv, dragonLoot)

# takes in new inventory dictionary and display items in it 
displayInventory(inv)

