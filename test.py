import curses
import time

curses.initscr()
curses.noecho()
window = curses.newwin(30, 50, 0, 0)
window.keypad(1) #Escape sequences are interpresed
curses.curs_set(0) #Make cursor invisible
window.border(0)
window.timeout(1000)
window.nodelay(True)

while True:
    window.refresh()
    press =  window.getch()

    if press == ord('q'): #q quits the program
        curses.endwin()
        exit()
    elif str(press) != '-1':
       window.addch(press)
    
    time.sleep(0.1)