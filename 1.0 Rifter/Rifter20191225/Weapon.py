#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

#Weapon.py
print ("Weapon.py")
import easygui, random
import stats

def main():
    global RND
    ImportStats()       
    wep = stats.wep
    print ("wep = %d" % wep)
    if stats.g == "G":
        msg = ("What kind of Data do you want?")
        title = ("Weapon.py")
        choices = ("User Input", "Random", "Test")
        x = easygui.choicebox(msg, title, choices)
        if x == "User Input":
            RND = "N"
        elif x == "Random":
            RND = "Y"
        elif x == "Test":
            RND = "T"
    if wep == 0 and RND == "T":
        wep = 1
    while wep > 0:
        print ("%d weapon of choice") % wep
        WEAPON()
        wep=wep-1
    ExportStats()

def ExportStats():
    stats.weapon = weapon
def ImportStats():
    global weapon, RND
    weapon = stats.weapon
    RND = stats.RND
    return weapon, RND

def WEAPON():
    global RND
    if RND == "Y" or RND =="T":
        x = random.randrange(1,3)
    if RND == "N":
        choice = ["Ancient Weapon","Modern Weapon"]
        msg = "Please choose Weapon category"
        title = "RIFTS"
	#print "1 - Ancient Weapon Proficiencies"
        #print "2 - Modern Weapon Proficiencies"
        x = easygui.choicebox(msg,title,choice)
    if x == 1 or x == "Ancient Weapon":
        AWEAPON()
    elif x == 2 or x == "Modern Weapon":
        MWEAPON()
    else:
        SKILLS()
def AWEAPON():
##Ancient Weapon Proficiencies
    global RND, weapon
    if RND == "T":
        x = 5
    if RND == "Y":
        x = random.randrange(1,15)
    if RND == "N":
        choice = ["Archery and Targeting","Axe","Blunt","Chain","Knife","Grappling Hook","Paired Weapons","Pole Arm","Quick Draw","Rope","Shield","Spear","Staff","Sword","Whip"]
        msg = "Please choose Weapon category"
        title = "RIFTS"		
        #print "1 - W.P. Archery and Targeting"
        #print "2 - W.P. Axe"
        #print "3 - W.P. Blunt"
        #print "4 - W.P. Chain"
        #print "5 - W.P. Knife"
        #print "6 - W.P. Grappling Hook"
        #print "7 - W.P. Paired Weapons"
        #print "8 - W.P. Pole Arm"
        #print "9 - W.P. Quick Draw"
        #print "10 - W.P. Rope"
        #print "11 - W.P. Shield"
        #print "12 - W.P. Spear"
        #print "13 - W.P. Staff"
        #print "14 - W.P. Sword"
        #print "15 - W.P. Whip"
        x = easygui.choicebox(msg,title,choice)
    if x ==1 or x == "Archery and Targeting":
        weapon.append("W.P. Archery and Targeting")
    elif x == 2 or x == "Axe":
        weapon.append("W.P. Axe")
    elif x == 3 or x == "Blunt":
        weapon.append("W.P. Blunt")
    elif x == 4 or x == "Chain":
        weapon.append("W.P. Chain")
    elif x == 5 or x == "Knife":
        weapon.append("W.P. Knife")
    elif x == 6 or x == "Grappling Hook":
        weapon.append("W.P. Grappling Hook")
    elif x == 7 or x == "Paired Weapons":
        weapon.append("W.P. Paired Weapons")
    elif x == 8 or x == "Pole Arm":
        weapon.append("W.P. Pole Arm")
    elif x == 9 or x == "Quick Draw":
        weapon.append("W.P. Quick Draw")
        weapon.append(" +1 initiative")
        weapon.append(" +2 initiative P.P. 18 - 23")
        weapon.append(" +3 initiative P.P. 24 - 30")
        weapon.append(" +4 initiative P.P 30+")    
    elif x == 10 or x == "Rope":
        weapon.append("W.P. Rope")
    elif x == 11 or x == "Shield":
        weapon.append("W.P. Shield")
    elif x == 12 or x == "Spear":
        weapon.append("W.P. Spear")
    elif x == 13 or x == "Staff":
        weapon.append("W.P. Staff")
    elif x == 14 or x == "Sword":
        weapon.append("W.P. Sword")
    elif x == 15 or x == "Whip":
        weapon.append("W.P. Whip")
    else:
        SKILLS()
    return weapon
	
