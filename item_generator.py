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

    item = choice(items)

    print("You found a", qlty, item +"!")
