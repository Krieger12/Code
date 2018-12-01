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


easygui.msgbox ("Welcom to Rifts Generator \n This code is still in beta testing")
RNDYN = easygui.buttonbox (" Do you want to create character, randomize character creation, or run test code ", title="Rifts Character Generator", choices = ['Create', 'Random', 'Test'] )
if RNDYN == 'Create':
    stats.RND="N" 
elif RNDYN == 'Random':
    stats.RND="Y"
elif RNDYN == 'Test':
    stats.RND="T"
#stats.RND="Y"

def main():
    import Rolls
    import OCCselect
    import skills
    import Weapon
    import combat
    import Print
    raw_input("Press Enter to exit...")
main()

    
    
