#!/usr/bin/env python
import RPi.GPIO as GPIO
from Adafruit_GPIO.MCP230xx import MCP23017
#import pyautogui

#pins={}
class joystick:
    def __init__(self,ppins,keys,name):
        self._name=name
        self._pins={}
        for x in range(len(ppins)):
            self._pins[ppins[x]]=keys[x]
        self.setup()
        self.addEvents()


    def setup(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        for pin in self._pins.keys():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)


    def keyPress(self,ev=None):
        if GPIO.input(ev)==GPIO.LOW:
            print('%s: Down: %s - %s' % (self._name,ev,self._pins[ev]))
            #TODO pyautogui.keyDown(self._pins[ev])
        else:
            print('%s: Up: %s - %s' % (self._name,ev,self._pins[ev]))
            #TODO pyautogui.keyUp(self._pins[ev])


    def addEvents(self):
        for pin in self._pins.keys():
            GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.keyPress,bouncetime=50) # wait for falling
    #        GPIO.add_event_detect(pin, GPIO.RISING, callback=keyUp,bouncetime=250) # wait for falling


    def destroy(self):
    	GPIO.cleanup()                     # Release resource

class joystickMCP:
    def __init__(self, ppins, keys, name):
        self._name = name
        self._pins = {}
        self._mcp= MCP23017()
        self.active=True
        for x in range(len(ppins)):
            self._pins[ppins[x]] = keys[x]
            self._prevStatus[ppins[x]]=True
        self.setup()
        self.loop()


    def setup(self):
        #GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
        #self._mcp = MCP23017()
        #self._mcp.setup(8,1)
        #self._mcp.pullup(8,True)

        for pin in self._pins.keys():
            self._mcp.setup(pin, GPIO.IN)#tutti i pin in input
            self._mcp.pullup(pin,True)#lì setto a 3.3v

    def checkKeyPress(self, ev=None):
        if self._mcp.input(ev) != self._prevStatus[ev]:
            if self._mcp.input(ev) == GPIO.LOW:
                print('Down: Push!')
            else:
                print('Up: Push!')
            self._prevStatus[ev] = self._mcp.input(ev)


    def loop(self):
        while self.active:
            for pin in self._pins.keys():
                self.checkKeyPress(pin)


    def destroy(self):
        self.active=False


