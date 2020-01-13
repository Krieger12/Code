#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

print ("combat.py")
title=("combat.py")
###Hand Skills
##'BASIC' =1
##'EXPERT' = 2
##'MARTIAL ARTS' = 3
##'COMMANDO'  = 3
##'ASSASSIN' = 4
##'Other
import easygui, random, stats
global skills,hand,RND
stats.title=title
level = stats.Level
Dhit = []
if stats.g == "G":
    msg=("What kind of Data do you want?")
    title=("combat.py")
    choices=("User Input","Random","Test")
    x = easygui.choicebox(msg, title, choices)
    if x == "User Input":
        RND = "N"
        stats.hand = 99
    elif x == "Random":
        RND = "Y"
    elif x == "Test":
        RND = "T"
def main():
    #import skills
    ImportStats()

    Print()
    if stats.combat[0] == "SELECT":
        Combat()
    elif stats.hand == 0:
        NONE()
    elif stats.combat[0] == "HAND TO HAND: BASIC"or stats.hand == 1:
        BASIC()
    elif stats.combat[0] == "HAND TO HAND: EXPERT"or stats.hand == 2:
        EXPERT()
    elif stats.combat[0] == "HAND TO HAND: MARTIAL" or stats.hand == 3:
        MARTIALARTS()
    elif stats.combat[0] == "HAND TO HAND: ASSASSIN" or stats.hand == 4:
        ASSASSIN()
    else:
        Combat()
    Print()
    #elif stats.combat == "BASIC":
    ExportStats()
def Print():
    print (Dhit)
    print (combat)
    print ("Number of Attacks %s ") % stats.attack
    print ("Damage + %s ") % stats.damage
    print ("Strike + %s ") % stats.strike
    print ("Dodge + %s ") % stats.dodge
    print ("Roll with punch or fall + %s ") % stats.roll
    print ("Parry attack + %s ") % stats.parry
    print ("Initiative + %s ") % stats.inish
    print ("Horror + %s ") % stats.horror
def ImportStats():
    global skills,hand,RND,combat
    hand = stats.hand
    skills = stats.skills
    combat=stats.combat
    #RND = stats.RND
    return hand,skills,combat
def ExportStats():
    global skills,hand,combat
    stats.hand = hand
    stats.skills = skills
    stats.combat = combat
    stats.Dhit = Dhit

def Combat():
    #Rifts game master guide pg 44
    global RND,skills,hand
    if RND == "T":
        x = 0
    if RND == "Y":
       x = random.randrange(0, 6)
    if RND == "N":
        if hand == 0:
            choices = ['BASIC']
        elif hand == 1:
            choices = ['EXPERT']
        elif hand == 2:
            choices == ['MARTIAL ARTS','COMMANDO']
        elif hand == 3:
            choices = ['ASSASSIN']
        elif hand == 99:
            choices = ['NONE','BASIC','EXPERT','MARTIAL ARTS','COMMANDO','ASSASSIN','Other Books']
        x = easygui.choicebox("Choose your Hand to Hand skill", title, choices)
        
    if x == 0 or x == 'NONE':
        NONE()
    if x ==1 or x == 'BASIC':
        if hand == 1: 
            BASIC()
            hand = 1
        else:
            if RND == "Y":
                x = random.randrange(2,5)
            if RND == "N":
                easygui.msgbox ("skill already used")
                Combat()        
    elif x == 2 or x == 'EXPERT':
        if hand >= 1: 
            EXPERT()
            hand = 2
        else:
            if RND == "Y":
                Combat()  
            if RND == "N":
                easygui.msgbox ("Requires Basic")
                Combat()  
    elif x == 3 or x == 'MARTIAL ARTS':
        if hand >= 2: 
            MARTIALARTS()
            hand = 3
        else:
            if RND == "Y":
                Combat()  
            if RND == "N":
                easygui.msgbox("Requires Expert")
                Combat()
    elif x == 4 or x =='COMMANDO':
        if hand >= 2: 
            COMMANDO()
            hand = 3
        else:
            if RND == "Y":
                Combat()  
            if RND == "N":
                easygui.msgbox("Requires Expert")
                Combat() 
    elif x == 5 or  x =='ASSASSIN':
        if hand >= 3: 
            ASSASSIN()
            hand = 4
        else:
            if RND == "Y":
                Combat()  
            if RND == "N":
                easygui.msgbox("Requires Martial Arts")
                Combat()
    else:
        #Other Books not emplemented yet
        print ("Other Books not implemented yet")
        easygui.msgbox( 'Other Books not implemented yet')
    return hand
def NONE():
    global combat,Dhit
    combat = ["HAND TO HAND: NONE"]
    Dhit = ["Punch attack does 1d4 points damage."]
    if level > 2:
        stats.attack = stats.attack +1
    if level > 8:
            stats.attack = stats.attack +1
    return combat, Dhit
