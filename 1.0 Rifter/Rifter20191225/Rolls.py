#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

import easygui, random
import stats
title="Rolls.py"


def main():
    #ImportStats()
    if stats.g == "G":
        import g
    if stats.RND == "N":
        ChoiceStats()
    elif stats.RND == "Y":
        RandomStats()
    elif stats.RND == "T":
        TestStats()
    #ExportStats()
    
def ChoiceStats():
    #global IQ,ME,MA,PS,PP,PE,PB,Speed,HP
    msg = "Enter your dice rolls 3d6 \n If you roll over 15 please add 1D6"
    fieldNames = ["Intelligence Quotient: ","Mental Endurance: ","Mental Affinity: ","Physical Strength: ","Physical Prowess: ","Physical Endurance: ","Physical Beauty: ","Speed: "]
    fieldValues = []  # we start with blanks for the values
    # make sure that none of the fields was left blank
    x=1
    while x==1:
        errmsg = ""    
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = ('"%s" is a required field.\n\n' % fieldNames[i])
                easygui.msgbox(errmsg)
        if errmsg == "": x=0# no problems found
    #records values
    stats.IQ = int(fieldValues[0])
    stats.ME = int(fieldValues[1])
    stats.MA = int(fieldValues[2])
    stats.PS = int(fieldValues[3])
    stats.PP = int(fieldValues[4])
    stats.PE = int(fieldValues[5])
    stats.PB = int(fieldValues[6])
    stats.Speed = int(fieldValues[7])
    while stats.HP == 0:
        stats.HP = easygui.integerbox("Please roll 1d6 for Hit Points")
    stats.HP=stats.HP+stats.PE
    
    #return IQ,ME,MA,PS,PP,PE,PB,Speed,HP
def RandomStats():
    #global IQ,ME,MA,PS,PP,PE,PB,Speed,HP
    stats.IQ = random.randrange(3,19)
    if stats.IQ > 15:
        stats.IQ = stats.IQ+random.randrange(1,7)
    stats.ME = random.randrange(3,19)
    if stats.ME > 15:
        stats.ME = stats.ME+random.randrange(1,7)
    stats.MA = random.randrange(3,19)
    if stats.MA > 15:
        stats.MA = stats.MA+random.randrange(1,7)
    stats.PS = random.randrange(3,19)
    if stats.PS > 15:
        stats.PS = stats.PS+random.randrange(1,7)
    stats.PP = random.randrange(3,19)
    if stats.PP > 15:
        stats.PP = stats.PP+random.randrange(1,7)
    stats.PE = random.randrange(3,19)
    if stats.PE > 15:
        stats.PE = stats.PE+random.randrange(1,7)
    stats.PB = random.randrange(3,19)
    if stats.PB > 15:
        stats.PB = stats.PB+random.randrange(1,7)
    stats.Speed = random.randrange(3,19)
    if stats.Speed > 15:
        stats.Speed=stats.Speed+random.randrange(1,7)
    stats.HP=stats.PE+random.randrange(1,7)
    #return IQ,ME,MA,PS,PP,PE,PB,Speed,HP
def TestStats():
    stats.IQ = 10
    stats.ME = 10
    stats.MA = 10
    stats.PS = 10
    stats.PP = 10
    stats.PE = 10
    stats.PB = 10
    stats.Speed = 10
    stats.HP = 10
def ExportStats():
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP
    stats.IQ = IQ
    stats.ME = ME
    stats.MA = MA
    stats.PS = PS
    stats.PP = PP
    stats.PE = PE
    stats.PB = PB
    stats.Speed = Speed
    stats.HP = HP
    
def ImportStats():
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP
    IQ = stats.IQ
    ME = stats.ME
    MA = stats.MA
    PS = stats.PS
    PP = stats.PP
    PE = stats.PE
    PB = stats.PB
    Speed = stats.Speed
    HP = stats.HP
    return IQ,ME,MA,PS,PP,PE,PB,Speed,HP
main()    

