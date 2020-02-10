from pynput import keyboard
import time

def on_press(key):
    print('Key {} pressed.'.format(key))

def on_release(key):
    if str(key) == 'Key.esc':
        print('Exiting...')
        return False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    time.sleep(0.1)