from random import *
from type import *

class Monster(object):
    def __init__(self, name, dmg, spd, hlth, lvl):
        self.name = name
        self.dmg = dmg
        self.spd = spd
        self.hlth =hlth
        self.lvl = lvl

def monster_generator(lvl):
    Mod = {
        "bad" : 0.9,
        "normal" : 1,
        "good" : 1.1,
    }

    qlty = choice(list(Mod.keys()))
    mod = Mod[qlty]

    dmg = mod * randint(1, lvl)
    
    names = ['zombie', 'ogre', 'troll', 'orc']
    name = qlty + " " + choice(names)

    type("You encounter a " + name + "!")
    return(mod, name)
    
