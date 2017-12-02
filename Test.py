#!/usr/bin/env python
import RPi.GPIO as GPIO


testPin=11

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

    GPIO.setup(testPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
        

def keyPress(ev=None):
    if GPIO.input(ev)==GPIO.LOW:
        print('Down: Push!')

    else:
        print('Up: Push!')

        
	
def loop():

    GPIO.add_event_detect(testPin, GPIO.BOTH, callback=keyPress,bouncetime=50) # wait for falling
#        GPIO.add_event_detect(pin, GPIO.RISING, callback=keyUp,bouncetime=250) # wait for falling
    while True:
        pass   # Don't do anything

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()