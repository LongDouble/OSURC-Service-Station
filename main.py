from aux import SET_DEFAULT_HIGH, SETUP_PINS
import RPi.GPIO as GPIO
import time

print("Setting PIN mode")
GPIO.setmode(GPIO.BCM) #Using GPIO numbering

print("Setting PINS to HIGH")

#Setting PINS to be HIGH by default
SETUP_PINS()


print("Listening")
Buttons = [0, 0, 0, 0, 0, 0, 0]
Switches = [0, 0, 0, 0, 0, 0, 0]

while True:
	SET_DEFAULT_HIGH(Buttons, Switches)
	
	if Buttons[0] == False:
		print('Button 0')
		time.sleep(0.1)
	
	elif Buttons[1]  == False:
		print ('Button 1')
		time.sleep(0.1)
		
	elif Buttons[2]  == False:
		print ('Button 2')
		time.sleep(0.1)
		
	elif Buttons[3]  == False:
		print ('Button 3')
		time.sleep(0.1)
		
	elif Buttons[4]  == False:
		print ('Button 4')
		time.sleep(0.1)
		
	elif Buttons[5]  == False:
		print ('Button 5')
		time.sleep(0.1)
		
	elif Buttons[6]  == False:
		print ('Button 6')
		time.sleep(0.1)
	
