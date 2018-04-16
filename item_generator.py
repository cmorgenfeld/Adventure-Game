from random import *
from type import *

def weaponGenerator():
    dmgMod = {
        "Bad" : 0.9,
        "Normal" : 1,
        "Good" : 1.1,
    }
    qlty = choice(list(dmgMod.keys()))
    mod = dmgMod[qlty]

    items = ['Mace', 'Bow', 'Sword', 'Armor', 'Helmet', 'Shield']

    item = choice(items)

    print("You found a", qlty, item +"!")
