#!/user/bin/env python
# -*- coding: cp1252 -*-
# Random No Game No Life movie
# Created by Keith Marrs-Olson
import webbrowser, random

x = random.randrange(1,19)

if x < 13:
	url = ("http://www.animefreak.tv/watch/no-game-no-life-episode-%d-online" % x)
else:
	x = x -12
	url = ("http://www.animefreak.tv/watch/no-game-no-life-specials-%d-online" %x)
	
	
webbrowser.open(url, new=1, autoraise=True)
