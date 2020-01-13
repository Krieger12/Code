#!/user/bin/env python
# -*- coding: cp1252 -*
#rifts char gen
# Created by Keith Marrs-Olson

#Main code to run
'''
#easy gui skills.py
# need to work on cleaning easy gui in skills.py
# Test physical.py to make sure stats are correct
# add psychic abilities
# Coalition Soldgers
#   need to remove easygui messages for Coalition
#   input verification for numbers
'''
import easygui
import stats
title="Rifts Character Generator"
easygui.msgbox ("Welcom to Rifts Generator \n This code is still in in progress\n and probably will be for a long time")
choices = ['Create', 'Random', 'Test'] 
RNDYN = easygui.buttonbox (" Do you want to create character, randomize character creation, or run test code ", title, choices)
if RNDYN == 'Create':
    stats.RND="N" 
elif RNDYN == 'Random':
    stats.RND="Y"
elif RNDYN == 'Test':
    import g
##    choices = ['Create', 'Random', 'Test'] 
##    G = easygui.ynbox (" Do you want to enter Test mode? ", title,)
##    
##    if G == 0:
##        g = easygui.integerbox('Please input level',title, default=1)
##        stats.Level = g
##    if G == 1: stats.RND="T"
##
#stats.RND="T"

def main():
    import Rolls
    import OCCselect
    import skills
    import physical
    import Weapon
    import combat
    import Print
    raw_input("Press Enter to exit...")
    import cleanpyc
main()

    
    
