#!/user/bin/env python
# -*- coding: cp1252 -*
#rifts char gen
# Created by Keith Marrs-Olson

#'Coalition "Dead Boy" Grunt'

import easygui
import stats
import random
title = "RIFTS Dead Boy"
msg = "Please pick your skill"
def main():
    print ("DBoy.py")
    ImportStats()
    dead()
    ExportStats()
def dead():
        global RND,PS,PE,Speed,SDC,skills,OCC,race,PSkillNumb,SkillNumb,equipment
        stats.OCC = 'Coalition "Dead Boy" Grunt'
        stats.SDC = 3
        import SDC
        skills.append("O.C.C. Skills:")
        skills.append("Language: American 88% +1%/level")
        skills.append("Radio: Basic 55% +5")
        skills.append("Pilot Hovercraft 60% +5")
        skills.append("Pilot Tank & APC 50% +4")
        skills.append("Robot Combat: Basic")
        skills.append("Read Sensory Equipment 40% +5")
        skills.append("Weapon Systems 50% +5")
        skills.append("Body Building")
        stats.PS=stats.PS+2

        stats.SDC=stats.SDC+10

        skills.append("Climbing 45 +5%")
        skills.append("Running")
        stats.PE=stats.PE+1
        if RND == "Y" or RND == "T":
                x= random.randrange(4,17)
                stats.Speed=stats.Speed+x
                x= random.randrange(1,7)
                stats.SDC=stats.SDC+x
        if RND == "N":
                x=1
                while x==1:
                    choices = [
                        "Roll 4d4",
                        "Roll 1d6"
                    ]
                    errmsg = ""
                    sb = easygui.multenterbox("Running Bonuses", title, choices)
                    for i in range(len(sb)):
                        if sb[i].strip =="":
                            errmsg = ('"%s" is a required field.\n\n' % sb[i])
                            easygui.msgbox(errmsg)
                    if errmsg == "": x=0# no problems found
                    
                x = int(sb[0])
                stats.Speed=stats.Speed+x
                x = int(sb[1])
                stats.SDC=stats.SDC+x
        #skills.append("Hand to Hand: Expert")
        stats.hand = 2
        weapon.append("W.P. Energy Pistol")
        weapon.append("W.P. Energy Rifle")
        #skills.append("W.P. of choice")
        stats.wep = 2
        stats.PSkillNumb,stats.SkillNumb = 8,7
##        if RND == "Y":
##            PSkillNumb = 8
##            SkillNumb = 7
##            skills.append("Primary Skills:")
##            while PSkillNumb > 0:
##                SKILLS()
##                PSkillNumb = PSkillNumb - 1
##            skills.append(' ')
##            skills.append("Secondary Skills:")
##            while SkillNumb > 0:
##                SKILLS()
##                SkillNumb = SkillNumb - 1
##        if RND == "N":
##        skills.append("More info O.C.C. on 51")
##        skills.append("Please select 8  more O.C.C. Related Skills")
##        skills.append("Please select 7 secondary skills")
##        skills.append("Please refer to Rifts Main Book  pg 23")
##        skills.append("Or Ultimate Edition pg 305")
        race.append("More info on Coalition Grunt O.C.C. can be fount in the Main sourcebook page 51")
        equipment.append('Standard Equipment: Coalition "Dead Boy" body armor, energy rifle and energy sidearm of choice, four extra E-clips for each, two grenades, three signal flares, survival knife, utility belt, air filter and gas mask, walkie-talkie, uniform, combat boots, canteen, and additional non-energy weapon of choice. Equipment available upon assignment: Any weapon types, extra ammunition, Spider-skull Walker, Enforcer UAR-1, other robot vehicles, hovercraft (especially hovercycle), tank, jet pack, camera, disc recorder, optical enhancement, and food rations for weeks. Vehicle and equipment repair. Note: All weapons and equipment are given out on an as needed basis, with the commanding officer deciding whether or not the item(s) is really necessary or not. If the officer doesn\'t like the character(s), the availability of items may be extremely limited.')
        equipment.append("Money: The grunt gets a roof over his head, food, clothing, and all other basics provided free as part of his pay, as well as military facilities. Plus a monthly salary of 1700 credits. Starts off with one month's pay. The soldier's quarters is a nice dormitory arrangement shared by four individuals. Each gets a private bedroom/study complete with CD stereo system, television and VCD, mini-refrigerator, desk, dresser, and comfortable bed.")
        return PS,PE,Speed,SDC,skills,OCC,race,equipment
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
