#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith
# "Please refer to Rifts Main Book  pg 23"
# "Or Ultimate Edition pg 305"

#Skills section
print ("skills.py")

import easygui, random
import stats
title="skills.py"
stats.title=title
skills=stats.skills

RND = stats.RND
if stats.g == "G":
    msg = ("What kind of Data do you want?")

    choices = ("User Input", "Random", "Test")
    x = easygui.choicebox(msg, title, choices)
    if x == "User Input":
        RND = "N"
    elif x == "Random":
        RND = "Y"
    elif x == "Test":
        RND = "T"
shawn = stats.shawn
msg = "Please pick your skill"
def main():
    global RND
    ImportStats()
    skills.append(" ")
    skills.append("OCC Related Skills")
    OCC = stats.OCC
    if OCC == "Pirate":
        x = 3
        while x > 0:
            print ("Pirate skill %d") % x
            x=x-1
            PirateSKILLS()

    PSkillNumb = stats.PSkillNumb
    while PSkillNumb > 0:
        print ("Primary Skill %d") % PSkillNumb
        z = ("Please pick your Primary skills you have %s skills to pick") % PSkillNumb
        PSkillNumb = PSkillNumb - 1
        SKILLS(z)
    SkillNumb = stats.SkillNumb
    skills.append(" ")
    skills.append("Secondary Skill")
    while SkillNumb > 0:
        print ("Secondary Skill %d") % SkillNumb
        z = ("Please pick your skills you have %s skills to pick") % SkillNumb
        SkillNumb = SkillNumb - 1
        SKILLS(z)
    #SKILLS()
    skills.append(" ")

    ExportStats()
##    n = len(skills)
##    for r in range(0,n):
##        print (r, skills[r])
##    
def ImportStats():
    skills=stats.skills
def ExportStats():
    global skills,hand
    stats.skills=skills
    stats.shawn=shawn
def SKILLS(z):
    global RND,shawn,SkillNumb,skills#code test
    if RND == "T":
        s = "PHYSICAL"
    if RND == "Y":
        s = random.randrange(1,18)
    if RND  == "N":
        msg = z
        choices = ["COMMUNICATIONS", "DOMESTIC", "ELECTRICAL", "ESPIONAGE", "LANGUAGE", "LORE", "MECHANICAL", "MEDICAL", "MILITARY", "PHYSICAL", "PILOT SKILLS", "PILOT RELATED SKILLS", "ROGUE SKILLS", "SCIENCE", "TECHNICAL", "WEAPON PROFICIENCIES", "WILDERNESS", "Upgrade Combat Skills" ]
        s = easygui.choicebox(msg,title,choices)
    if s == 1 or s == "COMMUNICATIONS":
        COMMUNICATIONS()
    elif s == 2 or s == "DOMESTIC":
        DOMESTIC()
    elif s == 3 or s == "ELECTRICAL" :
        ELECTRICAL()
    elif s == 4 or s == "ESPIONAGE":
        ESPIONAGE()
    elif s == 5 or s == "LANGUAGE":
        LANGUAGE()
    elif s == 6 or s == "LORE":
        LORE()
    elif s == 7 or s == "MECHANICAL":
        MECHANICAL()
    elif s ==8 or s == "MEDICAL":
        MEDICAL()
    elif s == 9 or s == "MILITARY":
        MILITARY() 
    elif s == 10 or s == "PHYSICAL":
        shawn = shawn + 1
        print ("shawn=",shawn)
        print ("Physical Skill")
        if RND == "N": easygui.msgbox("Physical skill added \n Physical will be seleced later")
        skills.append("Physical Skill")
        stats.phy = stats.phy + 1
    elif s == 11 or s == "PILOT SKILLS":
        PILOTSKILLS()
    elif s == 12 or s == "PILOT RELATED SKILLS":
       PILOTRELATED()
    elif s == 13 or s == "ROGUE SKILLS":
       ROGUESKILLS()
    elif s == 14 or s == "SCIENCE":
       SCIENCE()
    elif s == 15 or s == "TECHNICAL":
       TECHNICAL()
    elif s == 16 or s == "WEAPON PROFICIENCIES":
            #WEAPON()
            #import Weapon
            print ("Weapon")
            if RND == "N": easygui.msgbox("Weapon skill added \n Weapons will be seleced later")
            skills.append ("Weapon")
            stats.wep = stats.wep+1
##            if stats.wep == 0:
##                import Weapon
##            elif stats.wep > 0:
##                reload(Weapon)
    elif s == 17 or s == "WILDERNESS":
        WILDERNESS()
    elif s == "Upgrade Combat Skills":
            stats.com = stats.com+1
            stats.combat = "SELECT"
            if stats.com == 1:
                import combat
            elif stats.com > 1:
                reload (combat)
            print ("Upgrade Combat Skills")
    return shawn,skills

