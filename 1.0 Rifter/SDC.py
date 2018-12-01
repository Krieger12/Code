#!/user/bin/env python
# -*- coding: cp1252 -*-
#rifts char gen
# Created by Keith Marrs-Olson
# Calculates SDC

import easygui,random
import stats

def main():
    stats.SDC = 1
    if stats.SDC == 1:
        MSA()
    elif stats.SDC == 2:
        Psy()
    elif stats.SDC == 3:
        Men()
    return
def MSA():
    if stats.RND == "Y":
        stats.SDC = random.randrange(4,25)
    if stats.RND == "N":
        stats.SDC = easygui.integerbox("Please roll 4d6 for Structural damage Capacity")
    if stats.RND == "T":
        stats.SDC = 15
    return    
def Psy():
    if stats.RND == "Y":
        stats.SDC = random.randrange(3,19)
    if stats.RND == "N":
        stats.SDC = easygui.integerbox("Please roll 3d6 for Structural damage Capacity")
    if stats.RND == "T":
        stats.SDC = 15
    return
def Men():
    if stats.RND == "Y":
        stats.SDC = random.randrange(1,4)*10
    if stats.RND == "N":
        SDC = easygui.integerbox("Please roll 1d4 for Structural damage Capacity")
        stats.SDC=SDC*10
    if stats.RND == "T":
        stats.SDC = 15
    return

main()
    
