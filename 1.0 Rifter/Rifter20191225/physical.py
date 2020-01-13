#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson
# THis is the physical skill selection of Rifts Chacters.

import easygui, stats, random


#PHYSICAL Skills section

import easygui, random, stats
print "physical.py"
title="physical.py"
#if stats.g=="G": import g
RND = stats.RND#"N"
if stats.g == "G":
    msg = ("What kind of Data do you want?")

    choices = ("User Input", "Random", "Test")
    x = easygui.buttonbox(msg, title, choices)
    if x == "User Input":
        RND = "N"
    elif x == "Random":
        RND = "Y"
    elif x == "Test":
        RND = "T"
skills=stats.skills
shawn = stats.shawn
msg = ("Please pick Physical your skill")
print shawn
def main():
    global RND
    ImportStats()
    phy = stats.phy
    Print()
    if phy > 0: skills.append("Physical Skills Selected")
    while phy > 0:
        print("%d Physical skill of choice" % phy)
        selection()
        phy=phy-1
    ##    global RND,skills,PS,PP,PE,SDC,Speed,dodge,attack
    ExportStats()
    print("stats.SDC")
    print("stats.PS")
    print("stats.PP")
    print("stats.PE")
    print("stats.Speed")
    print("stats.parry")
    print("stats.dodge")
    print("stats.roll")
    skills.append("")
def Print():
    print(stats.SDC)
    print(stats.PS)
    print(stats.PP)
    print(stats.PE)
    print(stats.Speed)
    print(stats.parry)
    print(stats.dodge)
    print(stats.roll)
def ImportStats():
    skills=stats.skills
def ExportStats():
    global skills
    #print skills
    stats.skills=skills
    stats.shawn=shawn
def selection():
    global skills,RND
    title = ("Physical.py")
    if RND == "Y":
        x = random.randrange(1,18)
    if RND == "T":
        count=+1
        x = "Physical Labor"
        print("stats.shawn = %s" % stats.shawn)
        #if stats.shawn > 4: easygui.msgbox("Shawn you are a cheater!!!")
        x = random.randrange(1, 18)
    if RND == "N":
        if stats.shawn > 4 and stats.g != "G": easygui.msgbox("Shawn you are a cheater!!!")
        msg = ("Please pick your Physical skill")
        choices = ["Acrobatics", "Athletics", "Aerobic Athletics", "Body Building & Weight Lifting", "Boxing", "Climbing", "Fencing", "Forced March", "Gymnastics", "Juggling", "Kick Boxing", "Outdoorsmanship", "Physical Labor", "Prowl", "Running", "Swimming", "S.C.U.B.A", "Wrestling"]
        x = easygui.choicebox(msg,title,choices)
