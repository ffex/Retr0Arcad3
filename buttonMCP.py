#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
from Adafruit_GPIO.MCP230xx import MCP23017
from evdev import uinput, UInput, ecodes as e

class joystickMCP:
    def __init__(self, ppins, keys, name):
        self._name = name
        self._pins = {}
        self._prevStatus = {}
        self.ui=""
        self._mcp= MCP23017()
        self.active=True
        for x in range(len(ppins)):
            self._pins[ppins[x]] = keys[x]
            self._prevStatus[ppins[x]]=True
        os.system("sudo modprobe uinput")
        self.ui = UInput(name="fex",vendor=9999,product=8888)
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
              #  print('Down: Push!')
                self.ui.write(e.EV_KEY, self._pins[ev], 1)
            else:
               # print('Up: Push!')
                self.ui.write(e.EV_KEY, self._pins[ev], 0)
            self._prevStatus[ev] = self._mcp.input(ev)
        self.ui.syn()


    def loop(self):
        while self.active:
            for pin in self._pins.keys():
                self.checkKeyPress(pin)


    def destroy(self):
        self.active=False
