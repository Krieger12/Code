#!/user/bin/env python
# -*- coding: cp1252 -*-
# RIFTS Coaption char gen
# Created by Keith Marrs-Olson
# This is to create a print of the character
## expand on this section
import stats
import easygui,sys
import random, os
def main():
    ImportStats()
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND,weapon
    Printhtml(IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,attack,inish,dodge,strike,roll,skills,race,OCC,ISP,PPE,Psionic,damage,combat,equipment,weapon)
    return

def Printhtml(IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,attack,inish,dodge,strike,roll,skills,race,OCC,ISP,PPE,Psionic,damage,combat,equipment,weapon):
    Name = "Your_New_Monster.html"
    f = open(Name, 'w')
    print>>f, ("<!DOCTYPE html>")
    print>>f, ("<html>")
    print>>f, ("<head>")
    print>>f, ("<title>%s Pirate Character</title>") % Name
    print>>f, ("</head>")
    print>>f, ("<body style=\"background-color:black;font-size:20px\">")
    print>>f, ("<font style=\"color:white\">")
    print>>f, (" ")
    print>>f, ("<h1> %s </h1>") % OCC
    print>>f, ("<div style=\"float: left; width: 33%;\">")
    print>>f, ("<p>Intelpgence Quotient: %s </p>") % IQ
    print>>f, ("<p> Physical Strength: %s </p>") % PS
    print>>f, ("<p> Physical Prowess: %s </p>") % PP
    print>>f, ("<p> Physical Endurance: %s </p>") % PE
    if PE > HP:
        HP = PE
    print>>f, ("<p> Speed: %s </p>") % Speed
    print>>f, "<p> </p>"
    print>>f, "</div>"
    print>>f, ("<div style=\"float: left; width: 33%;\">")
    print>>f, ("<p> Hit Points: %s </p>") % HP
    print>>f, ("<p> SDC: %s </p>") % SDC
    print>>f, ("<p> MDC: %s </p>") % MDC
    print>>f, ("<p> ISP: %s </p>") % ISP
    print>>f, ("<p> PPE: %s </p>") %ISP
    print>>f, ("</div>")
    print>>f, ("<div style=\"float: left; width: 33%;>\"")
    print>>f, ("<p> Number of Attacks %s </p>") %attack 
    print>>f, ("<p> Damage + %s </p>") % damage
    print>>f, ("<p> Strike + %s </p>") % strike
    print>>f, ("<p> Dodge + %s </p>") % dodge
    print>>f, ("<p> Roll with punch or fall + %s </p>") % roll
    print>>f, ("<p> Parry attack + %s </p>") % parry
    print>>f, ("<p> Initiative + %s </p>") % inish
    print>>f, ("<p> Horror + %s </p>") % horror
    print>>f, ("</div>")
##    print>>f, ("<div style=\"float: left; width: 33%;>\"")
##    #this portion of code will only work on Keith's Computer
##    path = "E:\PiratePics\\"
##    random_filename = random.choice([
##        x for x in os.listdir(path)
##        if os.path.isfile(os.path.join(path, x))
##        ])
##    print(random_filename)
##    picfile = 'file:///E:/PiratePics/'+random_filename
##    print (picfile)
##    print>>f, ('<A HREF="%s"><IMG HEIGHT=150 WIDTH=200 SRC="%s"></A>') % (random_filename, picfile) #  max-width:75%% max-height:75%%
##    #end custome picture import
##    print>>f, ("<p> %s </p>") % combat[0]
##    d = len(weapon)
##    print>>f, "<p> </p>"
##    for r in range (0,d):
##        print>>f, ("<li> %s </li>")% weapon[r]
##    print>>f, ("</div>")
    print>>f, ("<div style=\"float: left; width: 100%;>\"")
    print>>f, ("<p>   </p>")
    d = len(skills)
    for r in range (0,d):
        print>>f, ("<li> %s </li>")% skills[r]
    d = len(race)
    for R in range (0,d):
        print>>f, ("<li> %s </li>")% race[R]
    print>>f, "<p> </p>"
    d = len(equipment)
    for r in range (0,d):
        print>>f, ("<li> %s </li>")% equipment[r]
    """
    if stats.RND == "Y":
        
        easygui.choicebox(title,msg,choices)
    if stats.RND == R or stats.RND == "Y"
    d = len(Psionic)
    for r in range (0,d):
        print>>f, ("<li> %s </li>") % Psionic[r]
        """

    print>>f, "<p> \" \" </p>"
    d = len(combat)
    print>>f, "<p> </p>"
    for r in range (0,d):
        print>>f, ("<li> %s </li>")% combat[r]

    print>>f, ("</div>")
    print>>f, "</body>"
    print>>f, "</html>"
    n = sys.path[0]+"\\"+Name
##    easygui.msgbox ("Your Character can be found at: \n"+ n, title="Rifts Pirate Gen")
    import webbrowser
    webbrowser.open(n)
    return
def ImportStats():
    global IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND,weapon, horror
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
    weapon = stats.weapon
    race = stats.race
    OCC = stats.OCC
    Psionic = stats.Psionic
    combat = stats.combat
    equipment = stats.equipment
    RND = stats.RND
    horror = stats.horror
    return IQ,ME,MA,PS,PP,PE,PB,Speed,HP,SDC,MDC,ISP,PPE,attack,inish,strike,roll,damage,roll,parry,dodge,skills,race,OCC,Psionic,combat,equipment,RND,weapon, horror

main()
