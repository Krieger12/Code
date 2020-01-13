#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson

# Dog Boy Characeter


import easygui,random
import stats
title = "Dogboy.py"
RND=stats.RND
if RND == "G":
    RND = "N"
def main():
    print ("dogboy.py")
    ImportStats()
    dog()
    #ExportStats()
        
def dog():
    global RND,PPE,ISP,PS,PE,Speed,SDC,skills,OCC,race,PSkillNumb,SkillNumb,equipment
    stats.OCC = 'Dog Boy'
    stats.SDC == 2
    import SDC
    stats.inish=stats.inish+1
    skills=stats.skills
    skills.append("O.C.C. Skills:")
    skills.append("Language: American 88% +1%/level")
    skills.append("Intelligence 38%+ 4)")
    skills.append("Radio: Basic 55% +5")
    skills.append("Pilot Hovercraft 60% +5")
    skills.append("Read Sensory Equipment 40% +5")
    skills.append("Weapon Systems 50% +5")
    skills.append("Climbing 50% +5")
    skills.append("Running")
    stats.PE=stats.PE+1
    if RND == "T":
        stats.Speed=stats.Speed+1
        stats.SDC=stats.SDC+1
    if RND == "Y":
        z = random.randrange(4,19)
        stats.Speed=stats.Speed+z
        z = random.randrange(1,7)
        stats.SDC=stats.SDC+z
    if RND == "N":
        msg = "Running Bonus"
        title="Rifts Gen"
        SDC = "SDC bonus roll 3d6 :"
        Speed="Speed bonus roll 2d6 :"
        fieldNames = [SDC,Speed]
        fieldValues = []
        x=1
        while x==1:
            errmsg = ""    
            fieldValues = easygui.multenterbox(msg,title, fieldNames)
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg = ('"%s" is a required field.\n\n' % i)
                    easygui.msgbox(errmsg)
            if errmsg == "": x=0# no problems found
            for i in range(len(fieldNames)):
                print (fieldNames[i],fieldValues[i])
        stats.SDC = stats.SDC + int(fieldValues[0])
        stats.Speed = stats.Speed + int(fieldValues[1])
    skills.append("Land Navigation 46% +4")
    skills.append("Wilderness Survival 40% +5")
    weapon=stats.weapon
    weapon.append("W.P. Energy Pistol")
    weapon.append("W.P. Energy Rifle W.P.")
    stats.wep=stats.wep+1
    stats.hand = 2     #Hand to Hand: Martial Arts
    stats.PSkillNumb,stats.SkillNumb = 5,8
