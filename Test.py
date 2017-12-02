#!/usr/bin/env python
import RPi.GPIO as GPIO



class Test:
    def __init__(self,pin=11):
        self._testPin=pin
        self.setup()
        self.addEvent()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

        GPIO.setup(self._testPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)


    def keyPress(self,ev=None):
        if GPIO.input(ev)==GPIO.LOW:
            print('Down: Push!')

        else:
            print('Up: Push!')



    def addEvent(self):

        GPIO.add_event_detect(self._testPin, GPIO.BOTH, callback=self.keyPress,bouncetime=50) # wait for falling
    #        GPIO.add_event_detect(pin, GPIO.RISING, callback=keyUp,bouncetime=250) # wait for falling
    #    while True:
    #        pass   # Don't do anything

    def destroy(self):
    	GPIO.cleanup()                     # Release resource

