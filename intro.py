from type import *
from time import *

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
    type('"What should I do, O great village leader?" questioned '+ name + '.')
    type('"Follow your heart, young one", he replied.')
    type('"I will pay back the Concrete Fountain for all of the hardship in my life!" exclaimed ' + name + '.')
    type('"Take this pouch of our finest wooden dice, it should fetch a good price at our neighboring town, \
Blackwater. Good luck on your quest, ' + name + ' you will bring Villageville much honor and glory! \
But first, look inside you and tell me your strengths and weaknesses."')

    #Variables given values so 'while' loop doesn't crash
    strgth = 0
    spd = 0
    chrsma = 0
    hlth = 0
    pnts = 20
    type('*You have 4 major attributes; strength, speed, charisma, and constitution.*')
    type('*You have 20 points to allocate between the different attributes*')
    while not pnts == 0 or not 0 <= strgth <= 10 or not 0 <= spd <= 10 \
          or not 0 <= chrsma <= 10 or not 0 <= hlth <= 10:
        type("How much strength do you have? (0 - 10): ")
        strgth = int(input())
        pnts -= strgth
        type("*You have " + str(pnts) + " points left to allocate*")
        type("How much speed do you have? (0 - 10): ")
        spd = int(input())
        pnts -= spd
        type("*You have " + str(pnts) + " points left to allocate*")
        type("How much charisma do you have? (0 - 10): ")
        chrsma = int(input())
        pnts -= chrsma
        type("*You have " + str(pnts) + " points left to allocate*")
        type("How much constitution do you have? (0 - 10): ")
        hlth = int(input())
        pnts -= hlth

        if not pnts == 0 or not 0 <= strgth <= 10 or not 0 <= spd <= 10 \
           or not 0 <= chrsma <= 10 or not 0 <= hlth <= 10:
            type("Make sure your total is 20 and no value is negative.")

    return(name, strgth, spd, chrsma, hlth)
