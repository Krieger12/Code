#!/user/bin/env python
# -*- coding: cp1252 -*
#rifts char gen
# Created by Keith Marrs-Olson

#Main code to run

#easy gui skills.py
#need to change easygui messages in selection screen especially on skills
# Bug saying you have no skills when selecting dropdown
# vague dropdown on second skill list


import easygui
import stats
title="Rifts Character Generator"

easygui.msgbox ("Welcom to Rifts Generator \n This code is still in beta testing")
RNDYN = easygui.buttonbox (" Do you want to create character, randomize character creation, or run test code ", title, choices = ['Create', 'Random', 'Test'] )
if RNDYN == 'Create':
    stats.RND="N" 
elif RNDYN == 'Random':
    stats.RND="Y"
elif RNDYN == 'Test':
    stats.RND="T"
#stats.RND="Y"

def main():
    choices = ["Animalistic Predator"]#, "Intelligent Monster"]
    monster = easygui.buttonbox (" Do you want to create monster or randomize monster creation? ", title, choices)
    if monster == choices[0]:
        print choices[0]
        pet()
    elif monster == choices[1]:
        print choice[1]
        supernatural()
    else:
        print choices[2]
        char()
def Char():
    print ("still need to implement")
##    import Rolls
##    import OCCselect
##    import skills
##    import Weapon
##    import combat
##    import Print
##    
def pet():
    stats.OCC="Animalistic Predator"
    import Monster
    import MPrint
def supernatural():
    stats.OCC= "Intelligent Supernatural Monster"
    import supernatural
    import Print
main()

    
    
