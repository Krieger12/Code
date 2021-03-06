#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson
#combat.py
print ("combat.py")

###Hand Skills
##'BASIC' =1
##'EXPERT' = 2
##'MARTIAL ARTS' = 3
##'COMMANDO'  = 3
##'ASSASSIN' = 4
##'Other
import easygui, random, stats
global skills,hand,RND
RND = stats.RND
def main():
    #import skills
    ImportStats()
    if stats.combat[0] == "SELECT" or stats.hand == 0:
        Combat()
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
    print (combat)
    #elif stats.combat == "BASIC":
    ExportStats()
def ImportStats():
    global skills,hand,RND,combat
    hand = stats.hand
    skills = stats.skills
    combat=stats.combat
    #RND = stats.RND
    return hand,skills,RND, combat
def ExportStats():
    global skills,hand,combat
    stats.hand = hand
    stats.skills = skills
    stats.combat = combat

def Combat():
    #Rifts game master guide pg 44
    global RND,skills,hand
    if RND == "T":
        x = 1
    if RND == "Y":
       x = random.randrange(1, 6)
    if RND == "N":
        x = easygui.choicebox ("Choose your Hand to Hand skill", title="Rifts Pirate Gen", choices = ['BASIC','EXPERT','MARTIAL ARTS','COMMANDO','ASSASSIN','Other Books'] )
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
        print ("Other Books not emplemented yet")
        easygui.msgbox( 'Other Books not emplemented yet')
    return hand
def BASIC():
    global combat
    stats.attack,stats.roll=2,2
    combat = ["HAND TO HAND: BASIC"]
    combat.append("Level 1 Two attacks per melee; + 2 to pull/roll with punch,fall or impact.")
    combat.append("Level 2 +2 to parry and dodge.")
    combat.append("Level 3 Kick attack does 1D6 points damage.")
    combat.append("Level 4 + One additional attack per melee.")
    combat.append("Level 5 + 1 to strike.")
    combat.append("Level 6 Critical strike on an unmodified roll of 19 or 20.")
    combat.append("Level 7 + 2 to damage.")
    combat.append("Level 8 Judo-style body throw/flip; does 1D6 damage, and victim loses initiative and one attack per melee.")
    combat.append("Level 9 + One additional attack per melee.")
    combat.append("Level 10 An additional +2 to pull/roll with punch, fall or impact.")
    combat.append("Level 11 An additional + 1 to parry and dodge.")
    combat.append("Level 12 An additional + 1 to strike.")
    combat.append("Level 13 Critical strike or knockout from behind.")
    combat.append("Level 14 An additional +2 to damage.")
    combat.append("Level 15 + One additional attack per melee.")
    return combat
def EXPERT():
    global combat,attack,roll
    stats.attack,stats.roll=2,2
    combat  = ["HAND TO HAND: EXPERT"]
    combat.append("Level 1 Two attacks per melee to start; + 2 to pull/roll with punch,fall or impact.")
    combat.append("Level 2 + 3 to parry and dodge.")
    combat.append("Level 3 + 2 to strike.")
    combat.append("Level 4 + One additional attack per melee.")
    combat.append("Level 5 Kick attack does 1D6 damage.")
    combat.append("Level 6 Critical strike on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 7 Paired weapons.")
    combat.append("Level 8 Judo-style body throw/flip; does 1D6 damage, and victim loses initiative and one attack.")
    combat.append("Level 9 + One additional attack per melee.")
    combat.append("Level 10 +3 to damage.")
    combat.append("Level 11 Knockout/stun on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 12 An additional +2 to parry and dodge.")
    combat.append("Level 13 Critical strike or knockout from behind (triple damage).")
    combat.append("Level 14 + One additional attack per melee.")
    combat.append("Level 15 Death blow on a roll of natural 20.")
    return combat
