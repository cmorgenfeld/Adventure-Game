from random import *
from time import *
from type import *
from item_generator import *
from save_game import *
from monster_generator import *
from intro import *

class Player(object):
    def __init__(self, name, strgth, spd, chrsma, hlth):
        self.name = name
        self.strgth = strgth
        self.spd = spd
        self.chrsma = chrsma
        self.hlth = hlth
        self.lvl = 1
        
    def damageUpdate(self):
        self.damage = round(self.strgth * weapon_mod)


name, strgth, spd, chrsma, hlth = intro()
player = Player(name, strgth, spd, chrsma, hlth)
zone, lvl = zoneGenerator(player.lvl)
#Saves and loads game to save_game.txt
saveGame(strgth, spd, chrsma, hlth)
strgth, spd, chrsma, hlth = loadGame()
#Creates monster (Only has name and damage values tho)
dmg, name = monster_generator()
monster = Monster(name, dmg, dmg, dmg, player.lvl)
#Use in this order (Creates weapon and updates player's damage value)
#    |
#  \|/
"""weapon_mod, weapon = weaponGenerator()
player.damageUpdate()"""
