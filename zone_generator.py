from random import *
from type import *

def zoneGenerator(lvl):
    adjectives = ['dusty', 'spooky', 'scary', 'dark', 'bright', 'old', 'new']
    names = ['graveyard', 'cave', 'ghost town', 'cabin', 'camp', 'secret lair']

    name = choice(adjectives) + ' ' + choice(names)
    
    return(name, lvl)
