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
title="Rifts Character Generator"
choices = ['Random', 'Test'] 
RNDYN = easygui.buttonbox (" Do you want to create character, randomize character creation, or run test code ", title="Rifts Character Generator", choices = ['Random', 'Test'] )
if RNDYN == 'Create':
    stats.RND="N" 
elif RNDYN == 'Random':
    stats.RND="Y"
elif RNDYN == 'Test':
    stats.RND="T"
#stats.RND="Y"

def main():
    x=1
    while x==1:
        errmsg = ""    
        rep = easygui.integerbox("how many times do you want to run the code")
        if rep == "":
                errmsg = ('"%s" is a required field.\n\n' % rep)
                easygui.msgbox(errmsg)
        if errmsg == "": x=0# no problems found
    n = 0
    while n != rep:
        n=n+1
        print ("character number %s" % n)
        if n == 1:
            import Rolls
            import OCCselect
            import skills
            import Weapon
            import combat
            import Print
        else:
            reload(Rolls)
            reload(OCCselect)
            reload(skills)
            reload(Weapon)
            reload(combat)
            reload(Print)
main()

    
    