# dogboy bonusus
    stats.SDC = stats.SDC + 20
    stats.inish = stats.inish + 2
    stats.dodge = stats.dodge + 1
    stats.strike = stats.strike + 1
    stats.parry = stats.parry + 1
    if RND == "T":
        stats.ISP = stats.ISP+1
        stats.PPE = stats.PPE+1
        stats.PE = stats.PE+1
        stats.PS=stats.PS+1
        stats.Speed=stats.Speed+1
    if RND == "Y":
        z=random.randrange(1,7)
        z=z*10
        ISP=stats.ME+z
        stats.ISP = stats.ISP+z
        z = random.randrange(3,19)
        stats.PPE=stats.PPE+z
        z = random.randrange(1, 5)
        stats.PE = stats.PE+z
        z = random.randrange(1, 5)
        stats.PS=stats.PS+z
        z = random.randrange(2, 13)
        stats.Speed=stats.Speed+z
    if RND == "N":
        ISP = "ISP bonus roll 1d6"
        PPE = "PPE bonus roll 3d6"
        PE = "PE bonus roll 1d4"
        PS = "PS bonus roll 1d4"
        Speed = "Speed bonus roll 2d6"
        fieldNames = [ISP, PPE, PE, PS, Speed]
        fieldValues = []  # we start with blanks for the values
        # make sure that none of the fields was left blank
        x = 1
        while x == 1:
            errmsg = ""
            fieldValues = easygui.multenterbox("Dogboy Bonuses", title, fieldNames)
            for i in range(len(fieldNames)):
                if fieldValues[i].strip() == "":
                    errmsg = ('"%s" is a required field.\n\n' % i)
                    easygui.msgbox(errmsg)
            if errmsg == "": x = 0  # no problems found
        # records values
        for i in range(len(fieldNames)):
            print (i, fieldNames[i], fieldValues[i])
        #stats.SDC = stats.SDC + int(fieldValues[0])
        #stats.Speed = stats.Speed + int(fieldValues[])
        z = int(fieldValues[0])*10
        stats.ISP = stats.ISP + z
        stats.PPE = stats.PPE + int(fieldValues[1])
        print PPE[1]
        print stats.PPE
        stats.PE = stats.PE + int(fieldValues[2])
        stats.PS = stats.PS + int(fieldValues[3])
        stats.Speed = stats.Speed + int(fieldValues[4])

    race=stats.race

    simp = "Simple"
    #if stats.RND == "N":
    #    simp=easygui.buttonbox ("Do you want extended or simplified Dogboy output", title="Rifts Character Generator", choices = ['Extended', 'Simple'] )

    if simp == "Simple":
        race.append("Special Dog Boy Abilitys")
        race.append("1 Sense psychic and magic energy 40% +5")
        race.append("2 Sense supernatural beings 62% +2")
        race.append("3 Psi-Bonuses")
        race.append("4 Other Psionic Powers:")
        Psionic = ["Psionic Powers"]
        Psionic.append("sense evil")
        Psionic.append("sense magic")
        Psionic.append("sixth sense")
        Psionic.append("empathy (receiver only, not transmission)")
        Psionic.append("     plus choice of one other from the sensitive category.")
        race.append("5 Physical Bonuses")
        race.append("Bite attack inflicts 1D6 S.D.C. damage")
        race.append("6 Superior sense of smell 70% + 3")
        skills.append("Track by smell alone 40% + 4%")
        skills.append("Identify specific odour 54% +2")
        race.append("7 Keen hearing")
        race.append("8 Instinctive hunters")
        race.append("9 Instinctive pack animals")
            
    elif simp == "Extended":
        print ("not all extended dog boy power explanations are not supported at this time")

        race.append(' ')
        race.append('Mutant Dog Powers')
        race.append('Sense Psychic and Magic Energy:')
        race.append("    Range: 50 feet (15 m)")
        race.append('    Base Skill: 8% + 2')
        race.append("    Active Magic Range: 400 foot (121 m) area +50 (15 m)/level")
        race.append('    Base Skill: 40% + 5')
        race.append('    Duration: Automatic and constant')
        race.append('Sense supernatural beings')
        race.append("    Range: 100 feet (30.5 m)")
        race.append('    Base Skill: 35% + 5')
        race.append("    Active Magic Range: 1000 feet (305 m) + 100 feet (30.5 m)/level")
        race.append('    Base Skill: 70% +3')
        race.append('    Duration: Automatic and constant')
        race.append('Psi-Bonuses: As a master psionic, the psi-hound needs to roll a 10 or higher to save versus psionic attack')
        race.append(' ')
        race.append("More info on Dog Boy O.C.C. can be cound in the Rifts Main Book  pg 107")
        race.append("Or Ultimate Edition pg 144")
        equipment.append("Standard Equipment: Two energy weapons of choice and two ancient weapons (sword, mace, etc.), meat hook (1D6 S.D.C./H.P. damage), billy club (2D4 S.D.C./H.P. damage), dagger, a suit of M.D.C. body armor, 1D4 pairs of handcuffs, mess kit, canteen or water skin, sleeping bag, backpack, fishing hooks and line, 100 feet (30.5 m) of rope and a grappling hook, flashlight, cigarette lighter, pack of cigarettes, comb, pocket mirror, binoculars, and sunglasses or tinted goggles. Specialized vehicles (jet skies, row boat, etc.), weapons, and equipment may be provided by the Captain or sponsor of the mission if the pirates are working for somebody else or as Privateers. However, individuals are generally expected to acquire and maintain their own gear, whether it be as little as a gun and life jacket to a suit of power armor and a trunk full of weapons.")
        equipment.append(' ')    
        equipment.append("Money: Starts with 1D4x1OOO in creditis and 1D4xlOOO in saleable black market/trade items. The Captain of the ship typically provides his crew with a sleeping bunk, fresh water and lousy to excellent food depending on each individual ship. Some also provide some measure of medical care (again, can vary from lousy to excellent).")
        equipment.append(' ')
        equipment.append("Cybernetics: None to start, but pirates often acquire 1D4 cybernetic implants or one bionic limb.")
    elif simp == "Extended":
        print ("not all extended dog boy power explenations are not supported at this time")
                    