def MARTIALARTS():
    global combat,attack,roll
    stats.attack,stats.roll=2,3
    combat  = ["HAND TO HAND: MARTIALARTS"]
    combat.append("Level 1 Two attacks per melee to start; + 3 to pull/roll with punch, fall or impact.")
    combat.append("Level 2 + 3 to parry and dodge; + 2 to strike.")
    combat.append("Level 3 Karate-style kick does 1D8 damage.")
    combat.append("Level 4 + One additional attack per melee.")
    combat.append("Level 5 Jump Kick (critical strike). Entangle.")
    combat.append("Level 6 Critical strike on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 7 Paired Weapons.")
    combat.append("Level 8 Leap Attack (critical strike).")
    combat.append("Level 9 + One additional attack per melee.")
    combat.append("Level 10 Judo style body throw/flip; does 1D6 damage victim loses initiative and one attack.")
    combat.append("Level 11 An additional +4 to damage.")
    combat.append("Level 12 An additional +2 to parry and dodge.")
    combat.append("Level 13 Knock-out/stun on an unmodified roll of 18, 19 or 20.")
    combat.append("Level 14 + One additional attack per melee.")
    combat.append("Level 15 Death blow on a roll of a natural 20.")
    return combat
def ASSASSIN():
    global combat,strike
    stats.strike=2
    combat = ["HAND TO HAND: ASSASSIN"]
    combat.append("Level 1 +2 to strike (one attack per melee).")
    combat.append("Level 2 + 2 additional attacks per melee.")
    combat.append("Level 3 +3 to pull/roll with punch/fall.")
    combat.append("Level 4 +4 to damage.")
    combat.append("Level 5 + One additional attack per melee.")
    combat.append("Level 6 +3 to parry/dodge. Entangle.")
    combat.append("Level 7 Knock-out/stun on an unmodified roll of 17-20.")
    combat.append("Level 8 + One additional attack per melee.")
    combat.append("Level 9 Kick attack does 1D6 damage.")
    combat.append("Level 10 Critical strike on an unmodified roll of 19 or 20.")
    combat.append("Level 11 +2 to strike.")
    combat.append("Level 12 Death blow on a roll of a natural 20.")
    combat.append("Level 13 + One additional attack per melee.")
    combat.append("Level 14 +2 to damage.")
    combat.append("Level 15 +2 to strike.")
    return combat,strike
def COMMANDO():
    global combat,attack
    stats.attack=2
    combat = ["HAND TO HAND: COMMANDO"]
    combat.append("Level 1 Starts with two attacks per melee round, paired weapons, body flip/throw, body block/tackle and +2 to save vs horror factor.")
    combat.append("Level 2 +1 on initiative, +1 to strike, +2 to parry and dodge, +3 to roll with punch/fall/impact, and +3 to pull punch. Backward sweep kick: Used only against opponents coming up behind the character. Does no damage; it is purely a knock-down attack (same penalties as body flip) but cannot be parried (an opponent can try to dodge it but is -2 to do so).")
    combat.append("Level 3 Disarm, +1 to automatic body flip.")
    combat.append("Level 4 + One additional attack per melee and Karate kick attack. This is a conventional, karate-style, kick. It starts with bringing the knee, folded, up to chest level, then the foot is completely extended. Does 2D6 damage.")
    combat.append("Level 5 Automatic dodge and critical body flip/throw.")
    combat.append("Level 6 +2 on initiative, +1 to strike, parry and dodge, and +1 to body flip/throw.")
    combat.append("Level 7 +2 to damage, +1 to save vs horror factor, +1 to disarm, +1 to automatic dodge and +2 to pull punch.")
    combat.append("Level 8 + One additional attack per melee, jump kick, +1 to body flip/throw, and +1 to roll with punch/fall/impact. ")
    combat.append("Level 9 Death blow on a natural 18-20!")
    combat.append("Level 10 +2 to save vs horror factor, +1 on initiative and +1 to strike.")
    combat.append("Level 11 +1 to disarm, +1 to pull punch and +1 to body flip/throw.")
    combat.append("Level 12 +2 to damage, +1 to parry and dodge, +2 to automatic dodge.")
    combat.append("Level 13+ One additional attack per melee.")
    combat.append("Level 14 Automatic body flip/throw.")
    combat.append("Level 15 Critical strike on a natural 17-20.")
    return combat
main()
