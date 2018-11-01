from random import *
from type import *

def weaponGenerator(lvl):
    dmgMod = {
        "bad" : 0.9,
        "normal" : 1,
        "good" : 1.1,
    }
    qlty = choice(list(dmgMod.keys()))
    mod = dmgMod[qlty]

    items = ['mace', 'bow', 'sword', 'armor', 'helmet', 'shield']
    item = qlty + " level " + str(lvl) + ' ' + choice(items)

    return(mod, item)