##        print
##        print "1 - Acrobatics"
##        print "2 - Athletics"
##        print "3 - Aerobic Athletics"
##        print "4 - Body Building & Weight Lifting"
##        print "5 - Boxing"
##        print "6 - Climbing"
##        print "7 - Fencing"
##        print "8 - Forced march"
##        print "9 - Gymnastics"
##        print "10 - Juggling"
##        print "11 - Kick Boxing"
##        print "12 - Outdoorsmanship"
##        print "13 - Physical Labor"
##        print "14 - Prowl"
##        print "15 - Running"
##        print "16 - Swimming"
##        print "17 - S.C.U.B.A"
##        print "18 - Wrestling"
##        x = input(" Please enter Skill: ")
    if x ==1 or x =="Acrobatics":
        skills.append("Acrobatics:")
        skills.append("     Automatic kick attack at first level; IDS damage.")
        skills.append("     60% +5% per level — Sense of balance")
        skills.append("     60% + 3% per level — Walk tightrope or high wire")
        skills.append("     80% + 2% per level — Climb rope")
        skills.append("     60% +5% per level — Back flip")
        skills.append("     40% base climb ability or adds a + 15% to climb skill.")
        skills.append("     30% base prowl ability or adds a +5% to prowl skill")
        stats.roll=stats.roll+2
        stats.PS=stats.PS+1
        stats.PP=stats.PP+1
        stats.PE=stats.PE+1
        if RND == "Y":
            z = random.randrange(1,7)
        if RND == "T":
            z = 1
        if RND == "N":
            msg = "SDC increase roll 1d6"
            z = easygui.enterbox(msg,title,"")
        stats.SDC=stats.SDC+int(z)
    elif x == 2 or x =="Athletics":
        skills.append("Athletics")
        stats.parry=stats.parry+1
        stats.dodge=stats.dodge+1
        stats.roll=stats.roll+1
        stats.PS=stats.PS+1
        if RND == "T":
            stats.Speed=stats.Speed+1
            stats.SDC=stats.SDC+1
        if RND == "Y":
            z = random.randrange(1,7)
            stats.Speed=stats.Speed+x
            z = random.randrange(1,9)
            stats.SDC=stats.SDC+z
        if RND == "N":
            fieldNames = ["Speed increase Roll 1d6","SDC increase Roll 1d8"]
            fieldValues = []  # we start with blanks for the values
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
            stats.Speed=stats.Speed+int(fieldValues[0])
            stats.SDC=stats.SDC+int(fieldValues[0])
    elif x == 3 or x == "Aerobic Athletics":
        skills.append("Aerobic Athletics")
        if RND == "T": z = 1
        if RND == "Y":
            z = random.randrange(2,9)
        if RND == "N":
            msg = "SDC increase roll 2d4"
            z = easygui.enterbox(meg,title,"")
        stats.SDC=stats.SDC+int(z)
    elif x == 4 or x == "Body Building & Weight Lifting":
        skills.append("Body Building & Weight Lifting")
        stats.PS=stats.PS+2
        stats.SDC=stats.SDC+10
    elif x == 5 or x == "Boxing":
        skills.append("Boxing")
        stats.attack=stats.attack+1
        stats.parry=stats.parry+2
        stats.dodge=stats.dodge+2
        stats.roll=stats.roll+1
        stats.PS=stats.PS+2
        if RND == "T":
            z = 1
        if RND == "Y":
            z = random.randrange(3,19)
        if RND == "N":
            msg = "SDC increase roll 3d6"
            z = easygui.enterbox(meg,title,"")
        stats.SDC=stats.SDC+int(z)
    elif x == 6:
        skills.append("Climbing 40% +5")                      
    elif x == 7:
        skills.append("Fencing")
        skills.append("	    requires W.P. Sword (W.P. Knife optional)")
        skills.append("     +1 strike/ perry with sword or dagger")
        skills.append("     +1d6 damage with sword")
    elif x == 8:
        skills.append("Forced march")
        stats.PE=stats.PE+2
        if RND == "T":
            stats.Speed=stats.Speed+1
            stats.SDC=stats.SDC+1
        if RND == "Y":
            z = random.randrange(1,4)
            stats.Speed=stats.Speed+z
            z = random.randrange(2,12)
            stats.SDC=stats.SDC+z
        if RND == "N":
            msg = "Speed increase roll 1d4"
            z = easygui.enterbox(meg,title,"")
            stats.Speed=stats.Speed+z
            msg = "SDC increase roll 2d6"
            z = easygui.enterbox(meg,title,"")

            stats.SDC=stats.SDC+z
    elif x == 9:
        skills.append("Gymnastics")
        skills.append("    Automatic kick attack at first level; 2D4 damage.")
        skills.append("    50% + 5% per level — Sense of balance")
        skills.append("    60% + 3% per level — Work parallel bars & rings")
        skills.append("    70% + 2% per level — Climb rope")
        skills.append("    70% + 5% per level — Back flip")
        skills.append("    25% base climb ability or adds a +7% to climb skill.")
        skills.append("    30% base prowl ability or adds a +5% to prowl skill.")
        stats.roll=stats.roll+2
        stats.PS=stats.PS+2
        stats.PE=stats.PE+2
        stats.PP=stats.PP+1        
        if RND == "T":
            z = 1
        if RND == "Y":
            z = random.randrange(2,12)
        if RND == "N":
            z= input ("please Roll 2d6")
        stats.SDC=stats.SDC+z
    elif x == 10:
        skills.append("Juggling 35% +5")
    elif x == 11:
        skills.append("Kick Boxing")
        stats.PE=stats.PE+1
        stats.PS=stats.PS+1
        if RND == "T":
            z = 1
        if RND == "Y":
            z = random.randrange(1,10)
        if RND == "N":
            msg = ("SDC increase roll 1d10")
            z = easygui.enterbox(meg,title,"")
        stats.SDC=stats.SDC+z
        skills.append(" Round House Kick 3d6")
        skills.append(" Axe Kick 2d8")
        skills.append(" Knee Strike 1d8")
        skills.append(" Leap Kick 3d8 (counts as two melee attacks)")
    elif x == 12:
        skills.append("Outdoorsmanship")
        skills.append(" Requires Wilderness Survival")
        skills.append(" +5 Wilderness Survival Skill")
        stats.PE=stats.PE+1
        if RND == "T":
            z = 1
        if RND == "Y":
            z = random.randrange(2,12)
        if RND == "N":
            msg = ("SDC increase roll 2d6")
            z = easygui.enterbox(msg,title, "")
        stats.SDC=stats.SDC+int(z)
    elif x == 13 or x == "Physical Labor":
        skills.append("Physical Labor")
        stats.PS=stats.PS+2
        stats.PE=stats.PE+1
        if RND == "T": z=1
        if RND == "Y":
            z = random.randrange(2,16)
        if RND == "N":
            msg = "SDC increase roll 2d8"
            z = easygui.enterbox(meg,title,"")
        stats.SDC=stats.SDC+int(z)
    elif x == 14:
        skills.append("Prowl 25% + 5%")
    elif x == 15:
        skills.append("Running")
        stats.PE=stats.PE+1
        if RND == "T":
            x = 4
            y = 1
        if RND == "Y":
            x = random.randrange(4,17)
            y = random.randrange(1,7)
        #Multi enter box
        if RND == "N":
            fieldNames = ["Speed increase Roll 4d4","SDC increase Roll 1d6"]
            fieldValues = []  # we start with blanks for the values
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
            stats.Speed=stats.Speed+int(fieldValues[0])
            stats.SDC=stats.SDC+int(fieldValues[0])
            #reset x,y values
            x,y = 0,0
        stats.SDC=stats.SDC+y
        stats.Speed=stats.Speed+x
    elif x == 16:
        skills.append("Swimming 50% +5")
    elif x == 17:
        skills.append("S.C.U.B.A 50% +5")
    elif x == 18:
        skills.append("Wrestling")
        skills.append(" Body block/tackle does 1D4 damage and the opponent must dodge or parry to avoid being knocked down (lose one melee attack if knocked down).")
        skills.append(" Pin/incapacitate on a roll of 18, 19, or 20.")
        skills.append(" Crush/squeeze does 1D4 damage per squeeze attack.")
        stats.roll=stats.roll+1
        stats.PS=stats.PS+2
        stats.PE=stats.PE+1
        if RND == "T":
            z = 1
        if RND == "Y":
            z = random.randrange(4,25)
        if RND == "N":
            msg = "SDC increase roll 4d6"
            z = easygui.enterbox(meg,title,"")
        stats.SDC=stats.SDC+int(z)
    else:
        print("Error: No Physical skill selected ")
    return skills
    
##    
main()
