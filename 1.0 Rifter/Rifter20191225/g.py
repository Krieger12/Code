import stats
import easygui
g=stats.g
title = "g.py"
def main():
    if stats.g == "n":
        stats.g = "g"
        stats.RND=""
        choices = ['Create', 'Random', 'Test'] 
        G = easygui.ynbox (" Do you want to enter God mode? ", title)
        
        if G == 1:
            g = easygui.integerbox('Please input level',title, default=1)
            stats.Level = g
            stats.g="G"
        if G == 0:
            stats.RND="T"
            stats.g="n"
    if stats.g == "G":
        choices = ['Create', 'Random', 'Test'] 
        RNDYN = easygui.buttonbox (" Do you want to create character, randomize character creation, or run test code ", title, choices)
        if RNDYN == 'Create':
            if stats.title=="OCCselect.py":
                stats.RND="G"
            else: stats.RND="N"
        elif RNDYN == 'Random':
            stats.RND="Y"
        elif RNDYN == 'Test':
            stats.RND="T"

    else: exit
main()


