import RPi.GPIO as GPIO
import time

print("Setting PIN mode")
GPIO.setmode(GPIO.BCM) #Using GPIO numbering

print("Setting PINS to HIGH")
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

#Since the default is high, when the switch is pressed the GPIO pin is brought to ground
print("Listening")

while True:
	Button_0 = GPIO.input(18)
	Button_1 = GPIO.input(19)
	Button_2 = GPIO.input(4)
	Button_3 = GPIO.input(5)
	Button_4 = GPIO.input(6)
	Button_5 = GPIO.input(7)
	Button_6 = GPIO.input(8)
	
	if Button_0 == False:
		print('Button 0')
		time.sleep(0.1)
	
	elif Button_1 == False:
		print ('Button 1')
		time.sleep(0.1)
		
	elif Button_2 == False:
		print ('Button 2')
		time.sleep(0.1)
		
	elif Button_3 == False:
		print ('Button 3')
		time.sleep(0.1)
		
	elif Button_4 == False:
		print ('Button 4')
		time.sleep(0.1)
		
	elif Button_5 == False:
		print ('Button 5')
		time.sleep(0.1)
		
	elif Button_6 == False:
		print ('Button 6')
		time.sleep(0.1)
	
