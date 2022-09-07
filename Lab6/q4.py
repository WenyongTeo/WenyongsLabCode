#lab 6(2) Q4
from lib import getIntegerRange, getPositiveInteger

def menuOption():
    print("Menu")
    print("1. Purchase Soup")
    print("2. Replenish Soup")
    print("3. Display all soup")
    print("0. Quit")
    option = getIntegerRange("Enter choice: ", 0, 3)
    return option

def initializeSoups(filename):
    infile = open(filename, 'r')
    dict = {}
    for oneLine in infile: # Clam Chowder, 50
        key = oneLine[0] # first char as key
        soup, quantity = oneLine.strip().split(', ')
        valueList = [soup, int(quantity)]
        # set to dictionary
        dict[key] = valueList
    infile.close()
    print(dict)
    return dict

def purchaseSoup(inventory):
    # all the keys ffor availabe soups
    availableSoups = [ v for v in inventory.values() if v[1] > 0 ]
    print(availableSoups)
    displayStore(availableSoups)

    # soup selection w/ validation
    choiceSoup = input('Enter first character of the soup available: ').upper()
    if choiceSoup in inventory:
        currentQty = inventory[choiceSoup][1]
        if currentQty > 0:
            purchaseQty = getPositiveInteger('Enter purchase quantity: ')
            if purchaseQty > currentQty:
                print("No enough quantity to serve...")
            else:
                inventory[choiceSoup][1] = currentQty - purchaseQty
                print("Thank you, have a nice meal")
        else:
            print("Soup not available...")
    else:
        print("Soup not available...")

def replenishSoup(inventory):
    # all the keys ffor availabe soups
    emptySoups = [ v for v in inventory.values() if v[1] == 0 ]
    print(emptySoups)
    displayStore(emptySoups)

    # soup selection w/ validation
    choiceSoup = input('Enter soup to replenish: ').upper()
    if choiceSoup in inventory:
        currentQty = inventory[choiceSoup][1]
        if currentQty == 0:
            replenishQty = getPositiveInteger('Enter quantity: ')
            if replenishQty > 50:
                print("Cannot replenish more than 50...")
            else:
                inventory[choiceSoup][1] = replenishQty
                print("Ready to serve")
        else:
            print("Soup cannot be replenish...")
    else:
        print("Soup not available...")


def displayStore(inventoryList):
    print("========================")
    print("{:<15s} {:<8s}".format("Soup", "Qty left"))
    for soupItem in inventoryList:
        print("{:<15s} {:^8d}".format(soupItem[0], soupItem[1]))
    print("========================")

def outfile(filename, dict):
    # write to file
    outfile = open(filename, 'w')
    for k,v in dict.items():
        outfile.write('{}, {}\n'.format(v[0], v[1]))
    outfile.close()

def main():
    inventory = initializeSoups("soups.txt")
    while True:
        option = menuOption()
        if option == 1:
            purchaseSoup(inventory)
        elif option == 2:
            replenishSoup(inventory)
        elif option == 3:
            displayStore(inventory.values())
        else:
            outfile("soups.txt", inventory)
            break
main()