#!/user/bin/env python
# -*- coding: cp1252 -*-
# RIFTS Coalition char gen
# Created by Keith Marrs-Olson

#Global
IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE = 0,0,0,0,0,0,0,0,0,0,0,0,0
attack,inish,strike,roll,damage,roll,parry,dodge,horror =1,0,0,0,0,0,0,0,0
skills,race,OCC,Psionic,combat,equipment = [],[],[],[],[""],[]
hand = 1
RND="T"
PSkillNumb,SkillNumb=5,5
com,wep = 0,0 #Skill Counter
weapon = []
shawn=0
Char = ["IQ","ME","MA","PS","PP","PE","PB","Speed","HP","SDC","MDC","ISP","PPE","attack","inish","strike","roll","damage","roll","parry","dodge","skills","race","OCC","Psionic","weapon","combat","equipment","RND"]
stat = [IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,weapon,combat,equipment,RND]

def main():
    print ("Keith's RIFTS Pirate Character Generator")

        #Print()
##def Print():    
##    for i in range(len(Char)):
##        X = Char[i]
##        Y = stat[i]
##        #print "Charfields[",i,"]"
##        print (X, " = ", Y)
##        #print
##        #print "stats.",X,"=",X
##        #print X,"= stats.",X


main()
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

