from random import *
from type import *

def weaponGenerator():
    dmgMod = {
        "bad" : 0.9,
        "normal" : 1,
        "good" : 1.1,
    }
    qlty = choice(list(dmgMod.keys()))
    mod = dmgMod[qlty]

    items = ['mace', 'bow', 'sword', 'armor', 'helmet', 'shield']
    item = qlty + " " + choice(items)

    type("You found a " + item +"!")
    return(mod, item)
