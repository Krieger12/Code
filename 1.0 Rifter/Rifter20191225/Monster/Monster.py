#!/user/bin/env python
# -*- coding: cp1252 -*
# Rifts monster generator Page 250 of the main source book
# Created by Keith Marrs-Olson

#Main code to run

import random
import easygui
import stats
msg = ["secret rifter message from monster"]
title = ["Monster Title"]

def main():
    print("Monster.py")
    ImportStats()
    Monster()
    #ExportStats()

def Monster():
    race=stats.race
    if stats.RND == "N":
        stats.RND = "Y"
    if stats.RND == "Y" or stats.RND == "T":

        stats.inish = random.randrange(1,5)
        stats.strike = 1
        stats.attack = random.randrange(1,5)
        MDC = random.randrange(1,5)
        stats.MDC = MDC*10
        stats.IQ = random.randrange(2,9)
        PS = random.randrange(3,19)
        stats.PS=PS+12
        PP = random.randrange(2,13)
        stats.PP=PP+12
        PE = random.randrange(4,17)
        stats.PE=PE+12
        S = random.randrange(1,5)
        if S == 1:
            Speed = random.randrange(3,19)
        elif S == 2:
            Speed = random.randrange(5,31)
            Speed=Speed+6
        elif S == 3:
            Speed = random.randrange(1,7)
            Speed=Speed*10
        elif S == 4:
            Speed = random.randrange(2,13)
            Speed=((Speed*10)+20)
            
        stats.Speed=Speed
        Horror = random.randrange(3,12)
        stats.Horror=Horror+4
        stats.PPE = random.randrange(1,5)
        print stats.PPE
        stats.PPE=stats.PPE*10
               
    else:
        print ("Manual entry not implemented at this time")