def COMMUNICATIONS():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,15)
    if RND == "N":
        msg = "Please pick your skill"
        choices = ["Barter", "Creative Writing", "Cryptography", "Electronic Countermeasures", "Laser Communications", "Optic Systems", "Perforamnce", "Public Speaking", "Radio: Basic", "Radio: Scramblers", "Sensory Equipment", "Singing", "Surveillance System", "TV/Video"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x =="Barter":
        skills.append("Barter 30% + 4")
    elif x == 2 or x =="Creative Writing":
        skills.append("Creative Writing 25% +5")
    elif x == 3 or x =="Cryptography":
        skills.append("Cryptography 25% +5")
    elif x == 4 or x =="Electronic Countermeasures":
        skills.append("Electronic Countermeasures 30% +5")
    elif x == 5 or x =="Laser Communications":
        skills.append("Laser Communication 30% +5")
    elif x == 6 or x =="Optic Systems":
        skills.append("Optic Systems 30% +5")
    elif x == 7 or x =="Perforamnce":
        skills.append("Perforamnce 30% +5")
    elif x == 8 or x =="Public Speaking":
        skills.append("Public Speaking 30% +5")
    elif x == 9 or x =="Radio: Basic":    
        skills.append("Radio: Basic 45% +5")
    elif x == 10 or x =="Radio: Scramblers":
        skills.append("Radio: Scramblers 35% +5")
    elif x == 11 or x =="Sensory Equipment":
        skills.append("Sensory Equipment 30% +5")
    elif x == 12 or x =="Singing":
        skills.append("Singing 35% +5")
    elif x == 13 or x =="Surveillance System":
        skills.append("Surveillance Systems 30%+5")
    elif x == 14 or x =="TV/Video":
        skills.append("T.V./Video 35% +4")
    else:
        SKILLS()
    return skills

def DOMESTIC():
    global skills,RND
    if RND == "Y":
        x = random.randrange(1,12)
    if RND == "N":
        choices = ["Brewing","Cooking","Danceing","Fishing","Gardening","Housekeeping","Play Musical Instrument","Recycle","Sewing","Singing","Wardrobe & Grooming"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Brewing":
        skills.append("Brewing 25/30% +5")
    elif x == 2 or x == "Cooking":
        skills.append("Cooking 35% +5")
    elif x == 3 or x == "Danceing":
        skills.append("Danceing 30% +5")
    elif x == 4 or x == "Fishing":
        skills.append("Fishing 35% +5")
    elif x == 5 or x == "Gardening":
        skills.append("Gardening 36% +4")
    elif x == 6 or x == "Housekeeping":
        skills.append("Housekeeping 35% +5")
    elif x == 7 or x == "Play Musical Instrument":
        skills.append("Play Musical Instrument 35% +5")
    elif x == 8 or x == "Recycle":
        skills.append("Recycle 30% +5")
    elif x == 9 or x == "Sewing":
        skills.append("Sewing 40% +5")
    elif x == 10 or x == "Singing":
        skills.append("Singing 35% +5")
    elif x == 11 or x == "Wardrobe & Grooming":
        skills.append("Wardrobe & Grooming 50% +4")
    else:
        SKILLS()
    return skills

def ELECTRICAL():
    global skills,RND
    if RND == "Y":
        x = random.randrange(1,6)
    if RND == "N":
        choices = ["Basic Electronics","Computer Repair","Electrical Engineer","Electricity Generation","Robot Electronics"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Basic Electronics":
        skills.append("Basic Electronics 30% +5")
    elif x == 2 or x == "Computer Repair":
        skills.append("Computer Repair 25% +5")
    elif x == 3 or x == "Electrical Engineer":
        skills.append("Electrical Engineer 30% +5")
        skills.append(" requires Advances mathematics and Literacy")
    elif x == 4 or x == "Electricity Generation":
        skills.append("Electricity Generation 50% +5")
        skills.append(" requires Basic mathematics, Basic Electronics and Basic Mechanics")
    elif x == 5 or x == "Robot Electronics":
        skills.append("Robot Electronics 30% +5")
        skills.append(" requires Electrical Engineering and Computer Science")
    else:
        SKILLS()
    return skills

def ESPIONAGE():
    global skills,RND#,strike
    if RND == "Y":
        x = random.randrange(1,15)
    if RND == "N":
        choices = ["Detect Ambush","Detect Concealment","Disguise","Disguise","Escape Artist","Forgery","Impersonation","Intelligence","Interrogation","Pick Locks","Pick Pockets","Sniper","Tracking (people)","Undercover Ops","Wilderness Survival"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Detect Ambush":
        skills.append("Detect Ambush 30% +5")
    elif x == 2 or x == "Detect Concealment":
        skills.append("Detect Concealment 25% +5")
    elif x == 3 or x == "Disguise":
        skills.append("Disguise 25% +5")
    elif x == 4 or x == "Escape Artist":
        skills.append("Escape Artist 30% +5")
    elif x == 5 or x == "Forgery":
        skills.append("Forgery 20% +5")
    elif x == 6 or x == "Intelligence":
        skills.append("Intelligence 32% +4")
    elif x == 7 or x == "Impersonation":
        skills.append("Impersonation 30/16% +4")
    elif x == 8 or x == "Interrogation":
        skills.append("Interrogation 30% +5")
    elif x == 9 or x == "Pick Locks":
        skills.append("Pick Locks 30% +5")
    elif x == 10 or x == "Pick Pockets":
        skills.append("Pick Pockets 25% +5")
    elif x == 11 or x == "Sniper":
        skills.append("Sniper +2 strike on aimed shot")
	#strike=strike+2
    # Add Strike
    elif x == 12 or x == "Tracking (people)":
        skills.append("Tracking (people) 25% +5")
    elif x == 13 or x == "Undercover Ops":
        skills.append("Undercover Ops 30% +5")
    elif x == 14 or x == "Wilderness Survival":
        skills.append("Wilderness Survival 25% +5")
    else:
        SKILLS()
    return skills,#,strike

def LANGUAGE():
    global RND
    if RND == "Y":
        x = random.randrange(1,3)
    if RND == "N":
        x = easygui.buttonbox ("Please select if you want the skill: ", title="Rifts Character Generator", choices = ['Spoken', 'Written'])
    if x == 1 or x == "Spoken":
        speak()
    elif x == 2 or x == "Written":
        write()
    else:
        SKILLS()
def speak():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,14)
    if RND == "N":
        choices = ["American","Techno-Can","Spanish","Japanese","Chinese","Euro","Draganese/Elven","Gobblely","Faerie Speak","Demongogian","Russian","Mongolian","Rogues Cant"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "American":
        skills.append("Language: American 50% +3")
    elif x == 2 or x == "Techno-Can":
        skills.append("Language: Techno-Can 50% +3")
    elif x == 3 or x == "Spanish":
        skills.append("Spanish 50% +3")
    elif x == 4 or x == "Japanese":
        skills.append("Japanese 50% +3")
    elif x == 5 or x == "Chinese":
        skills.append("Chinese 50% +3")
    elif x == 6 or x == "Euro":
        skills.append("Euro 50% +3")
    elif x == 7 or x == "Draganese/Elven":
        skills.append("Draganese/Elven 50% +3")
    elif x == 8 or x == "Gobblely":
        skills.append("Gobblely 50% +3")
    elif x == 9 or x == "Faerie Speak":
        skills.append("Faerie Speak 50% +3")
    elif x == 10 or x == "Demongogian":
        skills.append("Demongogian 50% +3")
    elif x == 11 or x == "Russian":
        skills.append("Russian 50% +3")
    elif x == 12 or x == "Mongolian":
        skills.append("Mongolian 50% +3")
    elif x == 13 or x == "Rogues Cant":
        skills.append("Rogues Cant 30% +5")
    else:
        SKILLS()
    return skills
def write():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,14)
    if RND == "N":
        choices = ["American","Techno-Can","Spanish","Japanese","Chinese","Euro","Draganese/Elven","Gobblely","Faerie Speak","Demongogian","Pogues Cant","Russian","Mongolian","Rogues Cant"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "American":
        skills.append("American 30% +5")
    elif x == 2 or x == "Techno-Can":
       skills.append("Techno-Can 30% +5")
    elif x == 3 or x == "Spanish":
       skills.append("Spanish 30% +5")
    elif x == 4 or x == "Japanese":
        skills.append("Japanese 30% +5")
    elif x == 5 or x == "Chinese":
        skills.append("Chinese 30% +5")
    elif x == 6 or x == "Euro":
        skills.append("Euro 30% +5")
    elif x == 7 or x == "Draganese/Elven":
        skills.append("Draganese/Elven 30% +5")
    elif x == 8 or x == "Gobblely":
       skills.append("Gobblely 30% +5")
    elif x == 9 or x == "Faerie Speak":
        skills.append("Faerie Spiek 30% +5")
    elif x == 10 or x == "Demongogian":
        skills.append("Demongogian 30% +5")
    elif x == 11 or x == "Russian":
        skills.append("Russian 30% +5")
    elif x == 12 or x == "Mongolian":   
        skills.append("Mongolian 30% +5")
    elif x == 13 or x =="Rogues Cant":
        skills.append("Rogues Cant 30% +5")
    else:
        SKILLS()
    return skills

def LORE():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,11)
    if RND == "N":
        choices = ["American Indians","Cattle & Animals","Deamons","Monsters","Faeries","Creatures of Magic","Juicers","Magic","Psychics","Psionics"," D-Bee"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "American Indians":
        skills.append("Lore American Indians 25% +5")
    elif x == 2 or x == "Cattle & Animals":
        skills.append("Lore Cattle & Animals 30% +5")
    elif x == 3 or x == "D-Bee ":
        skills.append("Lore D-Bee 25% +5")
    elif x == 4 or x == "Demons":
        skills.append("Lore Demons 25% +5")
    elif x == 5 or x == "Monsters":
        skills.append("Lore Monsters 25% +5")
    elif x == 6 or x == "Faeries":
        skills.append("Lore Faeries 25% +5")
    elif x == 7 or x == "Creatures of Magic":
        skills.append("Lore Creatures of Magic 25% +5")
    elif x == 8 or x == "Juicers":
        skills.append("Lore Juicers 30% +5")
    elif x == 8 or x == "Magic":
        skills.append("Lore Magic 25% +5")
    elif x == 9 or x == "Psychics":
        skills.append("Lore Psychics 25% +5")
    elif x == 10 or x == "Psionics":
        skills.append("Lore Psionics 25 % +5")
    else:
        print ("def LORE outside bounds",x)
    return skills
def MECHANICAL():
    global skills,RND
    if RND == "Y":
        x = random.randrange(1,9)
    if RND == "N":
        choices = ["Aircraft Mechanics","Automotive Mechanics","Bioware Mechanic","Locksmith","Mechanical Engineer","Robot Mechanics","Vehicle Armorer","Weapons Engineer"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Aircraft Mechanics":
        skills.append("Aircraft Mechanics 25% +5")
    elif x == 2 or x == "Automotive Mechanics":
        skills.append("Automotive Mechanics 25% +5")
    elif x == 3 or x == "Bioware Mechanic":
        skills.append("Bioware Mechanic 30% +5")
    elif x == 4 or x == "Locksmith":
        skills.append("Locksmith 25% +5")
    elif x == 5 or x == "Mechanical Engineer":
        skills.append("Mechanical Engineer 25% +5")
        skills.append(" +5% locksmith and surveillance systems")
    elif x == 6 or x == "Robot Mechanics":
        skills.append("Robot Mechanics 20% +5")
    elif x == 7 or x == "Vehicle Armorer":
        skills.append("Vehicle Armorer 30% +5")
    elif x == 8 or x == "Weapons Engineer":
        skills.append("Weapons Engineer 25% +5")

def MEDICAL():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,16)
    if RND == "N":
        choices = ["Animal Husbandry","Brewing Medicinal","Crime Scene Investigation","Cybernetic Medicine","Entomological Medicine","Field Surgery","First Aid","Forensics","Holistic Medicine","Pathology","Paramedic","Psychology","Veterinary Science"," Medical Doctor","M.D. in Cybernetics"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Animal Husbandry":
        skills.append("Animal Husbandry 35% +5")
    elif x == 2 or x == "Brewing Medicinal":
        skills.append("Brewing Medicinal 25/30% +5")
        skills.append(" +5 Holistic Medicine Skill")
    elif x == 3 or x == "Crime Scene Investigation":
        skills.append("Crime Scene Investigation 35% +5")
        skills.append(" Requires Biology, Chemistry, Analyrical, Advanced Mathmatics and Literacy")
    elif x == 4 or x == "Cybernetic Medicine":
        skills.append("Cybernetic Medicine 40/60% +5")
    elif x == 5 or x == "Entomological Medicine":
        skills.append("Entomological Medicine 40/20% +5")
        skills.append(" Requires Basic Math and Chemistry")
    elif x == 6 or x == "Field Surgery":
        skills.append("Field Surgery 16% +4")
    elif x == 7 or x == "First Aid":
        skills.append("First Aid 45% +5")
    elif x == 8 or x == "Forensics":
        skills.append("Forensics 35% +5")
        skills.append(" Requires Biology and Chenistry")
    elif x == 9 or x == "Holistic Medicine":
        skills.append("Holistic Medicine 30/20% +5")
        skills.append(" +10 Brewing, Identify Plants and Fruits and Preserve Food Skills")
    elif x == 10 or x == "Pathology":
        skills.append("Pathology 40% +5")
    elif x == 11 or x == "Paramedic": 
        skills.append("Paramedic 40% +5")
        skills.append(" +5 Forensic Skill")
        skills.append(" Requires Biology Chemistry and Literacy Skills")
    elif x == 12 or x == "Psychology":  
        skills.append("Psychology 35% +5")
    elif x == 13 or x == "Veterinary Science":
        skills.append("Veterinary Science 50% +4")
        skills.append(" Requires Biology and Animal Husbandry")
    elif x == 14 or x == "Medical Doctor":
        skills.append("Medical Doctor 60/50% +5")
        skills.append(" Reqires Biology, Pathology, Chemistry, Basic or Advanced Mathmatics and Literacy")
    elif x == 15 or x == "M.D. in Cybernetics":
        skills.append("M.D. in Cybernetics")
        skills.append(" Requires Cybernetic Medicine skill twice and Electrical Engineering")
    else:
        SKILLS()
    return skills

def MILITARY():
    global RND,skills#,PE,Speed,SDC FORCED MARCH
    if RND == "Y":
        x = random.randrange(1,16)
    if RND == "N":
        choices = ["Camouflage","Demolitions"," Demolitions Disposal","Underwater Demolitions","Field Armorer & Amunitions Expert","Find Contraband","Forced March","Military Etiquette","Military Forticication","Naval History","Naval Tactics","NBC Warefare","Parachuting","Recognize Weapon Quality","Trap/Mine Detection"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Camouflage":
        skills.append("Camouflage 20% +5")
    elif x == 2 or x == "Demolitions":
        skills.append("Demolitions 60$ +3")
    elif x == 3 or x == "Demolitions Disposal":
        skills.append("Demolitions Disposal 60% +3")
    elif x == 4 or x == "Underwater Demolitions":
        skills.append("Demolitions: Underwater 56% +4")
    elif x == 5 or x == "Field Armorer & Amunitions Expert":
        skills.append("Field Armorer & Amunitions Expert 40% +5")
        skills.append(" Basic Mathmatics 30% +5")
    elif x == 6 or x == "Find Contraband":
        skills.append("Find Contraband 26% +5")
    elif x == 7 or x == "Forced March":
        skills.append("Forced march")
        #edit this section to reflect changes
##        PE=PE+2
##        if RND == "Y":
##            z = random.randrange(1,5)
##            Speed=Speed+z
##            z = random.randrange(2,13)
##            SDC=SDC+z
##        if RND == "N":
##            z= input ("please Roll 1d4")
##            Speed=Speed+z
##            z= input ("please Roll 2d6")
##            SDC=SDC+z
    elif x == 8 or x == "Military Etiquette":
        skills.append("Military Etiquette 35$ +5")
    elif x == 9 or x == "Military Forticication":
        skills.append("Military Forticication 30% +5")
    elif x == 10 or x == "Naval History":
        skills.append("Naval History 30% +4")
    elif x == 11 or x == "Naval Tactics":
        skills.append("Naval Tactics 25% +5")
    elif x == 12 or x == "NBC Warefare":
        skills.append("NBC Warefare 35% +5")
    elif x == 13 or x == "Parachuting":
        skills.append("Parachuting 40% +5")
    elif x == 14 or x == "Recognize Weapon Quality":
        skills.append("Recognize Weapon Quality 25% 5")
    elif x == 15 or x == "Trap/Mine Detection":
        skills.append("Trap/Mine Detection 20% +5")
    else:
        SKILLS()
    return skills#,PE,Speed,SDC
#def PHYSICAL():

##    global RND,skills,PS,PP,PE,SDC,Speed,dodge,attack
##    if RND == "Y":
##        x = random.randrange(1,18)
##    if RND == "N":
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
##        print "13 - physical labor"
##        print "14 - Prowl"
##        print "15 - Running"
##        print "16 - Swimming"
##        print "17 - S.C.U.B.A"
##        print "18 - Wrestling"
##        x = input(" Please enter Skill: ")
##    if x ==1:
##        skills.append("Acrobatics:")
##        skills.append("Automatic kick attack at first level; IDS damage.")
##        skills.append("60% +5% per level — Sense of balance")
##        skills.append("60% + 3% per level — Walk tightrope or high wire")
##        skills.append("80% + 2% per level — Climb rope")
##        skills.append("60% +5% per level — Back flip")
##        skills.append("40% base climb ability or adds a + 15% to climb skill.")
##        skills.append("30% base prowl ability or adds a +5% to prowl skill")
##        skills.append("+ 2 bonus to roll with punch or fall")
##        #roll=roll+1
##        PS=PS+1
##        PP=PP+1
##        PE=PE+1
##        if RND == "Y":
##            z = random.randrange(1,6)
##        if RND == "N":
##            z= input ("please Roll 1d6")
##        SDC=SDC+z
##    elif x == 2:
##        skills.append("Athletics")
##        #parry=parry+1
##        dodge=dodge+1
##        #roll=roll+1
##        PS=PS+1
##        if RND == "Y":
##            z = random.randrange(1,6)
##            Speed=Speed+x
##            z = random.randrange(1,8)
##            SDC=SDC+z
##        if RND == "N":
##            z= input ("please Roll 1d6")
##            Speed=Speed+z
##            z= input ("please Roll 1d8")
##            SDC=SDC+z
##    elif x == 3:
##        skills.append("Aerobic Athletics")
##        if RND == "Y":
##            z = random.randrange(2,8)
##        if RND == "N":
##            z= input ("please Roll 2d4")
##        SDC=SDC+z
##    elif x == 4:
##        skills.append("Body Building & Weight Lifting")
##        PS=PS+2
##        SDC=SDC+10
##    elif x == 5:
##        skills.append("Boxing")
##        attack=attack+1
##        #parry=parry+2
##        dodge=dodge+2
##        #roll=roll+1
##        PS=PS+2
##        if RND == "Y":
##            z = random.randrange(3,18)
##        if RND == "N":
##            z= input ("please Roll 3d6")
##        SDC=SDC+z
##    elif x == 6:
##        skills.append("Climbing 40% +5")                      
##    elif x == 7:
##        skills.append("Fencing")
##        skills.append("	    requires W.P. Sword (W.P. Knife optional)")
##        skills.append("+1 strike/ perry with sword or dagger")
##        skills.append("+1d6 damage with sword")
##    elif x == 8:
##        skills.append("Forced march")
##        PE=PE+2
##        if RND == "Y":
##            z = random.randrange(1,4)
##            Speed=Speed+z
##            z = random.randrange(2,12)
##            SDC=SDC+z
##        if RND == "N":
##            z= input ("please Roll 1d4")
##            Speed=Speed+z
##            z= input ("please Roll 2d6")
##            SDC=SDC+z
##    elif x == 9:
##        skills.append("Gymnastics")
##        skills.append("Automatic kick attack at first level; 2D4 damage.")
##        skills.append("50% + 5% per level — Sense of balance")
##        skills.append("60% + 3% per level — Work parallel bars & rings")
##        skills.append("70% + 2% per level — Climb rope")
##        skills.append("70% + 5% per level — Back flip")
##        skills.append("25% base climb ability or adds a +7% to climb skill.")
##        skills.append("30% base prowl ability or adds a +5% to prowl skill.")
##        #roll+roll+2
##        PS=PS+2
##        PE=PE+2
##        PP=PP+1        
##        if RND == "Y":
##            z = random.randrange(2,12)
##        if RND == "N":
##            z= input ("please Roll 2d6")
##        SDC=SDC+z
##    elif x == 10:
##        skills.append("Juggling 35% +5")
##    elif x == 11:
##        skills.append("Kick Boxing")
##        PE=PE+1
##        PS=PS+1
##        if RND == "Y":
##            z = random.randrange(1,10)
##        if RND == "N":
##            z= input ("please Roll 1d10")
##        SDC=SDC+z
##        skills.append(" Round House Kick 3d6")
##        skills.append(" Axe Kick 2d8")
##        skills.append(" Knee Strike 1d8")
##        skills.append(" Leap Kick 3d8 (counts as two melee attacks)")
##    elif x == 12:
##        skills.append("Outdoorsmanship")
##        skills.append(" Requires Wilderness Survival")
##        skills.append(" +5 Wilderness Survival Skill")
##        PE=PE+1
##        if RND == "Y":
##            z = random.randrange(2,12)
##        if RND == "N":
##            z= input ("please Roll 2d6")
##        SDC=SDC+z
##    elif x == 13:
##        skills.append("physical labor")
##        PS=PS+2
##        PE=PE+1
##        if RND == "Y":
##            z = random.randrange(2,16)
##        if RND == "N":
##            z= input ("please Roll 2d8")
##        SDC=SDC+z
##    elif x == 14:
##        skills.append("Prowl 25% + 5%")
##    elif x == 15:
##        skills.append("Running")
##        PE=PE+1
##        if RND == "Y":
##            z = random.randrange(4,16)
##            Speed=Speed+z
##            z = random.randrange(1,6)
##            SDC=SDC+z
##        if RND == "N":
##            z= input ("please Roll 4d4")
##            Speed=Speed+z
##            z= input ("please Roll 1d6")
##            SDC=SDC+z
##    elif x == 16:
##        skills.append("Swimming 50% +5")
##    elif x == 17:
##        skills.append("S.C.U.B.A 50% +5")
##    elif x == 18:
##        skills.append("Wrestling")
##        skills.append(" Body block/tackle does 1D4 damage and the opponent must dodge or parry to avoid being knocked down (lose one melee attack if knocked down).")
##        skills.append(" Pin/incapacitate on a roll of 18, 19, or 20.")
##        skills.append(" Crush/squeeze does 1D4 damage per squeeze attack.")
##        #roll=roll+1
##        PS=PS+2
##        PE=PE+1
##        if RND == "Y":
##            z = random.randrange(4,24)
##        if RND == "N":
##            z= input ("please Roll 4d6")
##        SDC=SDC+z
##    else:
##        SKILLS()
##    return skills,PS,PP,PE,SDC,Speed,dodge,attack
##    
def PILOTSKILLS():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,24)
    if RND == "N":
        choices = ["Airplane","Automobile","Bicycling","Boat: Motor, Race & HydroFoil","Boat: Paddle Types/Canoe/Kayak","Boat: Sail Type","Boat: Ships/Seamanship","Combat Driving","Hover craft Ground","Hovercycles, Skycycles & Rocket Bikes","Jet Aircraft","Jet Packs","Military: Combat Helicopter","Military: Jet Fighter","Military: Submersibles","Military: Tanks & APCs","Military: Warship & Patrol Boats","Motorcycles & Snomobiles","Robots & Power Armor","Tracked & Construction Vehicles","Truck","Water Scooters","Water Skiing and Surfing"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Airplane":
        skills.append("Airplane 50% +4")
    elif x == 2 or x == "Automobile":
        skills.append("Drive: Automobile 60% +2")
    elif x == 3 or x == "Bicycling":
        skills.append("Bicycling 44% +4")
    elif x == 4 or x == "Boat: Motor, Race & HydroFoil":
        skills.append("Boat: Motor, Race & HydroFoil 55% +5")
    elif x == 5 or x == "Boat: Paddle Types/Canoe/Kayak":
        skills.append("Boat: Paddle Types/Canoe/Kayak 50% +5")
    elif x == 6 or x == "Boat: Sail Type":
        skills.append("Boat: Sail Type 60% +5")
    elif x == 7 or x == "Boat: Ships/Seamanship":
        skills.append("Boat: Ships/Seamanship 45/40% +5")
        skills.append(" Requires Sewing and Rope Work SKills")
    elif x == 8 or x == "Combat Driving":
        skills.append("Combat Driving")
    elif x == 9 or x == "Hover craft Ground":
        skills.append("Hover craft Ground 50% +5")
    elif x == 10 or x == "Hovercycles, Skycycles & Rocket Bikes":
        skills.append("Hovercycles, Skycycles & Rocket Bikes 70% +3")
    elif x == 11 or x == "Jet Aircraft":
        skills.append("Jet Aircraft 40% +4")
    elif x == 12 or x == "Jet Packs":
        skills.append("Jet Packs 42% +4")
    elif x == 13 or x == "Military: Combat Helicopter":
        skills.append("Military: Combat Helicopter 52% +4")
    elif x == 14 or x == "Military: Jet Fighter":
        skills.append("Military:Jet Fighter 40% +4")
    elif x == 15 or x == "Military: Submersibles":
        skills.append("Military: Submersibles 40% +4")
    elif x == 16 or x == "Military: Tanks & APCs":
        skills.append("Military: Tanks & APCs 36% +4")
    elif x == 17 or x == "Military: Warship & Patrol Boats":
        skills.append("Military: Warship & Patrol Boats 40% +4")
    elif x == 18 or x == "Motorcycles & Snomobiles":
        skills.append("Motorcycles & Snomobiles 60% +4")
    elif x == 19 or x == "Robots & Power Armor":
        skills.append("Robots & Power Armor 56% +3")
    elif x == 20 or x == "Tracked & Construction Vehicles":
        skills.append("Tracked & Construction Vehicles 40% +4")
    elif x == 21 or x == "Truck":
        skills.append("Truck 40% +4")
    elif x == 22 or x == "Water Scooters":
        skills.append("Water Scooters 50% +5")
    elif x == 23 or x == "Water Skiing and Surfing":
        skills.append("Water Skiing and Surfing 40% +4")
    else:
        SKILLS()
    return skills
def PILOTRELATED():
    global skills
    if RND == "Y":
        x = random.randrange(1,4)
    if RND == "N":
        choices = ["Navigation","Read Sensory Equipment","Weapon Systems","Robot Combat: Basic","Robot Combat: Elite"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Navigation":
        skills.append("Navigation 40% +5")
        skills.append(" Requires math, read sensory equipment. literacy")
    elif x == 2 or x == "Read Sensory Equipment":
        skills.append("Read Sensory Equipment 30% 5")
    elif x == 3 or x == "Weapon Systems":
        skills.append("Weapon Systems 40% +5")
    elif x == 4 or x == "Robot Combat: Basic":
        skills.append("Robot Combat: Basic")
    elif x == 5 or x == "Robot Combat: Elite":
        skills.append("Robot Combat: Elite")
    else:
        SKILLS()
    return skills
def ROGUESKILLS():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,17)
    if RND == "N":
        choices = ["Cardsharp","Computer Hacking","Concealment","Find Contraband","Gambling (standard)","Gambling (Dirty Tricks)","I.D. Undercover Agent","Imitate Voice & Sounds","Palming","Pick Locks","Pick Pockets","Prowl","Roadwise","Safe Cracking","Seduction","Streetwise","Tailing"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Cardsharp":
        skills.append("Cardsharp 24% +4")
    elif x == 2 or x == "Computer Hacking":
        skills.append("Computer Hacking 20% +5")
        skills.append(" Requires Literact, Computer Poeration, Computer Programming, & Basic Mathmatics")
    elif x == 3 or x == "Concealment":
        skills.append("Concealment 20% +4")
    elif x == 4 or x == "Find Contraband":
        skills.append("Find Contraband 26% +4")
        skills.append("+10% I.D. Undercover Agent skill")
    elif x == 5 or x == "Gambling (standard)":
        skills.append("Gambling (standard) 30% +5")
    elif x == 6 or x == "Gambling (Dirty Tricks)":
        skills.append("Gambling (Dirty Tricks) 20% +4")
    elif x == 7 or x == "I.D. Undercover Agent":
        skills.append("I.D. Undercover Agent 30% +4")
    elif x == 8 or x == "Imitate Voice & Sounds":
        skills.append("Imitate Voice & Sounds 42/36% +4")
        skills.append("+5% Impersonation Skill")
    elif x == 9 or x == "Palming":
        skills.append("Palming 20% +5")
    elif x == 10 or x == "Pick Locks":
        skills.append("Pick Locks 30% +5")
    elif x == 11 or x == "Pick Pockets":
        skills.append("Pick Pockets 25% +5")
    elif x == 12 or x == "Prowl":
        skills.append("Prowl 25% +5")
    elif x == 13 or x == "Roadwise":
        skills.append("Roadwise 26% +4")
    elif x == 14 or x == "Safe Cracking":
        skills.append("Safe Cracking 20% +4")
        skills.append(" M.E. of 14 or less -10% skill")
    elif x == 15 or x == "Seduction":
        skills.append("Seduction 20% +3")
        skills.append(" +1% for each point over 20 M.A. and +2% for each point over 17 P.B.")
    elif x == 16 or x == "Streetwise":
        skills.append("Streetwise 20% +4")
        skills.append("+10% I.D. Undercover Agent skill")
    elif x == 17 or x == "Tailing":
        skills.append("Tailing 30% +5")
        skills.append("+5% if character also has prowl")                 
    else:
        SKILLS()
    return skills
def SCIENCE():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,14)
    if RND == "N":
        choices = ["Anthropology","Archaeology","Artificial Intelligence","Astronomy & Navigation","Astrophysics","Biology","Botany"," Chemistry","Chemistry: Analytical","Chemistry: pharmaceutical","Mathematics: Basic","Mathematics: Advanced","Xenology","Zoology"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Anthropology":
        skills.append("Anthropology 30% +5")
    elif x == 2 or x == "Archaeology":
        skills.append("Archaeology 30/20% +5")
    elif x == 3 or x == "Artificial Intelligence":
        skills.append("Artificial Intelligence 30% +3")
        skills.append(" Requirs Computer Operation")
        skills.append(" +5 All COmputer SKills")
    elif x == 4 or x == "Astronomy & Navigation":
        skills.append("Astronomy & Navigation 30% +5")
        skills.append(" +10% if character has Advanced Mathmatics")
        skills.append(" requires Basic Mathmatics and Literacy")
    elif x == 5 or x == "Astrophysics":
        skills.append("Astrophysics 30% +5")
    elif x == 6 or x == "Biology":
        skills.append("Biology 30%+5")
    elif x == 7 or x == "Botany":
        skills.append("Botany 25% +5")
    elif x == 8 or x == "Chemistry":
        skills.append("Chemistry 30% +5")
    elif x == 9 or x == "Chemistry: Analytical":
        skills.append("Chemistry: Analytical 25% +5")
        skills.append(" Requires Chemistry, Advanced Mathmatics and Literacy")
    elif x == 10 or x == "Chemistry: pharmaceutical":
        skills.append("Chemistry: pharmaceutical 30& +5")
        skills.append(" +10% Juicer Lore")
    elif x == 11 or x == "Mathematics: Basic":
       skills.append("Mathematics: Basic 45% +5")
    elif x == 12 or x == "Mathematics: Advanced":
        skills.append("Mathematics: Advanced 45% +5")
        skills.append(" requires Basic Mathmatics")
    elif x == 13 or x == "Xenology":
        skills.append("Xenology 30% +5")
    elif x == 14 or x == "Zoology":
        skills.append("Zoology 30% +5")
        skills.append(" +5% Herding and Track & Trap Animals +10% Veternary Science")             
    else:
        SKILLS()
    return skills
def TECHNICAL():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,28)
    if RND == "N":
        choices = ["Apraise Goods","Art","Begging","Breed Dogs","Calligraphy","Computer Operation","Computer Programming","Cybernetics: Basic","Excavation","Firefighting","Gemology","General Repair & Maintenance","History: Pre-Rifts","History: Post-Apocalypse","Jury-Rig","Law: General","Leather Working","Masonry","Mining","Mythology","Philosophy","Photography","Recycling","Research","Rope Works","Salvage","Ventriloquism","Whittling & Sculpting"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Apraise Goods":
        skills.append("Apraise Goods 30% +5")
    elif x == 2 or x == "Art":
        skills.append("Art 35% +5")
    elif x == 3 or x == "Begging":
        skills.append("Begging 30% +3")
    elif x == 4 or x == "Breed Dogs":
        skills.append("Breed Dogs 40/20% +5")
    elif x == 5 or x == "Calligraphy":
        skills.append("Calligraphy 35% +5")
        skills.append(" Requires Literacy to actually write, othewise copy letters and ideograms.")
    elif x == 6 or x == "Computer Operation":
        skills.append("Computer Operation 40% +5")
        skills.append(" Requires literacy")
    elif x == 7 or x == "Computer Programming":
        skills.append("Computer Programming 35% +5")
        skills.append(" Requires Computer Operation")
    elif x == 8 or x == "Cybernetics: Basic":
        skills.append("Cybernetics: Basic 25% +5")
    elif x == 9 or x == "Excavation":
        skills.append("Excavation 40% +5")
    elif x == 10 or x == "Firefighting":
        skills.append("Firefighting 30% +5")
    elif x == 11 or x == "Firefighting":
        skills.append("Gemology 25% +5")
        skills.append(" +5% Mining")
    elif x == 12 or x == "General Repair & Maintenance":
        skills.append("General Repair & Maintenance 35% +5")
    elif x == 13 or x == "History: Pre-Rifts":
        skills.append("History: Pre-Rifts 32%/24% +4")
    elif x == 14 or x == "History: Post-Apocalypse":
        skills.append("History: Post-Apocalypse 35/30% +5")
    elif x == 15 or x == "Jury-Rig":
        skills.append("Jury-Rig 25% +5")
        skills.append(" Requires Basic Math and Electonics")
    elif x == 16 or x == "Law: General":
        skills.append("Law: General 35% +5")
    elif x == 17 or x == "Leather Working":
        skills.append("Leather Working 40% +5")
    elif x == 18 or x == "Masonry":
        skills.append("Masonry 40% +5")
    elif x == 19 or x == "Mining":
        skills.append("Mining 35% +5")
    elif x == 20 or x == "Mythology":
        skills.append("Mythology 30% +5")
    elif x == 21 or x == "Philosophy":
        skills.append("Philosophy 30% +5")
    elif x == 22 or x == "Photography":
        skills.append("Photography 35% +5")
    elif x == 23 or x == "Recycling":
        skills.append("Recycling 30% +5")
    elif x == 24 or x == "Research":
        skills.append("Research 40% +5")
    elif x == 25 or x == "Rope Works":
        skills.append("Rope Works 30% +5")
    elif x == 26 or x == "Salvage":
        skills.append("Salvage 35% +5")
    elif x == 27 or x == "Ventriloquism":
        skills.append("Ventriloquism 16% +4")
    elif x == 28 or x == "Whittling & Sculpting" :
        skills.append("Whittling & Sculpting 30% +5")
    else:
        SKILLS()
    return skills

def WILDERNESS():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,13)
    if RND == "N":
        choices = ["Boat Building","Carpenntry","Dowsing","Fasting","Hunting","Identify Plants & Fruits","Land Navigation","Preserve Food","Skin & Prepare Animal Hides","Spelunking","Track Animals","Trap Animals","Wilderness Survival"]
        x = easygui.choicebox(title,msg,choices)
    if x == 1 or x == "Boat Building":
        skills.append("Boat Building 25% +5")
    elif x == 2 or x == "Carpenntry":
        skills.append("Carpentry 25% +5")
    elif x == 3 or x == "Dowsing":
        skills.append("Dowsing 20% +5")
    elif x == 4 or x == "Fasting":
        skills.append("Fasting 40% +5")
    elif x == 5 or x == "Hunting":
        skills.append("Hunting")
        skills.append(" +2% prowl")
        skills.append(" +5% track animals")
        skills.append(" +5% skin animals")
        skills.append(" +5% wilderness survival +5 to cook the catch only")
    elif x == 6 or x == "Identify Plants & Fruits":
        skills.append("Identify Plants & Fruits 25% +5")
    elif x == 7 or x == "Land Navigation":
        skills.append("Land Navigation 36% +4")
    elif x == 8 or x == "Preserve Food":
        skills.append("Preserve Food 25% +5")
    elif x == 9 or x == "Skin & Prepare Animal Hides":
        skills.append("Skin and Prepare Animal Hides 30% +5")
    elif x == 10 or x == "Spelunking":
        skills.append("Spelunking 35% +5")
        skills.append("+5% Climbing")
    elif x == 11 or x == "Track Animals":
        skills.append("Track Animals 20% +5")
    elif x == 12 or x == "Trap Animals":
        skills.append("Trap Animals 30% +5")
    elif x == 13 or x == "Wilderness Survival":
        skills.append("Wilderness Survival 30% +5")
    else:
        SKILLS()
    return skills

def PirateSKILLS():
    global RND,skills
    skills=stats.skills
    if RND == "Y":
        x = random.randrange(1,27)
    if RND == "N":
        msg = "Please pick your Pirate skill"
        choices = ['Cardsharp', 'Concealment', 'Detect Ambush', 'Detect Concealment', 'Disguise', 'Escape Artist', 'Forgery', 'Gambling (Dirty Tricks)', 'Gambling (standard)', 'I.D. Undercover Agent', 'Imitate Voice & Sounds', 'Impersonation', 'Intelligence', 'Palming', 'Pick Locks', 'Pick Pockets', 'Prowl', 'Safe Cracking', 'Seduction', 'Sniper', 'Streetwise', 'Tailing', 'Tracking (people)', 'Undercover Ops', 'Wilderness Survival']
        x = easygui.choicebox(title,msg,choices)
    elif x == 1 or x == "Cardsharp":
        skills.append("Cardsharp 30% +5")
    elif x == 2 or x == "Concealment":
        skills.append("Concealment 30% +5")
    elif x == 3 or x == "Detect Ambush":
        skills.append("Detect Ambush 30% +5")
    elif x == 4 or x == "Detect Concealment":
        skills.append("Detect Concealment 30% +5")
    elif x == 5 or x == "Disguise":
        skills.append("Disguise 30% +5")
    elif x == 6 or x == "Escape Artist":
        skills.append("Escape Artist 30% +5")
    elif x == 7 or x == "Forgery":
        skills.append("Forgery 30% +5")
    elif x == 8 or x == "Gambling (Dirty Tricks)":
        skills.append("Gambling (Dirty Tricks) 30% +5")
    elif x == 9 or x == "Gambling (standard)":
        skills.append("Gambling (standard) 30% +5")
    elif x == 10 or x == "I.D. Undercover Agent":
        skills.append("I.D. Undercover Agent 30% +5")
    elif x == 11 or x == "Imitate Voice & Sounds":
        skills.append("Imitate Voice & Sounds 30% +5")
    elif x == 12 or x == "Impersonation":
        skills.append("Impersonation 30% +5")
    elif x == 13 or x == "Intelligence":
        skills.append("Intelligence 30% +5")
    elif x == 14 or x == "Palming":
        skills.append("Palming 30% +5")
    elif x == 15 or x == "Pick Locks":
        skills.append("Pick Locks 30% +5")
    elif x == 16 or x == "Pick Pockets":
        skills.append("Pick Pockets 30% +5")
    elif x == 17 or x == "Prowl":
        skills.append("Prowl 30% +5")
    elif x == 18 or x == "Safe Cracking":
        skills.append("Safe Cracking 30% +5")
    elif x == 19 or x == "Seduction":
        skills.append("Seduction 30% +5")
    elif x == 20 or x == "Sniper":
        skills.append("Sniper 30% +5")
    elif x == 21 or x == "Streetwise":
        skills.append("Streetwise 30% +5")
    elif x == 22 or x == "Tailing":
        skills.append("Tailing 30% +5")
    elif x == 23 or x == "Tracking (people)":
        skills.append("Tracking (people) 30% +5")
    elif x == 24 or x == "Undercover Ops":
        skills.append("Undercover Ops 30% +5")
    elif x == 25 or x == "Wilderness Survival":
        skills.append("Wilderness Survival 30% +5")
    else:
        print ("skills.py PirateSKILLS() line 194 error")
    stats.skills = skills
    return skills


#calls main
main()
