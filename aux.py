import RPi.GPIO as GPIO
import time
import serial
import keyboard

typed = ""

def SETUP_PINS():
	GPIO.setmode(GPIO.BCM) #This makes Python use the pinout numbers for PIN identification
	GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high for S1 (Button 0)
	GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S2 (Button 1)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S3 (Button 2)
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S4 (Button 3)
	GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S5 (Button 4)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S6 (Button 5)
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S7 (Button 6)

	GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S8 (Switch 0)
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S9 (Switch 1)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S10 (Switch 2)
	GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S11 (Switch 3)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S12 (Switch 4)
	GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S13 (Switch 5)
	GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Default is high S14 (Switch 6)

def SET_TO_PIN_VALUE(Buttons, Switches):
	Buttons[0] = GPIO.input(8)
	Buttons[1] = GPIO.input(7)
	Buttons[2] = GPIO.input(6)
	Buttons[3] = GPIO.input(5)
	Buttons[4] = GPIO.input(24)
	Buttons[5] = GPIO.input(19)
	Buttons[6] = GPIO.input(18)

	Switches[0] = GPIO.input(25)
	Switches[1] = GPIO.input(10)
	Switches[2] = GPIO.input(26)
	Switches[3] = GPIO.input(12)
	Switches[4] = GPIO.input(13)
	Switches[5] = GPIO.input(14)
	Switches[6] = GPIO.input(15)

def key_press(key):
    global typed
    typed = typed + key.name
    encoded = "3," + typed + "\n"
    encoded = encoded.encode()
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.write(encoded)


