"""
    Wants to be displayed like:
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    etc....
    Total Number of items: 100
"""
import pprint

possibleLoot = [ 'rope', 'torch', 'gold coin', 'dagger', 'arrow']

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger' : 1, 'arrow': 12}

def displayInventory(amount, backpack):
    print("Inventory:")

    for item in backpack:
        if item in amount:
            amount[item] += 1
        else:
            amount[item] = 1

    item_total = sum(inventory.values())

    pprint.pprint(amount, width= 5)

    print ("Total Number of items: " + str(item_total))

displayInventory(inventory, possibleLoot)