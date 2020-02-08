from aux import SET_DEFAULT_HIGH, SETUP_PINS
import RPi.GPIO as GPIO
import time
import serial

print("Setting PIN mode...")
GPIO.setmode(GPIO.BCM)

print("Setting PINS to HIGH...")
SETUP_PINS()

print("Connecting to Arduino...")
ser = serial.Serial('/dev/ttyUSB0', 9600)

Buttons = [0, 0, 0, 0, 0, 0, 0]
Switches = [0, 0, 0, 0, 0, 0, 0]

print("Listening")

while True:
	SET_DEFAULT_HIGH(Buttons, Switches)
	
	for i in Buttons:
		if i == False:
			print("Button " + str(i))
			time.sleep(0.1)
	
	for i in Switches:
		if i == False:
			print("Switch " + str(i))
			time.sleep(0.1)
	