def MWEAPON():
##Modern Weapon Proficiencies
    global RND,weapon
    if RND == "T":
        x = 4
    if RND == "Y":
        x = random.randrange(1,12)
    if RND == "N":
            choice = ["Revolver","Automatic Pistol","Bolt Action Rifle (hunting and sniping)","Shotgun","Automatic and Semi-automatic Rifles","W.P. Sub-Machinegun","W.P. Heavy Military Weapons","Military Flamethrowers","Harpoon & Spear Gun","Energy Pistol","Energy Rifle","Heavy Energy Weapons"]
            msg = "Please choose Weapon category"
            title = "RIFTS"
            x = easygui.choicebox(msg,title,choice)
#        print "1 - W.P. Revolver"
#        print "2 - W.P. Automatic Pistol"
#        print "3 - W.P. Bolt Action Rifle (hunting and sniping)"
#        print "4 - W.P. Shotgun"
#        print "5 - W.P. Automatic and Semi-automatic Rifles"
#        print "6 - W.P. Sub-Machinegun"
#        print "7 - W.P. Heavy Military Weapons"
#        print "8 - Military Flamethrowers"
#        print "9 - Harpoon & Spear Gun"
#        print "10 - W.P. Energy Pistol"
#        print "11 - W.P. Energy Rifle"
#        print "12 - W.P. Heavy Energy Weapons"
#        x= input ("Selection: ")

    if x == 1 or x == "Revolver":
        weapon.append("W.P. Revolver")
    elif x == 2 or x == "Automatic Pistol":
        weapon.append("W.P. Automatic Pistol")
    elif x == 3 or x == "Bolt Action Rifle (hunting and sniping)":
        weapon.append("W.P. Bolt Action Rifle (hunting and sniping)")
    elif x == 4 or x == "Shotgun":
        weapon.append("W.P. Shotgun")
    elif x == 5 or x == "Automatic and Semi-automatic Rifles":
        weapon.append("W.P. Automatic and Semi-automatic Rifles")
    elif x == 6 or x == "W.P. Sub-Machinegun":
        weapon.append("W.P. Sub-Machinegun")
    elif x == 7 or x == "W.P. Heavy Military Weapons":
        weapon.append("W.P. Heavy Military Weapons")
    elif x == 8 or x == "Military Flamethrowers":
        weapon.append("W.P. Military Flamethrowers")
    elif x == 9 or x == "Harpoon & Spear Gun":
        weapon.append("W.P. Harpoon & Spear Gun")
    elif x == 10 or x == "Energy Pistol":
        weapon.append("W.P. Energy Pistol")
    elif x == 11 or x == "Energy Rifle":
        weapon.append("W.P. Energy Rifle")
    elif x == 12 or x == "Heavy Energy Weapons":
        weapon.append("W.P. Heavy Energy Weapons")
    else:
        SKILLS()
    return weapon
