#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

# OCC Selection
print ("OCCselect.py")
title="OCCselect.py"
import easygui,random
import stats
stats.title=title
RND=stats.RND
def main():
        ImportStats()
        Select()
        #ExportStats()

def Select():
        global RND
        if stats.g == "G":
            msg = ("What kind of Data do you want?")
            title = ("OCCselect.py")
            choices = ("User Input", "Random", "Test")
            x = easygui.buttonbox(msg, title, choices)
            if x == "User Input":
                RND = "G"
                if stats.g == "G":
                    stats.hand = 99
            elif x == "Random":
                RND = "Y"
            elif x == "Test":
                RND = "T"
        if RND == "G":
                msg=("What kind of OCC do you want?")
                title=("OCCselect.py")
                choices=("User Input","Random","Test")
                x = easygui.buttonbox(msg, title, choices)
                if x == "User Input":
                    title = "Rifter 1.12 Gen"
                    choices = ['Pirate','Privateer',
                               'Coalition Dog Boy',
                               'Coalition "Dead Boy" Grunt',
                               'Coalition Military Specialist',
                               'Coalition Elite Robot Powered Armor (RPA)',
                               'Coalition Technical Officer',
                               ]

                    ##                """print "6 = Coalition Psi-Stalker"
                    ####                nazi = input ("Please choose your O.C.C. : ")     """
                    C = easygui.choicebox("Choose your character class", title, choices)

                elif x == "Random":
                    RND = "Y"
                elif x == "Test":
                    RND = "T"
        if RND == "T":
                 C = "Trogue"
        if RND =="N":

                choices =['Coalition Dog Boy',
                        'Vegabond','Pirate',
                        'Coalition "Dead Boy" Grunt'
                          ]
                if stats.IQ > 11 and stats.ME > 11 and stats.PE > 9:
                        choices.append('Coalition Military Specialist')
                if stats.IQ > 9 and stats.PP >9:
                        choices.append('Coalition Elite Robot Powered Armor (RPA)')
                if stats.IQ > 8:
                        choices.append('Coalition Technical Officer')
                if stats.IQ > 7 and stats.PS > 9:
                        choices.append('Privateer')
##                """print "6 = Coalition Psi-Stalker"
####                nazi = input ("Please choose your O.C.C. : ")     """
                C = easygui.choicebox ("Choose your character class", title, choices)
        if RND =="Y":
                z = random.randrange(1,101)
                if stats.IQ > 7 and stats.PS > 9:
                        z = random.randrange(50,101)
                if z == 1:
                    # import cat
                    C = "Trogue"
                    # import special
                if z != 1 and z <= 40:
                    C = "Vegabond"
                elif z > 40 and z <= 60:
                    C = "Pirate"
                elif z > 60:
                    C = 'Coalition "Dead Boy" Grunt'
                elif z == 100:
                    print("choice is Coalition Technical Officer OCC")
                    C == "Coalition Technical Officer"

        if C == "Trogue":
            import Trogue
        elif C == "Vegabond":
            print("choice is Vegabond OCC")
            import Vegabond
        elif C == "Pirate":
            print("choice is Pirate OCC")
            import Pirate
        elif C == 'Coalition "Dead Boy" Grunt':
            print('choice is Coalition "Dead Boy" Grunt OCC')
            import DBoy
        elif C == 100 or C == 'Coalition Dog Boy':
            print("choice is DogBoy OCC")
            import dogboy
        elif C == "Privateer":
            # requires 8 IQ & 10 PS
            print("choice is Privateer OCC")
            import Privateer
        elif C == "Coalition Military Specialist":
            # requires 8 IQ & 10 PS
            print("choice is Coalition Military Specialist OCC")
            import special
        elif C == "Coalition Technical Officer":
            # requires 8 IQ & 10 PS
            print("choice is Coalition Technical Officer OCC")
            import tech
        elif C == "Coalition Elite Robot Powered Armor (RPA)":
            # requires 8 IQ & 10 PS
            print("choice is Coalition Elite Robot Powered Armor (RPA) OCC")
            import sam
        else:
            print("No OCC selected")

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
    return IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment

main() # Calls main 
