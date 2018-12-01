#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

# Default OCC 
print ("Default.py")
import easygui, random
import stats
title = "RIFTS Char"
msg = "Defaulr Char"
def main():
    ImportStats()
    char()
    #ExportStats()
       
def char():
    global RND,PE,inish,SDC,skills,OCC,race,PSkillNumb,SkillNumb,equipment,weapon,wep#+3Horror
    stats.OCC = 'Vegabond'
    stats.SDC == 1
    import SDC
    skills.append("O.C.C. Skills:")
    skills.append("Language: American 88% +1%/level")
    if RND == "Y":
        lang = random.randrange(1,18)
    elif RND == "N":
        msg = "Languages of choice"
        choices = ['American', 'Atlantean/Greek', 'Australian', 'Chinese', 'Demongogian', 'Dragonese/Elven', 'Dwarven', 'Euro', 'Faerie Speak', 'Gargoyle', 'Gobbley', 'Japanese', 'Mongolian', 'Rogues Cant', 'Russian', 'Spanish', 'Techno-Can']
        lang = easygui.choicebox(title,msg,choices)
    elif RND == "T":
        lang = 1
        stats.wep = 1
    if lang == 1 or lang == "American":
        skills.append("Literacy: American 30% +3")
    elif lang == 2 or lang == "Atlantean/Greek":
        skills.append("Language: Atlantean/Greek 50% +3")
    elif lang == 3 or lang == "Australian":
        skills.append("Language: Australian 50% +3")
    elif lang == 4 or lang == "Chinese":
        skills.append("Language: Chinese 50% +3")
    elif lang == 5 or lang == "Demongogian":
        skills.append("Language: Demongogian 50% +3")
    elif lang == 6 or lang == "Dragonese/Elven":
        skills.append("Language: Dragonese/Elven 50% +3")
    elif lang == 7 or lang == "Dwarven":
        skills.append("Language: Dwarven 50% +3")
    elif lang == 8 or lang == "Euro":
        skills.append("Language: Euro 50% +3")
    elif lang == 9 or lang == "Faerie Speak":
        skills.append("Language: Faerie Speak 50% +3")
    elif lang == 10 or lang == "Gargoyle":
        skills.append("Language: Gargoyle 50% +3")
    elif lang == 11 or lang == "Gobbley":
        skills.append("Language: Gobbley 50% +3")
    elif lang == 12 or lang == "Japanese":
        skills.append("Language: Japanese 50% +3")
    elif lang == 13 or lang == "Mongolian":
        skills.append("Language: Mongolian 50% +3")
    elif lang == 14 or lang == "Rogues Cant":
        skills.append("Language: Rogues Cant 50% +3")
    elif lang == 15 or lang == "Russian":
        skills.append("Language: Russian 50% +3")
    elif lang == 16 or lang == "Spanish":
        skills.append("Language: Spanish 50% +3")
    elif lang == 17 or lang == "Techno-Can":
        skills.append("Language: Techno-Can 50% +3")

    skills.append("Cook: 10% +1")
    skills.append("Pilot Automobile 5% +1")
    #import SkillSelect(PSkillNumb,SkillNumb)
    stats.PSkillNumb,stats.SkillNumb = 8,6
    race.append("The Vegabond character may know a little bit of everything, but is a master of none. Consequently, the character gets only a few basic O.C.C. skills to start with, but does get a greater selection of skills as he grows in experience.")
    race.append("Other Skills (general): Select eight other skills at level one. Plus select four additional skills at levels two and three, two at level six, one at level nine, and one at level twelve. All new skills start at level one proficiency.")
    race.append("Secondary Skills: The character also gets to select six secondary skills from the previous list, at first level and another four at level three.")
    race.append(" ")
                
                




    race.append("Please refer to Rifts Main Book  pg 23")
    race.append("Or Ultimate Edition pg 305")
    equipment.append("Standard Equipment: The clothes on his back and an extra set, baseball cap, jacket or coat, knife, gun with one extra clip of ammo, flashlight, back pack, sleeping bag, wallet with I.D., a couple bandages, pack of aspirin, comb, toothbrush and paste, a bar of soap, several pieces of candy, a sturdy plastic bag for extra stuff, and an old, rusty junker of a car or motorcycle.")
    equipment.append(' ')    
    equipment.append("Money: 3D4 x 100 in credit.")
    equipment.append(' ')
    equipment.append("Cybernetics: None to start. May purchase implants later, if desired.")
    return PE,inish,SDC,skills,weapon,OCC,race,equipment#PSkillNumb,SkillNumb,equipment#+3Horror

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
