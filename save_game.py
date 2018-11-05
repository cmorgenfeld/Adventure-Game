def saveGame(name, strgth, spd, chrsma, hlth, inventoryList):
    inventory = ''
    for i in range(len(inventoryList) - 1):
        inventory += inventoryList[i] + ', '
    inventory += inventoryList[i + 1]
    with open('save_game.txt', 'w') as save:
        save.write(name + '\n')
        save.write(str(strgth) + '\n')
        save.write(str(spd) + '\n')
        save.write(str(chrsma) + '\n')
        save.write(str(hlth) + '\n')
        save.write(str(inventory) + '\n')

def loadGame():
    with open('save_game.txt', 'r') as load:
        name = load.readline()
        strgth = int(load.readline())
        spd = int(load.readline())
        chrsma = int(load.readline())
        hlth = int(load.readline())
        inventory = load.readline()[:-1]

        return(name, strgth, spd, chrsma, hlth, inventory.split(', '))
