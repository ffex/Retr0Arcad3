#!/usr/bin/env python
import RPi.GPIO as GPIO
from Adafruit_GPIO.MCP230xx import MCP23017


class Test:
    
    def __init__(self,pin):
        self._testPin=pin
        self.setup()
        self.addEvent()
        self._prevStatus=GPIO.HIGH
        try:
            self.loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            pass
    def loop(self):
        #print('hola')
        while True:
            if self._mcp.input(8)!=self._prevStatus:
                if self._mcp.input(8)==GPIO.LOW:
                    print('Down: Push!')
                else:
                    print('Up: Push!')
                self._prevStatus=self._mcp.input(8)
            
    def setup(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        self._mcp = MCP23017()
        self._mcp.setup(8,1)
        self._mcp.pullup(8,True)
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