##race.append(' ')
##race.append('Mutant Dog Powers')
##race.append("1. Sense Psychic and Magic Energy: Basically like a bloodhound smelling a familiar scent, the psi-hound can detect the presence of psychic energy; specifically, fellow psionics (I.S.P.) and magic (P.P.E. specifically oriented toward magic, techno-wizardry and wizardry devices). The ability is constant and automatic, just like the psi-stalker. Range: 50 feet (15m). Unlike the stalker, the dog has little chance of recognizing that specific person's psychic scent again. Base Skill: 8% + 2% per additional level of experience. If the mutant has a bit of hair, skin, blood, or an article of clothing recently (4 hours or less) worn by the subject being hunted, the ability to follow the psychic trail enjoys a bonus of + 10%. If a psionic power or magic is being used within the range of sensitivity, he will sense that too. If the energy is being continually expended, like a series of magic or psionic attacks, or a long duration effect, he can track it to the source with ease. Base Skill: 40% + 5% per level of experience (roll once every melee). It is also possible that the character will recognize the scent again if encountered at some other time; 10% +4% per level of experience. Range: Sensitivity to a fellow psychic or magic practitioner not using his powers is 50 feet (15 m) +5 feet (1.5 m) per each additional level of experience. Sensitivity to psionic and magic powers being used is a 400 foot (121 m) area +50 (15 m) per level of experience. When tracking a psychic scent, roll percentile dice every 1000 feet (305 m) to see if the hunter is still on the trail. Duration: Automatic and constant. I.S.P.:None, automatic ability.")
##race.append('2. Sense supernatural beings: Identical in function to the previous ability, except the mutant dog is much more sensitive to the very distinctive psychic scent of the supernatural. Base Skill: 62% + 2% per level of experience. The ability to identify the specific type of paranormal creature is Base Skill: 62% + 2% per level of experience, and includes demons, vampires, and dragons. The tracking by scent Base Skill is 35% + 5% per level of experience. 70% +3% per level of experience if the supernatural being is using psionics or magic. Range: Sensitivity to the presence of a supernatural being when it is not using its powers is 100 feet (30.5 m) per level of experience. Sensitivity to supernatural creatures or magic being used is 1000 feet (305 m) + 100 feet (30.5 m) per additional level of experience. Duration: Automatic and constant. I.S.P.: None, automatic. NOTE: Close proximity to ley lines and nexus points disrupts the psychic senses.')
##race.append('3. Psi-Bonuses: As a master psionic, the psi-hound needs to roll a 10 or higher to save versus psionic attack and enjoys a bonus of + 1 to save vs psionic attack.')
##race.append('4. Other Psionic Powers: The Dog Pack character automatically gets the following psychic Sensitive powers: sense evil, sense magic, sixth sense, and empathy (receiver only, not transmission), plus choice of one other from the sensitive category.')
##race.append('5. Physical Bonuses: All Dog Boys, regardless of breed, get the following bonus rolls and attribute modifications: + 20 on physical S.D.C., + 2 on initiative roll, +1 to strike, parry, and dodge, +1D4 to P.E. attribute, 1D4 to P.S. attribute, +2D6 to speed attribute. Bite attack inflicts 1D6 S.D.C. damage. Physical endurance as it applies to weight/load and exertion is two times greater than for normal humans. ')
##race.append('Physical appearance: Human looks, none. The head/face is that of a canine, the body is fur covered, and there is a tail. Hands, full; possess fully articulated hands with human-like opposable thumbs and developed arms. Bipedal stance, usually full, although some are partial and like to run on all fours, but can stand and walk erect. Human speech, partial (occasionally full). Usually speech is a bit guttural and the character still has a tendency to growl, whimper, and howl when excited. Size varies from about four feet to six feet tall (1.2 to 1.8 meters); size levels 6-12. German shepherds, blood hounds, terriers, and spaniels are the most frequently transformed types of dog. However, experiments have included many other breeds, as well as coyotes, wolves, foxes and bears. NOTE: Fun Fact: Dogs have limited color vision. 6. Superior sense of smell. Dogs are a million times more aware of smells than a normal human. The mutant dog soldier is no exception. The character can follow a scent trail that is four days old and recognize an odor from smelling only a few molecules. Specific abilities are: Recognize and accurately identify general/common/known smells, including gases, food, and other distinctive odors. Range: 100 feet (30.5 m) per level of experience. Base Skill: 70% + 3% per level of experience. Identify specific odors, including the scent of specific individuals, items, or monsters. Range: 25 feet (7.6 m) per level of experience. Base Skill: 54% + 2% per level of experience. Track by smell alone! Does not follow tracks or any other visible trail. This also means that a mutant dog can sniff his way through total darkness if there is a scent that can be followed. This also means that the character suffers only half the normal penalties to strike, parry, and dodge when blinded or in darkness (can smell and hear his opponent). Range: Roll once for every 1000 feet (305 m). Base Skill: 40% + 4% per level of experience. A failed roll means the trail has been temporarily lost. Two successful rolls out of three tries means the trail has been rediscovered. Two failures means the trail is lost. Note: The psi-hound can smell a scent that is as much as four days old (96 hours), as long as the trail has not been washed away. Can not track through water. Also, despite what many people may think, a dog can not see any better in the dark than humans. However, their exceptional sense of smell and keen hearing helps compensate while in the darkness. 7. Keen hearing. The mutant can hear into a higher range of sound than humans and is more alert and sensitive to sounds. This is evident in some of the physical bonuses. 8. Instinctive hunters, they notice movement and give chase. This accounts for bonuses to strike, parry and dodge. 9. Instinctive pack animals. Loyal and group oriented, most mutant dogs work well in groups and prefer to be in a group than alone. This also affects the character's alignment. Most will be principled, scrupulous, unprincipled, or aberrant (evil). Characters who are anarchist, miscreant, or diabolic, tend to be loners, mean, and do not work well in a group unless they can be the leader.')
##race.append('Attribute Requirements: None, other than must be an intelligent mutant dog.')
##race.append('Other than the physical bonus rolls listed under Mutant Dog Powers #5, roll the usual 3D6 dice to determine the eight attributes.')
##race.append('The influence of ley line energy Ley lines and nexus points impair and even obliterate the psi-hound's psychic sensing and tracking abilities. However, the creatures normal physical abilities/tracking by smell are not affected and the other psychic')
##race.append('sensitive abilities are enhanced. Range and duration are increased by 50% when near a ley line and doubled when within a mile (1.6 km) of a nexus point.')
##race.append('P.P.E.: Most of the individual's P.P.E. has been expended in the development of psychic abilities. The remaining Permanent P.P.E. Base is 3D6.
##race.append('I.S.P.: To determine the character's initial amount of Inner Strength Points, take the number of M.E. as the base, roll 1D6x10 and add it to the base number. The character gets another 10 I.S.P. for each additional level of experience. Considered a master psionic. I.S.P. is regained at the rate of 2 per hour of activity, or 12 per hour of meditation or sleep.
##race.append('Intelligence (+ 6%) Radio: Basic (+ 10%) Pilot Hovercraft (+ 10%) Read Sensory Equipment (+ 10%) Weapon Systems (+10%) Climbing (+10%) Running Land Navigation (+10%) Wilderness Survival (+10%) W.P. Energy Pistol W.P. Energy Rifle W.P. one of choice Hand to Hand: Martial Arts')
    race.append("More info on Dog Boy O.C.C. can be cound in the Rifts Main Book  pg 107")
    race.append("Or Ultimate Edition pg 144")
                    
    return SDC,skills,race,#PSkillNumb,SkillNumb,equipment#+3Horror
def ExportStats():
    #global RND, PS, PE, Speed, SDC, skills, OCC, race, PSkillNumb, SkillNumb, equipment
    stats.PS = PS
    stats.PE = PE
    stats.Speed = Speed
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
