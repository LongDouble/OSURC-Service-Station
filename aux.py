import RPi.GPIO as GPIO
import time

def SETUP_PINS():
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high for S1 (Button 0)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S2 (Button 1)
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S3 (Button 2)
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S4 (Button 3)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S5 (Button 4)
	GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S6 (Button 5)
	GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S7 (Button 6)
	GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S8 (Switch 0)
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S9 (Switch 1)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S10 (Switch 2)
	GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S11 (Switch 3)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S12 (Switch 4)
	GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S13 (Switch 5)
	GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S14 (Switch 6)

def SET_DEFAULT_HIGH(Buttons, Switches):
	Buttons[0] = GPIO.input(18)
	Buttons[1] = GPIO.input(19)
	Buttons[2] = GPIO.input(4)
	Buttons[3] = GPIO.input(5)
	Buttons[4] = GPIO.input(6)
	Buttons[5] = GPIO.input(7)
	Buttons[6] = GPIO.input(8)
	Switches[0] = GPIO.input(9)
	Switches[1] = GPIO.input(10)
	Switches[2] = GPIO.input(11)
	Switches[3] = GPIO.input(12)
	Switches[4] = GPIO.input(13)
	Switches[5] = GPIO.input(14)
	Switches[6] = GPIO.input(15)

