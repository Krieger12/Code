#!/user/bin/env python
# -*- coding: cp1252 -*-
# The Handy Dandy Random Adventure Generator
# Created by Keith Marrs-Olson
# Credit to where credit is due
#   From The Rifter #63 pg 59
#   The Handy Dandy Random Adventure Generator
#   For Beyond the Supernatural™
#   By Chai Gallahun

Title="The Handy Dandy Random Adventure Generator"
import easygui, random, stats
def Main():
    choices = ("People (Main & Supporting Characters)","Places (Primary and Supporting Locations)","Scary Things - Conditions (Stage Dressing)","Scary Things Threats(Things That Went Bump in the Night)","Cloudy with a Chance for Horror (Weather)")
    choice = easygui.choicebox("Please Choose the Stage Settings:",Title,choices)
    if choice == "People (Main & Supporting Characters)":
        X = random.randrange(1,101)
        easygui.msgbox(" People (Main & Supporting Characters): \n %s" % stats.people[X])
    elif choice == "Places (Primary and Supporting Locations)":
        X = random.randrange(1,101)
        easygui.msgbox(" People (Main & Supporting Characters): \n %s" % stats.people[X])
    elif choice == "Scary Things - Conditions (Stage Dressing)":
        X = random.randrange(1,101)
        if X < 100:
            Y = random.randrange(1,9)
            easygui.msgbox(" Scary Things - Conditions (Stage Dressing): \n %s %s" % (stats.Stage[X], stats.EOD[Y]))
        else:
            easygui.msgbox(" Scary Things - Conditions (Stage Dressing): \n %s" % stats.Stage[X])
    elif choice == "Scary Things Threats(Things That Went Bump in the Night)":
        X = random.randrange(1,101)
        if X < 100:
            easygui.msgbox(" Scary Things Threats(Things That Went Bump in the Night): \n %s" % stats.SThing[X])
        else:
            y = random.randrange(2,9)
            z = 1
            while z<y:
                easygui.msgbox(" Scary Things Threats(Things That Went Bump in the Night): \n %s" % stats.SThing[X])
                z =z+1
    elif choice == "Cloudy with a Chance for Horror (Weather)":
        X = random.randrange(1,101)
        if X < 99:
            easygui.msgbox(" Cloudy with a Chance for Horror (Weather): \n %s" % stats.Weather[X])
        if X >= 99:
            if x == 99:
                y = random.randrange(2,6)
            else:
                y = random.randrange(3,10)
            while y>0:
                easygui.msgbox(" Cloudy with a Chance for Horror (Weather): \n %s" % stats.Weather[X])
                y=y-1
Main()
