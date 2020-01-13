#!/user/bin/env python
# -*- coding: cp1252 -*
#rifts char gen
# Created by Keith Marrs-Olson

#'Coalition "Dead Boy" Grunt'

import easygui
import stats
import random
title = "RIFTS RPA"
msg = "Please pick your skill"
def main():
    print ("RPA.py")
    ImportStats()
    elite()
    ExportStats()
def elite():
        global RND,PE,Speed,SDC,skills,race,OCC,PSkillNumb,SkillNumb,equipment
        if RND == "Y":
                SDC = random.randrange(1,5)
                stats.SDC = SDC*10
        if RND == "N":
                SDC = input ("Please roll 1d4 :")
                stats.SDC = SDC *10
        stats.OCC = 'Coalition Elite Robot Power Armor (RPA)'
        skills.append("O.C.C. Skills:")
        skills.append("Radio: Basic 55% +5")
        skills.append("Pilot Automobile 75% +5")
        skills.append("Pilot Hovercraft 65% +5")
        skills.append("Pilot Tank & APC 51% +4")
        skills.append("Robot Combat: Elite")
        skills.append("Read Sensory Equipment 45% +5")
        skills.append("Weapon Systems 50% +5")
        skills.append("Running")
        stats.PE=stats.PE+1
        if RND == "Y":
                x= random.randrange(4,17)
                stats.Speed=stats.Speed+x
                x= random.randrange(1,7)
                stats.SDC=stats.SDC+x
        if RND == "N":
                x = input ("Please roll 4d4 :")
                stats.Speed=stats.Speed+x
                x= input ("Please roll 1d6 :")
                stats.SDC=stats.SDC+x
                stats.SDC = stats.SDC *10
        #skills.append("Hand to Hand: Expert")
        stats.hand = 2
        weapon.append("W.P. Energy Pistol")
        weapon.append("W.P. Energy Rifle")
        #skills.append("W.P. of choice")
        stats.wep = 1
        #skills.append("Hand to Hand: Expert")

##        skills.append("Please select 10 more O.C.C. Related Skills")
##        skills.append("Please select 8 secondary skills")
        stats.PSkillNumb,stats.SkillNumb = 10,8
        equipment.append('Standard Equipment: Coalition "Dead Boy" body armor, energy rifle and energy sidearm of choice, four extra E-clips for each, two grenades, three signal flares, survival knife, utility belt, air filter and gas mask, walkie-talkie, uniform, combat boots, canteen, and additional non-energy weapon of choice. Conventional military vehicle of choice (motorcycle, jeep, hovercycle, etc.) for daily use and a SAMAS for field use only.')
        equipment.append("Money: The elite pilot gets a roof over his head, food, clothing, and all other basics provided free as part of his pay, as well as access to military facilities. Plus a monthly salary of 2000 credits. Starts off with one month's pay. The soldier's quarters is a nice dormitory arrangement shared by four individuals. Each gets a private bedroom/study complete with CD stereo system, television")
        return PE,Speed,SDC,skills,race,OCC,equipment
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
