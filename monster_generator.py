from random import *
from type import *

class Monster(object):
    def __init__(self, name, dmg, spd, hlth):
        self.name = name
        self.dmg = dmg
        self.spd = spd
        self.hlth =hlth

def monster_generator():
    dmgMod = {
        "bad" : 0.9,
        "normal" : 1,
        "good" : 1.1,
    }

    qlty = choice(list(dmgMod.keys()))
    mod = dmgMod[qlty]

    names = ['zombie', 'ogre', 'troll', 'orc']
    name = qlty + " " + choice(names)

    type("You encounter a " + name + "!")
    return(mod, name)
    
