#!/usr/bin/python
# coding: utf-8

import curses, curses.panel, time, random

LOGO = '''
88888888ba  88 88            
88      "8b "" 88            
88      ,8P    88            
88aaaaaa8P' 88 88 ,adPPYba,  
88""""""'   88 88 I8[    ""  
88          88 88  `"Y8ba,   
88          88 88 aa    ]8I  
88          88 88 `"YbbdP"'  
                             
                             
                                    
                                88  
                                88  
                                88  
,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
""     `Y8 88P'   `"8a a8"    `Y88  
,adPPPPP88 88       88 8b       88  
88,    ,88 88       88 "8a,   ,d88  
`"8bbdP"Y8 88       88  `"8bbdP"Y8  
                                    
                                    
                                                                                                                                       
88888888ba                                                                                                 88                          
88      "8b                                                                                                ""                          
88      ,8P                                                                                                                            
88aaaaaa8P' 8b,dPPYba,  ,adPPYba,   ,adPPYb,d8 8b,dPPYba, ,adPPYYba, 88,dPYba,,adPYba,  88,dPYba,,adPYba,  88 8b,dPPYba,   ,adPPYb,d8  
88""""""'   88P'   "Y8 a8"     "8a a8"    `Y88 88P'   "Y8 ""     `Y8 88P'   "88"    "8a 88P'   "88"    "8a 88 88P'   `"8a a8"    `Y88  
88          88         8b       d8 8b       88 88         ,adPPPPP88 88      88      88 88      88      88 88 88       88 8b       88  
88          88         "8a,   ,a8" "8a,   ,d88 88         88,    ,88 88      88      88 88      88      88 88 88       88 "8a,   ,d88  
88          88          `"YbbdP"'   `"YbbdP"Y8 88         `"8bbdP"Y8 88      88      88 88      88      88 88 88       88  `"YbbdP"Y8  
                                    aa,    ,88                                                                             aa,    ,88  
                                     "Y8bbdP"                                                                               "Y8bbdP" '''

PADDING = 1

def make_panel(h,l, y,x, str): 
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

	win = curses.newwin(h,l, y,x) 
	win.erase() 
	panel = curses.panel.new_panel(win) 
	return win, panel 

def seatmap(win):

	(MY, MX) = win.getmaxyx() #putting screen size in a corner
	win.border(0)
	win.addstr(0,0, str(win.getmaxyx()))
	win.addstr(MY-1, MX/2-4, "Colormode: %s" % curses.has_colors() ) #Tells if we can use colors or not :)

	win.refresh()

	logoheight, logolen = len(LOGO.split('\n'))+2 , max( [len(x)+1 for x in LOGO.split('\n')] ) #Width of the logo
	
	(logowin, logopan) = make_panel(logoheight, logolen, MY/2-20/2, MX/2-logolen/2, LOGO)
	
	curses.panel.update_panels()
	logopan.top()
	logowin.refresh()	

	if curses.can_change_color():
		curses.init_color(COLOR_RED, 0, 300, 200)

	


	while 1:
		time.sleep(1) 
		(PY,PX) = logowin.getmaxyx()
		(MY, MX) = win.getmaxyx()

		win.addstr(0, MX/2, str(logowin.getmaxyx()) )
		
		Y,X = random.randrange(PADDING, MY-PY-PADDING), random.randrange(PADDING, MX+1-PX-PADDING) 
 		logopan.move(Y,X)
 		curses.init_pair(1,random.randrange(0, 8), 0 )
 		logowin.addstr(2, 2, LOGO, curses.color_pair(1))

		curses.panel.update_panels()
		logowin.refresh()
		win.refresh()

curses.wrapper(seatmap)