##size area

    size = [
        "5  feet tall (1.5 m), equal to a small human.",
        "6  feet tall (1.8 m), equal to typical human.",
        "7  feet tall (2.1 m), equal to a tall human.",
        "10 feet tall (3 m), giant.",
        "12 feet tall (3.6 m), giant.",
        "15 feet tall (4.5 m), giant.",
        "18 feet tall (5.4 m), giant.",
        "20 feet tall (6.1 m), giant.",
        "22 feet tall (6.7 m), giant.",
        "25 feet tall (7.6 m), giant."
            ]
    if stats.RND == "Y" or stats.RND == "T":
        s = random.randrange(0,10)
    else:
        print ("Manual entry not implemented at this time")
        s = easygui.choicebox(msg,title,size)
    if s == size[4]:
        stats.MDC=stats.MDC+random.randrange(1,7)
    elif s == size[5]:
        stats.MDC=stats.MDC+random.randrange(2,13)
    elif s == size[6]:
        stats.MDC=stats.MDC+random.randrange(3,19)
    elif s == size[7]:
        stats.MDC=stats.MDC+random.randrange(4,25)
    elif s == size[8]:
        stats.MDC=stats.MDC+random.randrange(6,37)
    elif s == size[9]:
        stats.MDC=stats.MDC+(random.randrange(1,7)*10)
    print size[s]
    race.append(size[s])

    Hunting = [
        "Mated pairs, where there is one, another is near by.",
        "Solitary Hunter, always found alone.",
        "Hunt in small packs of 2D4.",
        "Hunt in medium packs of 3D6.",
        "Hunt in large packs of 6D6."
        ]
    if stats.RND == "Y" or stats.RND == "T":
        h = random.randrange(0,5)
    else:
        print ("Manual entry not implemented at this time")
        h = easygui.choicebox(msg,title,Weekness)
    race.append(Hunting[h])
    
    Feed=[
        
        "P.P.E., by killing its prey and absorbing the potential psychic energy, which is doubled at the moment of death.",
        "Feeds on human flesh; cannibal.",
        "Drinks human blood; vampire- like.",
        "Feeds on fear. A psychic vampire who empathically feels and absorbs his victim's emotions of fear/terror.",
        "None; hunts for the sheer pleasure of the kill. Does not eat or use any part of the prey."
        ]
    if stats.RND == "Y" or stats.RND == "T":
        w = random.randrange(0,5)
    else:
        print ("Manual entry not implemented at this time")
        w = easygui.choicebox(msg,title,Feed)
    race.append("Feeds on: ")
    race.append(Feed[w])
    x=0
    while x < 2:
        
        NWeapons = [
            "Horn: Stabbing attacks; 2D4 M.D.",
            "1D4+ 1 Tentacles instead of arms and hands: Quite powerful; 1D6 + 2 M.D. per hit/punch.",
            "Bite: Huge and powerful jaws and canine teeth; 2D6 M.D.",
            "Bite: Small, sharp teeth; 1D6 M.D.",
            "Clawed hands: 1D6 M.D.",
            "Clawed hands: Large retractable claws; 3D6 M.D.",
            "Thick, slashing tail: 2D4 M.D.; does not add to number of attacks.",
            "Prehensile tail: Used like a third arm/hand for hitting and holding; 1D4 M. D. damage but also adds one additional attack per melee.",
            "Prehensile tail with spikes or blade: Used as a third claw or stabbing/slashing weapon; 2D6 M.D.",
            "Fire Breath: Range is 40 feet (12 m), inflicts 3D6 M.D. Note: Dragons generally inflict 2D6 M.D. with their claws and 2D4 M.D. by bite."
            ]
        if stats.RND == "Y" or stats.RND == "T":
            w = random.randrange(0,10)
        else:
            print ("Manual entry not implemented at this time")
            w = easygui.choicebox(msg,title,NWeapons)
        race.append(NWeapons[w])
        if NWeapons[7]:
            stats.attack=stats.attack+1
            
        x=x+1
    x=0
    while x < 2:
        
        Abilities = [
            "Swim 90%",
            "Prowl 54% +4%",
            "Track by sight (follows trails, footprints, and other visual signs; knows the habits of its prey): 44% +4% per level of experience.",
            "Sense P.P.E. and Magic (same as Dog Pack).",
            "Track by smell 54% +4%",
            "Climb: 80% +2%",
            "Nightvision (Like an owl, can see clearly 200 feet (61 m) in total darkness and 4000 feet in outdoor night/darkness with other sources of light such as stars, moon, etc.).",
            "Keen Hearing (same as Dog Pack); + 1 on initiative and parry.",
            "Sense psychic and magic energy (same as Dog Pack).",
            "Natural sense of direction (never gets lost, homing sense: 80%)."
            ]
        if stats.RND == "Y" or stats.RND == "T":
            a = random.randrange(0,10)
        else:
            print ("Manual entry not implemented at this time")
            a = easygui.choicebox(msg,title,Abilities)
        race.append(NWeapons[a])
        x=x+1

    Weekness=[
        "Water. Normal water inflicts mega-damage! A squirt from a toy water pistol does 1D4 M.D. per each squirt (typical range 30 feet). A splash from an eight ounce glass of water does 2D6 M.D., a half gallon (1.6 liters) inflicts 6D6 M.D., while a gallon (3.7 liters) does 1D6X10 M.D. points.",
        "Energy. All types of energy including, fire, lasers, plasma, ion blasts, electricity, and nuclear energy inflicts double damage. However, kinetic energy/attacks, including mega-damage punches from robots and power armor, vibro- blades, explosives/missiles, rail guns, and bullets, do absolutely NO damage!",
        "Light. All forms of light blind and frighten the creature (-9 to strike, parry, and dodge when blinded). Lives in a dark cave or dwelling during the day. Hunts only at night. Exceptional night vision equal to a human's day vision. Laser weapons inflict double damage.",
        "Fire. All fires, even normal fires, inflict mega-damage. Megadamage fire/plasma/magic inflicts double damage.",
        "Weapons of Iron (must be 88% pure iron) inflict the mega-damage equivalent of the normal, ancient, S.D.C. weapon (see S.D.C. conversion to M.D.)",
        "Wood. The supernatural fiend is vulnerable to weapons made mostly of wood (90%). Thus, while bullets may bounce off, a wooden arrow shot from a bow will inflict mega-damage (see S.D.C. conversion to M.D.)."
        "Silver. The paranormal monster is vulnerable to weapons made of silver (including bullets). Basically works the same as Weapons of Iron.",
        "Symbols of goodness and purity invoke fear and hold the creature at bay. To be touched by the symbol inflicts 2D4 M.D. and sends the monster running 2D4xlOO yards/meters away.",
        "Mirror. The beast's reflection is terrifying, even to itself. If the creature sees its own reflection it must roll against its own horror factor. A failed roll means the creature is momentarily stunned as per the usual horror factor, then flees and hides for 1 D6x 10 minutes.",
        "Cold. The creature can not stand the cold. Exposure to freezing or below temperatures will inflict 2D6 M.D. every minute. The creature is rarely found in regions where the temperature drops to freezing, although the monster may migrate with the seasons. Shards of ice can be used like a dagger or club and do 1D6 M.D. each (snowballs inflict one M.D. point of damage each). Ice cold/frozen weapons will also inflict mega- damage."
        ]
    if stats.RND == "Y" or stats.RND == "T":
        w = random.randrange(0,10)
    else:
        print ("Manual entry not implemented at this time")
        w = easygui.choicebox(msg,title,Weekness)
    race.append("Weakness:")
    race.append(Weekness[w])


def ExportStats():
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND
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


main()
    
    
