#!/user/bin/env python
# -*- coding: cp1252 -*-
# Sceen Generator
# Created by Keith Marrs-Olson

import stats
x = 1
print ("people = [")
while x <101:
    #print ('%d: "%s"' % (x, people[x]))
    print ( '"%s",' % stats.people[x])
    x=x+1
    
