#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson
title="Rifts Pirate Gen",
# OCC Selection
print ("PirateSelect.py")
import easygui,random
import stats

def main():
        ImportStats()
        Select()
        #ExportStats()

def Select():
        if stats.RND =="N":

            choices = ['Vegabond','Pirate']
            if stats.IQ > 8 and stats.PS > 10:
                choices.append('Privateer')
                C = easygui.choicebox("Choose your Pirate class",title,choices)
        elif stats.RND =="Y" or stats.RND == "T":
                C = random.randrange(1,101)
                if stats.IQ > 7 and stats.PS > 9:
                        C = random.randrange(50,101)
        print ("random character # ",C)
        if C == 1 or C == "Trogue":
                print ("Test character chosen")
                import Trogue
        elif C != 1 and C <= 25 or C == "Vegabond":
                print("choice is Vegabond OCC")
                import Vegabond
        elif C > 25 and C < 75 or C == "Pirate":
                print("choice is Pirate OCC")
                import Pirate
        elif C >= 75 or C == "Privateer":
                print("choice is Privateer OCC")
                import Privateer
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
