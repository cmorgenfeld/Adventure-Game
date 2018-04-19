def saveGame(strgth, spd, chrsma, hlth):
    with open('save_game.txt', 'w') as save:
        save.write(str(strgth) + '\n')
        save.write(str(spd) + '\n')
        save.write(str(chrsma) + '\n')
        save.write(str(hlth) + '\n')

def loadGame():
    with open('save_game.txt', 'r') as load:
        strgth = int(load.readline())
        spd = int(load.readline())
        chrsma = int(load.readline())
        hlth = int(load.readline())

        return(strgth, spd, chrsma, hlth)
