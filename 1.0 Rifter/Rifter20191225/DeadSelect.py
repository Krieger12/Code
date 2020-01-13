#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

# OCC Selection
print ("DeadSelect.py")

import easygui,random
import stats

def main():
        ImportStats()
        Select()
##        loop="loopit"
##        while loop!=0:
##                Select(loop)
##                print loop
        #ExportStats()


def Select():
##        if stats.RND == "T":
##                C = 
        if stats.RND =="N"or stats.RND=="T":

                title='Coalition Soldier O.C.C.s "Dead Boys"'
                choices =['Coalition Dog Boy',
                        'Coalition "Dead Boy" Grunt'
                          ]
                if stats.IQ > 11 and stats.ME > 11 and stats.PE > 9:
                        choices.append('Coalition Military Specialist')
                if stats.IQ > 9 and stats.PP >9:
                        choices.append('Coalition Elite Robot Powered Armor (RPA)')
                if stats.IQ > 8:
                        choices.append('Coalition Technical Officer')
                """print "6 = Coalition Psi-Stalker"
##                nazi = input ("Please choose your O.C.C. : ")     """
                C = easygui.choicebox ("Choose your character class", title, choices)
        elif stats.RND =="Y":
                if stats.IQ > 11 and stats.ME > 11 and stats.PE > 9:
                        C = random.randrange(3,6)
                if stats.IQ > 9 and stats.PP >9:
                        C = random.randrange(1,5)
                if stats.IQ > 8:
                        C = random.randrange(1,4)
                else:
                        C = random.randrange(1,3)
        print ("random character # ",C)
        if C == 1 or C == 'Coalition Dog Boy':
                print("choice is Coalition Dog Boy OCC")
                import dogboy
        elif C == 2 or C == 'Coalition "Dead Boy" Grunt':
                print('Choice is Coalition "Dead Boy" Grunt OCC')
                import DBoy
        elif C == 3 or C == 'Coalition Technical Officer':
                print("choice is Coalition Technical Officer OCC")
                #if stats.IQ > 8:
                import tech
        elif C == 4 or C == 'Coalition Elite Robot Powered Armor (RPA)':
                print("choice is Coalition Elite Robot Powered Armor (RPA) OCC")
                #if stats.IQ > 9 and stats.PP >9:
                import sam
        elif C == 5 or C == "Coalition Military Specialist":
                print("choice is Coalition Military Specialist OCC")
                #if stats.IQ > 11 and stats.ME > 11 and stats.PE > 9:
                import special
        elif C == 7 or C == 'Coalition Technical Officer':
                print("choice is Coalition Technical Officer OCC")
                #if stats.IQ > 8:
                import tech
        elif C == 6 or C == 'Coalition Dog Boy':
                print("choice is Coalition Dog Boy OCC")
                import dogboy

        else :
                print ("No OCC selected")

def ExportStats():
    stats.IQ = IQ
    stats.ME = ME
    stats.MA = MA
    stats.PS = PS
    stats.PP = PP
    stats.PE = PE
    stats.PB = PB
    stats.Speed = Speed
    stats.HP = HP
    stats.SDC = SDC
    stats.MDC = MDC
    stats.ISP = ISP
    stats.PPE = PPE
    stats.attack = attack
    stats.inish = inish
    stats.strike = strike
    stats.roll = roll
    stats.damage = damage
    stats.roll = roll
    stats.parry = parry
    stats.dodge = dodge
    stats.skills = skills
    stats.race = race
    stats.OCC = OCC
    stats.Psionic = Psionic
    stats.weapon = weapon
    stats.combat = combat
    stats.equipment = equipment
    stats.RND = RND
    
def ImportStats():
    IQ = stats.IQ
    ME = stats.ME
    MA = stats.MA
    PS = stats.PS
    PP = stats.PP
    PE = stats.PE
    PB = stats.PB
    Speed = stats.Speed
    HP = stats.HP
    SDC = stats.SDC
    MDC = stats.MDC
    ISP = stats.ISP
    PPE = stats.PPE
    attack = stats.attack
    inish = stats.inish
    strike = stats.strike
    roll = stats.roll
    damage = stats.damage
    roll = stats.roll
    parry = stats.parry
    dodge = stats.dodge
    skills = stats.skills
    race = stats.race
    OCC = stats.OCC
    Psionic = stats.Psionic
    combat = stats.combat
    equipment = stats.equipment
    RND = stats.RND
    return IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND

main() # Calls main 
