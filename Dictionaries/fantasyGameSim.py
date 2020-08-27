"""
    Wants to be displayed like:
    Inventory: 
    12 arrow
    42 gold coin 
    1 rope 
    etc....
"""     
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger' : 1, 'arrow': 12}

def displayInventory(backpack):
    print("Inventory:")
    
    item_total = 0 
    for k,v in backpack.items():
        item_total = item_total + k.get(v)


    print ("Total Number of items: " + str(item_total)) 

displayInventory(inventory)