def BASIC():
    global combat,Dhit
    combat = ["HAND TO HAND: BASIC"]
    combat.append("Level 1 Two attacks per melee; + 2 to pull/roll with punch,fall or impact.")
    if level > 0:
        Dhit = ["Punch attack does 1d4 points damage."]
        stats.attack = 2
        stats.roll=stats.roll +2
    combat.append("Level 2 +2 to parry and dodge.")
    if level > 1:
        stats.parry = stats.parry + 2
        stats.dodge = stats.dodge + 2
    combat.append("Level 3 Kick attack does 1D6 points damage.")
    if level > 2:
        Dhit.append("Kick attack does 1D6 points damage")
    combat.append("Level 4 + One additional attack per melee.")
    if level > 3:
        stats.attack = stats.attack + 1
    combat.append("Level 5 + 1 to strike.")
    if level > 4:
        stats.strike = stats.strike + 1
    combat.append("Level 6 Critical strike on an unmodified roll of 19 or 20.")
    if level > 5:
        Dhit.append("Critical strike on an unmodified roll of 19 or 20")
    combat.append("Level 7 + 2 to damage.")
    if level > 6:
        stats.damage = stats.damage + 2
    combat.append("Level 8 Judo-style body throw/flip; does 1D6 damage, and victim loses initiative and one attack per melee.")
    if level > 7:
        Dhit.append("Judo-style body throw/flip; does 1D6 damage, and victim loses initiative and one attack per melee")    
    combat.append("Level 9 + One additional attack per melee.")
    if level > 8:
        stats.attack = stats.attack + 1
    combat.append("Level 10 An additional +2 to pull/roll with punch, fall or impact.")
    if level > 9:
        stats.roll = stats.roll + 2
    combat.append("Level 11 An additional + 1 to parry and dodge.")
    if level > 10:
        stats.parry = stats.parry + 1
        stats.dodge = stats.dodge + 1
    combat.append("Level 12 An additional + 1 to strike.")
    if level > 11:
        stats.strike = stats.strike + 1
    combat.append("Level 13 Critical strike or knockout from behind.")
    if level > 12:
        Dhit.append("Critical strike or knockout from behind.")
    combat.append("Level 14 An additional +2 to damage.")
    if level > 13:
        stats.damage = stats.damage + 2
    combat.append("Level 15 + One additional attack per melee.")
    if level > 14:
        stats.attack = stats.attack +1
    
    return combat,Dhit
def EXPERT():
    global combat,Dhit
    combat  = ["HAND TO HAND: EXPERT"]
    combat.append("Level 1 Two attacks per melee to start; + 2 to pull/roll with punch,fall or impact.")
    if level > 0:
        Dhit = ["Punch attack does 1d4 points damage"]
        stats.attack = 2
        stats.roll=stats.roll + 2
    combat.append("Level 2 + 3 to parry and dodge.")
    if level > 1:
        stats.parry= stats.parry + 3
        stats.dodge= stats.parry + 3
    combat.append("Level 3 + 2 to strike.")
    if level > 2:
        stats.strike = stats.strike + 2
    combat.append("Level 4 + One additional attack per melee.")
    if level > 3:
        stats.attack = stats.attack + 1
    combat.append("Level 5 Kick attack does 1D6 damage.")
    if level > 4:
        Dhit.append("Kick attack does 1D6 damage.")
    combat.append("Level 6 Critical strike on an unmodified roll of 18, 19 or 20.")
    if level > 5:
        Dhit.append("Critical strike on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 7 Paired weapons.")
    if level > 6:
        Dhit.append("Paired weapons.")
    combat.append("Level 8 Judo-style body throw/flip; does 1D6 damage, and victim loses initiative and one attack.")
    if level > 7:
        Dhit.append("Judo-style body throw/flip; does 1D6 damage, and victim loses initiative and one attack.")
    combat.append("Level 9 + One additional attack per melee.")
    if level > 8:
        stats.attack=stats.attack+1
    combat.append("Level 10 +3 to damage.")
    if level > 9:
        stats.damage=stats.damage+3
    combat.append("Level 11 Knockout/stun on an unmodified roll of 18, 19 or 20.")
    if level > 10:
        Dhit.append("Knockout/stun on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 12 An additional +2 to parry and dodge.")
    if level > 11:
        stats.parry=stats.parry+2
        stats.dodge=stats.dodge+2
    combat.append("Level 13 Critical strike or knockout from behind (triple damage).")
    if level > 12:
        Dhit.append("Critical strike or knockout from behind (triple damage).")
    combat.append("Level 14 + One additional attack per melee.")
    if level > 13:
        stats.attack=stats.attack+1
    combat.append("Level 15 Death blow on a roll of natural 20.")
    if level > 14:
        Dhit.append("Death blow on a roll of natural 20.")
    return combat,Dhit
