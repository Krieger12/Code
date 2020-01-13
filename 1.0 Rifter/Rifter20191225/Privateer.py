import easygui, random
import stats
title = "Privateer"
def main():
    print("Privateer.py")
    ImportStats()
    if stats.RND == "T":
        print RND
    Privateer()
    ExportStats()


def Privateer(): # requires 8 IQ & 10 PS
    global RND,SDC,PE,PP,inish,roll,horror,OCC,equipment,skills#+3 horror
    stats.PE=stats.PE+1
    stats.PP=stats.PP+1
    stats.horror=stats.horror+3
    stats.SDC=1
    import SDC
    if stats.RND == 'Y':
        stats.SDC=stats.SDC+random.randrange(2,13)
    elif stats.RND == 'N':
        z = easygui.integerbox ("please roll 2d6 for SDC bonus")
        stats.SDC=stats.SDC+z
    elif stats.RND =="T":
        stats.SDC=stats.SDC+5
        RND = "Y"
        
    stats.OCC = "Privateer"
    skills.append("O.C.C. Skills:")
    skills.append("Language: American 88% +1%/level")
    #skills.append("Two Languages of choice (+20%)")
    #from skills import LANGUAGE
    if RND == "Y":
            lang = random.randrange(1,18)
    if RND == "N":
        choices = ['American', 'Atlantean/Greek', 'Australian', 'Chinese', 'Demongogian', 'Dragonese/Elven', 'Dwarven', 'Euro', 'Faerie Speak', 'Gargoyle', 'Gobbley', 'Japanese', 'Mongolian', 'Rogues Cant', 'Russian', 'Spanish', 'Techno-Can']
        lang = easygui.choicebox("Pick Language of choice.",title,choices)

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
    skills.append("Radio: Basic 55% +5")
    skills.append("Navigation 46% +4")
    skills.append("Pilot: Sail Type 55% +3")
    skills.append("Pilot: Ships 45% +3")
    #skills.append("Pilot: One water vessel of choice (+15%)")
    if RND == "Y":
        boat = random.randrange(1,8)
    if RND == "N":
        choices = ['Deep Sea Diving', 'Motor, Race & HydroFoil', 'Paddle Types/Canoe/Kayak', 'Submersibles', 'Warships & Patrol Boats', 'Water Scooters', 'Water Skiing and Surfing']
        boat = easygui.choicebox("Choose one Pilot skill",title,choices)
    elif boat == 1 or boat == "Deep Sea Diving":
        skills.append("Pilot: Deep Sea Diving 55% +3")
    elif boat == 2 or boat == "Motor, Race & HydroFoil":
        skills.append("Pilot: Motor, Race & HydroFoil 55% +3")
    elif boat == 3 or boat == "Paddle Types/Canoe/Kayak":
        skills.append("Pilot: Paddle Types/Canoe/Kayak 55% +3")
    elif boat == 4 or boat == "Submersibles":
        skills.append("Pilot: Submersibles 55% +3")
    elif boat == 5 or boat == "Warships & Patrol Boats":
        skills.append("Pilot: Warships & Patrol Boats 55% +3")
    elif boat == 6 or boat == "Water Scooters":
        skills.append("Pilot: Water Scooters 55% +3")
    elif boat == 7 or boat == "Water Skiing and Surfing":
        skills.append("Pilot: Water Skiing and Surfing 55% +3")
    skills.append("Swimming 70% +5")
    skills.append("Streetwise (+8%)")
    skills.append("Find Contraband, Weapons & Cybernetics 40% +4")
    skills.append("Recognize Weapon Quality 35% +5")
    weapon.append("W.P. Energy Rifle")
    #weapon.append("W.P. Three of choice")
    stats.wep = 3
    #skills.append("Hand to Hand: Expert")
    stats.hand = 2
    
    if stats.RND == "Y" or stats.RND == "T":
        stats.PSkillNumb,stats.SkillNumb = 6,3
    if stats.RND == "Y" or stats.RND == "N":
        skills.append(' ')
        race.append("More info on Privateer O.C.C. can be fount in the Coalition Navy book page 117")
        race.append("O.C.C. Related Skills: Select three physical or technical(+10%) skills and six others of choice")
        equipment.append(' ')
        equipment.append("Standard Equipment: Typically some type of mega-damage body armor, including modified Coalition Shark, Dead Boy armor or Dog Boy armor. Other common equipment includes. Goggles or nonenvironmental helmet with or without visor, flashlight, cigarette lighter, pack of cigarettes, comb, pocket mirror, 100 feet (30.5 m) of lightweight rope and a grappling hook, binoculars, knapsack, backpack, three large sacks, utility belt, air filter, two canteens or water skins.")
        equipment.append("Weapons include a survival knife or meat hook (1D6 S.D.C.), one or two Vibro-Knifes, a pistol or revolver (energy or other), a rifle (energy or other), and 1D4+1 additional E-clips/ammo clips for the weapon.")

        equipment.append("Specialized vehicles (jet skies, row boat, etc.), weapons, and equipment may be provided by the Captain or sponsor of the mission. However, individuals are generally expected to acquire and maintain their own gear, whether it be as little as a gun and life jacket to a suit of power armor and a trunk full of weapons.")
        equipment.append(' ')    
        equipment.append("Money: Starts with 1D4x1OOO in credits and 1D4xlOOO in saleable black market/trade items. The Captain of the ship typically provides his crew with a sleeping bunk, fresh water and lousy to excellent food depending on each individual ship. Some also provide some measure of medical care (again, can vary from lousy to excellent).")
        equipment.append(' ')
        equipment.append("Cybernetics: None to start. , but privateers often acquire 1D4 cybernetic implants or one bionic limb.")
        equipment.append(' ')
    return PE,inish,SDC,skills,OCC,race,equipment#PSkillNumb,SkillNumb,equipment#+3Horror

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
