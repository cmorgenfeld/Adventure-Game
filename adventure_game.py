from random import *
from time import *
from type import *
from item_generator import *


def intro():
    #Intro
    type("Cool Title")
    type("A production by...")
    type("Black Table Gaming Corp.")

    #Name adventurer. W/backstory --> Child kidnapped by Black Table, going to rescue them.
    type("Name your adventurer")
    name = input()

    type("As a young man, "+ name + " met the love of his life. They settled down in the small village \
of Villageville and had a young boy named Kristofferson. On his first birthday, Kristofferson was \
kidnapped by the shadowy orginazation known to a select few as the Concrete Fountain. The villagers \
of Villageville advised "+ name + " not to pursue the criminals, but to forget the incident. And he did.")
    sleep(0.75)
    type("20 years later...")
    sleep(0.75)
    type("As "+ name + " returned from a day of hard labor crafting wooden dice, he saw a crowd of \
Villageville villagers around his hut. His wife had been murdered by the Concrete Fountain! \
"+ name + " ran to the village leader for guidance.")
    type('"What should I do, O great village leader?", questioned '+ name + '.')
    type('"Follow your heart, young one.", he replied')
    type('"I will pay back the Concrete Fountain for all of the hardship in my life!", exclaimed ' + name + '.')
    type('"Take this pouch of our finest wooden dice, it should fetch a good price our neighboring town, \
Blackwater. Good luck on your quest, ' + name + ' you will bring Villageville much honor and glory! \
But first, look inside you and tell me your strengths and weaknesses."')

    return(name)

def attributes():
    strgth = 0
    spd = 0
    chrsma = 0
    hlth = 0
    type('*You have 4 major attributes; strength, speed, charisma, and constitution.*')
    type('*You have 20 points to allocate between the different attributes*')
    while not strgth + spd + chrsma + hlth == 20 or not 0 <= strgth <= 20 or not 0 <= spd <= 20 \
          or not 0 <= chrsma <= 20 or not 0 <= hlth <= 20:
        type("How much strength do you have? (0 - 10): ")
        strgth = int(input())
        type("How much speed do you have? (0 - 10): ")
        spd = int(input())
        type("How much charisma do you have? (0 - 10): ")
        chrsma = int(input())
        type("How much constitution do you have? (0 - 10): ")
        hlth = int(input())

        if not strgth + spd + chrsma + hlth == 20 or not 0 <= strgth <= 20 or not 0 <= spd <= 20 \
           or not 0 <= chrsma <= 20 or not 0 <= hlth <= 20:
            type("Make sure your total is 20 and no value is negative.")

    return(strgth, spd, chrsma, hlth)



weaponGenerator()
name = intro()
strgth, spd, chrsma, hlth = attributes()
with open('save_game.txt', 'w') as save:
    save.write(strgth)
    save.write(spd)
    save.write(chrsma)
    save.write(hlth)
with open('save_game.txt', 'r') as save:
    print(save.read())
