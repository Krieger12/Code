#!/user/bin/env python
# -*- coding: cp1252 -*
#rifts char gen
# Created by Keith Marrs-Olson

#'Coalition "Dead Boy" Grunt'

import easygui
import stats
import random
title = "RIFTS Coalition Military Specialist"
msg = "Please pick your skill"
def main():
    print ("special.py")
    ImportStats()
    special()
    ExportStats()
def special():
        if RND == "T":
            RND = "N"
        global RND,PE,Speed,SDC,skills,race,OCC,PSkillNumb,SkillNumb,equipment
        stats.OCC= ("Coalition Military Specialist")
        stats.SDC == 3
        import SDC
        skills.append("O.C.C. Skills:")
        skills.append("Radio: Basic 55% +5")
        skills.append("Literacy 50% +5%")
        skills.append("Computer Operation 45% +5")
        skills.append("Intelligence 42% +4")
        skills.append("Pilot Hovercraft 60% +5")
        skills.append("Robot Combat: Elite")
        skills.append("Read Sensory Equipment 40% +5")
        skills.append("Weapon Systems 50% +5")
        skills.append("Running")
        stats.PE=stats.PE+1
        print ("Speed = %d" % stats.Speed)
        print ("SDC = %d" % stats.SDC)
        if RND == "Y":
                x= random.randrange(4,17)
                stats.Speed=stats.Speed+x
                x= random.randrange(1,7)
                stats.SDC=stats.SDC+x
        if RND == "N":
                msg = "Running Bonuses"
                choices = [
                    "Speed +4d4",
                    "SDC +1d6"
                    ]
                sb = easygui.multenterbox(msg, title, choices)
                x=1
                while x==1:
                    errmsg = ""
                    for i in range(len(sb)):
                        if sb[i].strip =="":
                            errmsg = ('"%s" is a required field.\n\n' % fieldNames[i])
                            easygui.msgbox(errmsg)
                    if errmsg == "": x=0# no problems found  
                
                #x = input ("Please roll 4d4 :")
                stats.Speed=stats.Speed+int(sb[0])
                #x= input ("Please roll 1d6 :")
                stats.SDC=stats.SDC+int(sb[1])
        print ("SDC = %d" % stats.SDC)
        print ("Speed = %d" % stats.Speed)
        

        #skills.append("Hand to Hand: Expert")
        stats.hand = 2
        weapon.append("W.P. Energy Pistol")
        weapon.append("W.P. Energy Rifle")
        stats.PSkillNumb,stats.SkillNumb = 12,8
        skills.append("More info O.C.C. on 54")
        equipment.append('Standard Equipment: Coalition "Dead Boy" body armor, energy rifle and energy sidearm of choice, four extra E-clips for each, four grenades, three signal flares, survival knife, distancing binoculars, robot medical kit, disc recorder, pocket computer, utility belt, air filter and gas mask, walkie-talkie, uniform, combat boots, canteen, and additional non-energy weapon of choice. Conventional military vehicle of choice (motorcycle, jeep, hovercycle, etc.) for daily use and a Spider-skull Walker for field use only.')
        equipment.append("Money: The military specialist gets a roof over his head, food, clothing, and all other basics provided free as part of his pay, as well as access to military facilities. Plus a monthly salary of 2200 credits. Starts off with one month’s pay. The officer's quarters is a private apartment with a private bathroom, living room, bedroom/study complete with CD stereo system, personal computer, large screen television and VCD, mini-refrigerator, desk, dresser, and comfortable bed.")
        equipment.append("Cybernetics and bionics: Select two augmentations from cybernetics (any category) and one from bionics (optional) from the category of weapons or bionic appendage (hand and arm, leg, etc).")
        return PS,PE,Speed,SDC,skills,OCC,race,equipment
        return stats.Speed
def ExportStats():
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND
    stats.IQ = IQ
    stats.ME = ME
    stats.MA = MA
    stats.PS = PS
    stats.PB = PB
    stats.Speed = Speed
    stats.HP = HP
    stats.MDC = MDC
    stats.ISP = ISP
    stats.PPE = PPE
    stats.attack = attack
    stats.strike = strike
    stats.roll = roll
    stats.damage = damage
    stats.roll = roll
    stats.parry = parry
    stats.dodge = dodge
    stats.skills = skills
    stats.weapon = weapon
    stats.race = race
    stats.Psionic = Psionic
    stats.combat = combat
    stats.equipment = equipment
    
def ImportStats():
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,weapon,equipment,RND
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
    weapon = stats.weapon
    Psionic = stats.Psionic
    combat = stats.combat
    equipment = stats.equipment
    RND = stats.RND
    return IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND
main()