def MARTIALARTS():
    global combat,Dhit
    combat  = ["HAND TO HAND: MARTIALARTS"]
    combat.append("Level 1 Two attacks per melee to start; + 3 to pull/roll with punch, fall or impact.")
    if level > 0:
        Dhit = ["Punch attack does 1d4 points damage"]
        stats.attack = 2
        stats.roll=stats.roll + 3
    combat.append("Level 2 + 3 to parry and dodge; + 2 to strike.")
    if level > 1:
        stats.parry = stats.parry + 3
        stats.dodge = stats.dodge + 3
        stats.strike = stats.strike + 2
    combat.append("Level 3 Karate-style kick does 1D8 damage.")
    if level > 2:
        Dhit.append("Karate-style kick does 1D8 damage.")
    combat.append("Level 4 + One additional attack per melee.")
    if level > 3:
        stats.attack=stats.attack+1
    combat.append("Level 5 Jump Kick (critical strike). Entangle.")
    if level > 4:
        Dhit.append("Jump Kick (critical strike). Entangle.")
    combat.append("Level 6 Critical strike on an unmodified roll of 18, 19 or 20.")
    if level > 5:
        Dhit.append("Critical strike on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 7 Paired Weapons.")
    if level > 6:
        Dhit.append("Paired Weapons.")
    combat.append("Level 8 Leap Attack (critical strike).")
    if level > 7:
        Dhit.append("Leap Attack (critical strike).")
    combat.append("Level 9 + One additional attack per melee.")
    if level > 8:
        stats.attack=stats.attack+1
    combat.append("Level 10 Judo style body throw/flip; does 1D6 damage victim loses initiative and one attack.")
    if level > 9:
        Dhit.append("Judo style body throw/flip; does 1D6 damage victim loses initiative and one attack.")        
    combat.append("Level 11 An additional +4 to damage.")
    if level > 10:
        stats.damage=stats.damage+4
    combat.append("Level 12 An additional +2 to parry and dodge.")
    if level > 11:
        stats.parry=stats.parry+2
        stats.dodge=stats.dodge+2
    combat.append("Level 13 Knock-out/stun on an unmodified roll of 18, 19 or 20.")
    if level > 12:
        Dhit.append("Knock-out/stun on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 14 + One additional attack per melee.")
    if level > 13:
        stats.attack=stats.attack+1
    combat.append("Level 15 Death blow on a roll of a natural 20.")
    if level > 14:
        Dhit.append("Death blow on a roll of a natural 20.")
    return combat,Dhit
def ASSASSIN():
    global combat,Dhit
    combat = ["HAND TO HAND: ASSASSIN"]
    combat.append("Level 1 +2 to strike (one attack per melee).")
    if level > 0:
        Dhit = ["Punch attack does 1d4 points damage"]
        stats.attack = 1
        stats.strike=stats.strike + 2
    combat.append("Level 2 + 2 additional attacks per melee.")
    if level > 1:
        stats.attack=stats.attack+2
    combat.append("Level 3 +3 to pull/roll with punch/fall.")
    if level > 2:
        stats.roll=stats.roll+3
    combat.append("Level 4 +4 to damage.")
    if level > 3:
        stats.damage=stats.damage+4
    combat.append("Level 5 + One additional attack per melee.")
    if level > 4:
        stats.attack=stats.attack+1
    combat.append("Level 6 +3 to parry/dodge. Entangle.")
    if level > 5:
        stats.dodge=stats.dodge+3
    combat.append("Level 7 Knock-out/stun on an unmodified roll of 17-20.")
    if level > 6:
        Dhit.append("Knock-out/stun on an unmodified roll of 17-20.")
    combat.append("Level 8 + One additional attack per melee.")
    if level > 7:
        stats.attack=stats.attack+1
    combat.append("Level 9 Kick attack does 1D6 damage.")
    if level > 8:
        Dhit.append("Kick attack does 1D6 damage.")
    combat.append("Level 10 Critical strike on an unmodified roll of 19 or 20.")
    if level > 9:
        Dhit.append("Critical strike on an unmodified roll of 19 or 20.")
    combat.append("Level 11 +2 to strike.")
    if level > 10:
        stats.strike=stats.strike+2
    combat.append("Level 12 Death blow on a roll of a natural 20.")
    if level > 11:
        Dhit.append("Death blow on a roll of a natural 20.")
    combat.append("Level 13 + One additional attack per melee.")
    if level > 12:
        stats.attack=stats.attack+1
    combat.append("Level 14 +2 to damage.")
    if level > 13:
        stats.damage=stats.damage+2
    combat.append("Level 15 +2 to strike.")
    if level > 14:
        stats.strike=stats.strike+2
    return combat,Dhit
