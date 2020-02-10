from aux import SET_TO_PIN_VALUE, SETUP_PINS, on_press, on_release
import RPi.GPIO as GPIO
import time
from pynput import keyboard
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


print("Setting up pins...\n")
SETUP_PINS()

print("Connecting to Arduino...\n")
ser = serial.Serial('/dev/ttyACM0', 9600)

print("Setting up keyboard listener...")
listener = keyboard.Listener(on_press=on_press,
       on_release=on_release)
listener.start()

time.sleep(1)
print("Listening for events...\n")

while True:
    #Sets all the values to the value of the PIN (HIGH or LOW)
        SET_TO_PIN_VALUE(Buttons, Switches) 

        #Checking button states
        count = 0
        for i in Buttons:
            if i == False and Button_Was_Pressed[count] == False: #If PIN is LOW and wasn't already triggered
                print("Button " + str(count) + "\n")
                message = "0," + str(count) + ",*\n"
                message = message.encode()
                ser.write(message)
                Button_Was_Pressed[count] = True
            count += 1

        #Checking switch states
        count = 0
        for i in Switches:
            if i == False and Switch_Was_Triggered[count] == False:
                print("Switch " + str(count) + "\n")
                message = "1," + str(count) + ",*\n"
                message = message.encode()
                ser.write(message)
                Switch_Was_Triggered[count] = True
            count += 1

