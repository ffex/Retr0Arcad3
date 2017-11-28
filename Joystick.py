#!/usr/bin/env python
import RPi.GPIO as GPIO
import pyautogui

pins={}

def init(ppins=[11,12,13,15,16],key=['w','s','a','d','space']):
    for x in range(len(ppins)):
        pins[ppins[x]]=key[x]

    

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    for pin in pins.keys():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
        

def keyPress(ev=None):
    if GPIO.input(ev)==GPIO.LOW:
        print('Down: %s - %s' % (ev,pins[ev]))
        pyautogui.keyDown(pins[ev])        
    else:
        print('Up: %s - %s' % (ev,pins[ev]))
        pyautogui.keyUp(pins[ev])
        
	
def loop():
    for pin in pins.keys():
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=keyPress,bouncetime=50) # wait for falling
#        GPIO.add_event_detect(pin, GPIO.RISING, callback=keyUp,bouncetime=250) # wait for falling
    while True:
        pass   # Don't do anything

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    init()
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()