def COMMANDO():
    global combat,Dhit
    combat = ["HAND TO HAND: COMMANDO"]
    combat.append("Level 1 Starts with two attacks per melee round, paired weapons, body flip/throw, body block/tackle and +2 to save vs horror factor.")
    if level > 0:
        Dhit = ["Punch attack does 1d4 points damage"]
        Dhit.append("paired weapons")
        Dhit.append("body flip/throw")
        Dhit.append("body block/tackle")
        stats.attack = 2
        stats.horror=stats.horror + 2
    combat.append("Level 2 +1 on initiative, +1 to strike, +2 to parry and dodge, +3 to roll with punch/fall/impact, and +3 to pull punch. Backward sweep kick: Used only against opponents coming up behind the character. Does no damage; it is purely a knock-down attack (same penalties as body flip) but cannot be parried (an opponent can try to dodge it but is -2 to do so).")
    if level > 1:
        stats.inish=stats.inish+1
        stats.strike=stats.strike+1
        stats.dodge=stats.dodge+1
        stats.roll=stats.roll+3
        stats.pull=stats.pull+3
        #Dhit.append("+3 to pull punch.")
        Dhit.append("Backward sweep kick: Used only against opponents coming up behind the character. Does no damage; it is purely a knock-down attack (same penalties as body flip) but cannot be parried (an opponent can try to dodge it but is -2 to do so).")
    combat.append("Level 3 Disarm, +1 to automatic body flip.")
    if level > 2:
        #Dhit.append("Disarm, +1")
        stats.disarm=stats.disarm+1
        Dhit.append("automatic body flip.")
    combat.append("Level 4 + One additional attack per melee and Karate kick attack. This is a conventional, karate-style, kick. It starts with bringing the knee, folded, up to chest level, then the foot is completely extended. Does 2D6 damage.")
    if level > 3:
        stats.attack=stats.attack+1
        Dhit.append("Karate kick attack. This is a conventional, karate-style, kick. It starts with bringing the knee, folded, up to chest level, then the foot is completely extended. Does 2D6 damage.")
    combat.append("Level 5 Automatic dodge and critical body flip/throw.")
    if level > 4:
        Dhit.append("Automatic dodge and critical body flip/throw.")
    combat.append("Level 6 +2 on initiative, +1 to strike, parry and dodge, and +1 to body flip/throw.")
    if level > 5:
        stats.inish=stats.inish+2
        stats.strike=stats.strike+1
        stats.dodge=stats.dodge+1
        Dhit.append("+1 to body flip/throw.")
    combat.append("Level 7 +2 to damage, +1 to save vs horror factor, +1 to disarm, +1 to automatic dodge and +2 to pull punch.")
    if level > 6:
        stats.damage=stats.damage+2
        stats.horror=stats.horror+1
        stats.disarm = 1
        stats.pull = 1
        stats.dodge=stats.dodge +1
    combat.append("Level 8 + One additional attack per melee, jump kick, +1 to body flip/throw, and +1 to roll with punch/fall/impact. ")
    if level > 7:
        stats.attack=stats.attack+1
        Dhit.append("Jump kick")
        Dhit.append("+1 to body flip/throw")
        stats.roll=stats.roll+1
    combat.append("Level 9 Death blow on a natural 18-20!")
    if level > 8:
        Dhit.append("Death blow on a natural 18-20!")
    combat.append("Level 10 +2 to save vs horror factor, +1 on initiative and +1 to strike.")
    if level > 9:
        stats.horror=stats.horror+2
        stats.inish=stats.inish+1
        stats.strike=stats.strike+1
    combat.append("Level 11 +1 to disarm, +1 to pull punch and +1 to body flip/throw.")
    if level > 10:
        stats.disarm=stats.disarm+1
        stats.pull=stats.pull+1
        Dhit.append("+1 to body flip/throw")
        #stats.flip=stats.flip+1
    combat.append("Level 12 +2 to damage, +1 to parry and dodge, +2 to automatic dodge.")
    if level > 11:
        stats.damage+2
        stats.dodge=stats.dodge+1
        Dhit.append("+2 to automatic dodge.")
    combat.append("Level 13 +1 additional attack per melee.")
    if level > 12:
        stats.attack=stats.attack+1
    combat.append("Level 14 Automatic body flip/throw.")
    if level > 13:
        Dhit.append("Automatic body flip/throw.")
    combat.append("Level 15 Critical strike on a natural 17-20.")
    if level > 14:
        Dhit.append("Critical strike on a natural 17-20.")
    return combat,Dhit
main()
