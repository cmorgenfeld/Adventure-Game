def saveGame(strgth, spd, chrsma, hlth, inventory):
    with open('save_game.txt', 'w') as save:
        save.write(str(strgth) + '\n')
        save.write(str(spd) + '\n')
        save.write(str(chrsma) + '\n')
        save.write(str(hlth) + '\n')
        save.write(str(inventory)[1:len(str(inventory)) - 1])

def loadGame():
    with open('save_game.txt', 'r') as load:
        strgth = int(load.readline())
        spd = int(load.readline())
        chrsma = int(load.readline())
        hlth = int(load.readline())
        inventory = load.readline()

        return(strgth, spd, chrsma, hlth, inventory.split(','))
