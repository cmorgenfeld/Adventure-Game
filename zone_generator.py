from random import *
from type import *

def zoneGenerator(lvl):
    adjectives = ['dusty', 'spooky', 'scary', 'dark', 'bright', 'old', 'new']
    names = ['graveyard', 'cave', 'ghost town', 'cabin', 'camp', 'secret lair']

    monsters = lvl + randint(1,3)
    name = choice(adjectives) + ' ' + choice(names)
    
    return(name, lvl, monsters)
