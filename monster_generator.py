from random import *
from type import *

class Monster(object):
    def __init__(self, name, dmg, spd, hlth, lvl):
        self.name = name
        self.dmg = dmg
        self.spd = spd
        self.hlth = hlth
        self.lvl = lvl
        
    def encounter(self):
        type('You encounter a ' + self.name + '!')
        type('The ' + self.name + ' closes in for a fight.')
        type('The ' + self.name + ' has ' + str(self.hlth) + ' health and is level ' + str(self.lvl) + '!')


def monster_generator(lvl):
    Mod = {
        "bad" : 0.9,
        "normal" : 1,
        "good" : 1.1,
    }

    qlty = choice(list(Mod.keys()))
    mod = Mod[qlty]
    if randint(1, 10) == 1:
        item = True
    else:
        item = False

    if lvl > 5:
        dmg = mod * randint(lvl - 5, lvl + 5)
        spd = mod * randint(lvl - 5, lvl + 5)
        hlth = mod * randint(lvl - 5, lvl + 5)
    else:
        dmg = mod * randint(1, lvl + 5)
        spd = mod * randint(1, lvl + 5)
        hlth = mod * randint(1, lvl + 5)
        
    names = ['zombie', 'ogre', 'troll', 'orc']
    name = qlty + " " + choice(names)

    return(name, dmg, spd, hlth, item)
    
