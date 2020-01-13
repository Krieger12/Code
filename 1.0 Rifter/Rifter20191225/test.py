PS = 30
PP = 55

if PS > 16:
    x = PS-15
    print ("damage +%s" %x)
if PP > 16:
    x=PP-16
    y,z=0,0
    while z <= x:
        z=z+2
        y=y+1
        print(x, y, z)
        print ("parry +%s" %y)


x=0
z = ["SDC",
    "PS",
    "PP",
    "PE",
    "Speed",
    "parry",
    "dodge",
    "damage",
     "parry",
     "dodge","strike",
     "roll"]
while x > 0:
    print('print("%s = "stats.%s)' % (z[x], z[x]))
    x=x-1
if x == 10:
    '''
    print ("Number of Attacks %s ") % stats.attack 
    print ("Damage + %s ") % stats.damage
    print ("Strike + %s ") % stats.strike
    print ("Dodge + %s ") % stats.dodge
    print ("Roll with punch or fall + %s ") % stats.roll
    print ("Parry attack + %s ") % stats.parry
    print ("Initiative + %s ") % stats.inish
    print ("Horror + %s ") % stats.horror
'''

    ps = PS 