###Weapon Skills
##def WEAPON():
##    global RND
##    if RND == "Y":
##        x = random.randrange(1,3)
##    if RND == "N":
##        print "1 - Ancient Weapon Proficiencies"
##        print "2 - Modern Weapon Proficiencies"
##        x= input ("Selection: ")
##    if x == 1:
##        AWEAPON()
##    elif x == 2:
##        MWEAPON()
##    else:
##        SKILLS()
##def AWEAPON():
####Ancient Weapon Proficiencies
##    global RND,skills
##    if RND == "Y":
##        x = random.randrange(1,16)
##    if RND == "N":
##        print "1 - W.P. Archery and Targeting"
##        print "2 - W.P. Axe"
##        # W.P. Battle Axe
##        print "3 - W.P. Blunt"
##        #W.P. Bola
##        #W.P. Boomerang
##        #W.P. Bow
##        print "4 - W.P. Chain"
##        #W.P. Crossbow
##        #W.P. Deadball
##        #W.P. Forked
##        print "5 - W.P. Knife"
##        print "6 - W.P. Grappling Hook"
##        #W.P. Mouth Weapons
##        #W.P. Net
##        print "7 - W.P. Paired Weapons"
##        print "8 - W.P. Pole Arm"
##        print "9 - W.P. Quick Draw"
##        print "10 - W.P. Rope"
##        print "11 - W.P. Shield"
##        #W.P. Siege Weapons
##        #W.P. Slingshot
##        #W.P. Small Thrown Weapons
##        print "12 - W.P. Spear"
##        print "13 - W.P. Staff"
##        print "14 - W.P. Sword"
##        #W.P. Trident
##        print "15 - W.P. Whip"
##        x= input ("Selection: ")
##    if x ==1:
##        weapon.append("W.P. Archery and Targeting")
##    elif x == 2:
##        weapon.append("W.P. Axe")
##    elif x == 3:
##        weapon.append("W.P. Blunt")
##    elif x == 4:
##        weapon.append("W.P. Chain")
##    elif x == 5:
##        weapon.append("W.P. Knife")
##    elif x == 6:
##        weapon.append("W.P. Grappling Hook")
##    elif x == 7:
##        weapon.append("W.P. Paired Weapons")
##    elif x == 8:
##        weapon.append("W.P. Pole Arm")
##    elif x == 9:
##        weapon.append("W.P. Quick Draw")
##        weapon.append(" +1 initiative")
##        weapon.append(" +2 initiative P.P. 18 - 23")
##        weapon.append(" +3 initiative P.P. 24 - 30")
##        weapon.append(" +4 initiative P.P 30+")    
##    elif x == 10:
##        weapon.append("W.P. Rope")
##    elif x == 11:
##        weapon.append("W.P. Shield")
##    elif x == 12:
##        weapon.append("W.P. SPear")
##    elif x == 13:
##        weapon.append("W.P. Staff")
##    elif x == 14:
##        weapon.append("W.P. Sword")
##    elif x == 15:
##        weapon.append("W.P. Whip")
##    else:
##        SKILLS()
##    return skills
##def MWEAPON():
####Modern Weapon Proficiencies
##    global RND,skills
##    if RND == "Y":
##        x = random.randrange(1,13)
##    if RND == "N":
##        print "1 - W.P. Revolver"
##        print "2 - W.P. Automatic Pistol"
##        print "3 - W.P. Bolt Action Rifle (hunting and sniping)"
##        print "4 - W.P. Shotgun"
##        print "5 - W.P. Automatic and Semi-automatic Rifles"
##        print "6 - W.P. Sub-Machinegun"
##        print "7 - W.P. Heavy Military Weapons"
##        #W.P. Grenade Launcher
##        print "8 - W.P. Military Flamethrowers"
##        print "9 - W.P. Harpoon & Spear Gun"
##        print "10 - W.P. Energy Pistol"
##        print "11 - W.P. Energy Rifle"
##        print "12 - W.P. Heavy Energy Weapons"
##        #W.P. Sharpshooting
##        x= input ("Selection: ")
##    if x == 1:
##        weapon.append("W.P. Revolver")
##    elif x == 2:
##        weapon.append("W.P. Automatic Pistol")
##    elif x == 3:
##        weapon.append("W.P. Bolt Action Rifle (hunting and sniping)")
##    elif x == 4:
##        weapon.append("W.P. Shotgun")
##    elif x == 5:
##        weapon.append("W.P. Automatic and Semi-automatic Rifles")
##    elif x == 6:
##        weapon.append("W.P. Sub-Machinegun")
##    elif x == 7:
##        weapon.append("W.P. Heavy Military Weapons")
##    elif x == 8:
##        weapon.append("W.P. Military Flamethrowers")
##    elif x == 9:
##        weapon.append("W.P. Harpoon & Spear Gun")
##    elif x == 10:
##        weapon.append("W.P. Energy Pistol")
##    elif x == 11:
##        weapon.append("W.P. Energy Rifle")
##    elif x == 12:
##        weapon.append("W.P. Heavy Energy Weapons")
##    else:
##        SKILLS()
##    return skills
main()
