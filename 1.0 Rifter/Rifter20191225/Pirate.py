
# More info on Pirate O.C.C. can be fount in the Coalition Navy book page 114
import easygui, random
import stats
title = "RIFTS skills"
msg = "Please pick your skill"
def main():
    print("Pirate.py")
    ImportStats()
    Pirate()
    #ExportStats()
       
def Pirate():
    global RND,PE,inish,SDC,skills,OCC,race,PSkillNumb,SkillNumb,equipment,weapon,wep#+3Horror
    stats.OCC = 'Pirate'
    stats.SDC == 1
    import SDC
    if stats.RND == 'Y':
        x=random.randrange(2,13)
        stats.SDC=stats.SDC + x
        x=random.randrange(1,5)
        stats.PE=stats.PE + x
    elif stats.RND == "N":
        z = easygui.integerbox ("please roll 2d6 for SDC bonus")
        stats.SDC=stats.SDC+z
        z = easygui.integerbox ("please roll 1d4 for PE bonus")
        stats.PE=stats.PE+z
    elif stats.RND == "T":
        stats.SDC=stats.SDC + 5
        stats.PE=stats.PE + 1
        RND = "Y"
        
    stats.inish=stats.inish+1
    skills.append("O.C.C. Skills:")
    skills.append("Language: American 88% +1%/level")
    #skills.append("Two Languages of choice (+20%)")
    #from skills import LANGUAGE
    if RND == "Y":
            lang = random.randrange(1,18)
    if RND == "N":
        msg = "Languages of choice"
        choices = ['American', 'Atlantean/Greek', 'Australian', 'Chinese', 'Demongogian', 'Dragonese/Elven', 'Dwarven', 'Euro', 'Faerie Speak', 'Gargoyle', 'Gobbley', 'Japanese', 'Mongolian', 'Rogues Cant', 'Russian', 'Spanish', 'Techno-Can']
        lang = easygui.choicebox(msg,title,choices)
    if lang == 1 or lang == "American":
        skills.append("Literacy: American 40% +3")
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
    skills.append("Mathematics: Basic 55% +5")
    skills.append("Radio: Basic +55% +5")
    skills.append("Pilot: Water Scooters 55% +3")
    #skills.append("Pilot Boats: Two types of choice (+15%)")
    boatnum = 0
    while boatnum  < 2:
        boatnum = boatnum + 1
        if RND == "Y":
            boat = random.randrange(1,9)
        if RND == "N":
            msg = "Please select boat pilot skills"
            choices = ['Deep Sea Diving', 'Motor, Race & HydroFoil', 'Paddle Types/Canoe/Kayak', 'Sail Type', 'Ships', 'Submersibles', 'Warships & Patrol Boats', 'Water Skiing and Surfing']
            boat = easygui.choicebox(msg,title,choices)

        if boat == 1 or boat == "Deep Sea Diving":
            skills.append("Pilot: Deep Sea Diving 55% +3")
        elif boat == 2 or boat == "Motor, Race & HydroFoil":
            skills.append("Pilot: Motor, Race & HydroFoil 55% +3")
        elif boat == 3 or boat == "Paddle Types/Canoe/Kayak":
            skills.append("Pilot: Paddle Types/Canoe/Kayak 55% +3")
        elif boat == 4 or boat == "Sail Type":
            skills.append("Pilot: Sail Type 55% +3")
        elif boat == 5 or boat == "Ships":
            skills.append("Pilot: Ships 55% +3")
        elif boat == 6 or boat == "Submersibles":
            skills.append("Pilot: Submersibles 55% +3")
        elif boat == 7 or boat == "Warships & Patrol Boats":
            skills.append("Pilot: Warships & Patrol Boats 55% +3")
        elif boat == 8 or boat == "Water Skiing and Surfing":
            skills.append("Pilot: Water Skiing and Surfing 55% +3")
    skills.append("Swimming 70% +5")
    skills.append("Climbing 40/30% +5")
    skills.append("Fishing 45% +5")
    skills.append("Interrogation 40% +5")
    skills.append("Find Contraband, Weapons & Cybernetics 40% +4")
    skills.append("Recognize Weapon Quality 35% +5")

    #skills.append("O.C.C. Related Skills: Select three rogue (+5%) or espionage (+5%) skills and three of choice")
    skills.append(" ")
    skills.append("OCC Pirate Related Skills")
    sk=1
    while sk < 4:
        PirateSKILLS()
        sk=sk+1
    
    #skills.append("Hand to Hand: Expert")
    stats.hand = 2
    weapon.append("W.P. Energy Rifle")
    weapon.append("W.P. Sword")
    #weapon.append("W.P. Two of choice")
    stats.wep = 2          
    
    
    #stats.PSkillNumb,stats.SkillNumb = (6)3,3
    #import SkillSelect(PSkillNumb,SkillNumb)
    # rogue or espionage skills?
    stats.PSkillNumb,stats.SkillNumb = 3,3
    if stats.RND == "Y" or stats.RND == "N" or stats.RND == "T":
        race.append(' ')
        race.append("More info on Pirate O.C.C. can be fount in the Coalition Navy book page 114")
        equipment.append("Standard Equipment: Two energy weapons of choice and two ancient weapons (sword, mace, etc.), meat hook (1D6 S.D.C./H.P. damage), billy club (2D4 S.D.C./H.P. damage), dagger, a suit of M.D.C. body armor, 1D4 pairs of handcuffs, mess kit, canteen or water skin, sleeping bag, backpack, fishing hooks and line, 100 feet (30.5 m) of rope and a grappling hook, flashlight, cigarette lighter, pack of cigarettes, comb, pocket mirror, binoculars, and sunglasses or tinted goggles. Specialized vehicles (jet skies, row boat, etc.), weapons, and equipment may be provided by the Captain or sponsor of the mission if the pirates are working for somebody else or as Privateers. However, individuals are generally expected to acquire and maintain their own gear, whether it be as little as a gun and life jacket to a suit of power armor and a trunk full of weapons.")
        equipment.append(' ')    
        equipment.append("Money: Starts with 1D4x1OOO in creditis and 1D4xlOOO in saleable black market/trade items. The Captain of the ship typically provides his crew with a sleeping bunk, fresh water and lousy to excellent food depending on each individual ship. Some also provide some measure of medical care (again, can vary from lousy to excellent).")
        equipment.append(' ')
        equipment.append("Cybernetics: None to start, but pirates often acquire 1D4 cybernetic implants or one bionic limb.")
    return PE,inish,SDC,skills,weapon,OCC,race,equipment#PSkillNumb,SkillNumb,equipment#+3Horror

def PirateSKILLS():
    global RND,skills
    if RND == "Y":
        x = random.randrange(1,27)
    if RND == "N":
        msg = "Please pick your Pirate skill"
        choices = ['Cardsharp', 'Concealment', 'Detect Ambush', 'Detect Concealment', 'Disguise', 'Escape Artist', 'Forgery', 'Gambling (Dirty Tricks)', 'Gambling (standard)', 'I.D. Undercover Agent', 'Imitate Voice & Sounds', 'Impersonation', 'Intelligence', 'Palming', 'Pick Locks', 'Pick Pockets', 'Prowl', 'Safe Cracking', 'Seduction', 'Sniper', 'Streetwise', 'Tailing', 'Tracking (people)', 'Undercover Ops', 'Wilderness Survival']
        x = easygui.choicebox(msg,title,choices)
    if x == 1 or x == "Cardsharp":
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
        print ("pirate.py PirateSKILLS() line 202 error")
    return skills
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
