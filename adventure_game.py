from random import *
from time import *
from type import *
from item_generator import *
from save_game import *
from monster_generator import *
from intro import *
from zone_generator import *

class Player(object):
    def __init__(self, name, strgth, spd, chrsma, hlth):
        self.name = name
        self.strgth = strgth
        self.spd = spd
        self.chrsma = chrsma
        self.hlth = hlth
        self.lvl = 1
        self.damage = self.strgth
        self.inventory = []
        
    def damageUpdate(self, drop, weapon_mod):
        if drop:
            self.damage = round(self.strgth * weapon_mod)
    def pickUp(self, drop, weapon):
        if drop:
            self.inventory.append(weapon)
        
#name, strgth, spd, chrsma, hlth = intro()
name, strgth, spd, chrsma, hlth = 'Katherine', 6, 4, 7, 3
player = Player(name, strgth, spd, chrsma, hlth)
zone, lvl, monsters = zoneGenerator(player.lvl)
type(zone)

#Creates monster (Drop is whether or not monster drops item)
name, dmg, spd, hlth, drop = monster_generator(player.lvl)
monster = Monster(name, dmg, spd, hlth, player.lvl)
monster.encounter()
#Use in this order (Creates weapon and updates player's damage value)
#   |
#  \|/

drop = True
weapon_mod, weapon = weaponGenerator(player.lvl)
player.damageUpdate(drop, weapon_mod)
player.pickUp(drop, weapon)
print(str(player.inventory)[2:-2])

#Saves and loads game to save_game.txt
saveGame(player.name, player.strgth, player.spd, player.chrsma, player.hlth, player.inventory)
player.name, player.strgth, player.spd, player.chrsma, player.hlth, player.inventory = loadGame()
type(str(player.inventory))
