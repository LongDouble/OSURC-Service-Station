from aux import SET_TO_PIN_VALUE, SETUP_PINS
import RPi.GPIO as GPIO
import curses
import time
import serial

#Will hold the value of the PIN each button and switch is on
Buttons = [0, 0, 0, 0, 0, 0, 0]
Switches = [0, 0, 0, 0, 0, 0, 0] 

#Will remember if a button or switch was already pressed
Button_Was_Pressed = [False, False, False, False, False, False, False] 
Switch_Was_Triggered = [False, False, False, False, False, False, False] 

#Will hold the encoded message to sent to the Arduino
message = ""

#Will hold the type messages
typed = ""

#Will hold ASCII value of keypressed
keypress = -1

curses.initscr()
curses.noecho()
window = curses.newwin(30, 50, 0, 0)
window.keypad(1) #Escape sequences are interpresed
curses.curs_set(0) #Make cursor invisible
window.border(0)
window.timeout(1000)
window.nodelay(True)

window.addstr("Setting up pins...\n")
window.refresh()
SETUP_PINS()

window.addstr("Connecting to Arduino...\n")
window.refresh()
ser = serial.Serial('/dev/ttyACM0', 9600)

window.addstr("Listening...\n")
window.refresh()

while True:
	#Sets all the values to the value of the PIN (HIGH or LOW)
	SET_TO_PIN_VALUE(Buttons, Switches) 
	
	#Checking button states
	count = 0
	for i in Buttons:
		if i == False and Button_Was_Pressed[count] == False: #If PIN is LOW and wasn't already triggered
			window.addstr("Button " + str(count) + "\n")
			window.refresh()
			message = "0," + str(count) + ",*"
			message = message.encode()
			ser.write(message)
			Button_Was_Pressed[count] = True
		count += 1
	
	#Checking switch states
	count = 0
	for i in Switches:
		if i == False and Switch_Was_Triggered[count] == False:
			window.addstr("Switch " + str(count) + "\n")
			window.refresh()
			message = "1," + str(count) + ",*"
			message = message.encode()
			ser.write(message)
			Switch_Was_Triggered[count] = True
		count += 1
	
	keypress = window.getch()
	
	if keypress == ord('q'):
		curses.endwin()
		exit()
        elif keypress != -1:
            typed = typed + chr(keypress)
            typed_encoded = "3," + typed + "\n"
            typed_encoded = typed_encoded.encode()
            ser.write(typed_encoded)
            window.addstr(typed + "\n")
            window.refresh()
            time.sleep(0.1)

