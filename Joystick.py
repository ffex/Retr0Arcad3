#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
from Adafruit_GPIO.MCP230xx import MCP23017
from evdev import uinput, UInput, ecodes as e
#import pyautogui
# See /usr/include/linux/input.h for keycode names
#adafruit-retrogame

#pins={}
class joystick:
    def __init__(self,ppins,keys,name):
        self._name=name
        self.active=True
        self._pins={}
        self._prevStatus = {}
        self.ui = ""
        for x in range(len(ppins)):
            self._pins[ppins[x]]=keys[x]
            self._prevStatus[ppins[x]]=GPIO.HIGH
        self.setup()
        os.system("sudo modprobe uinput")
        self.ui = UInput(name=name,vendor=9999,product=8888)
        self.loop()



    def setup(self):
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        for pin in self._pins.keys():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)


    def keyPress(self,ev=None):
        #ui.write(e.EV_KEY, key, state)
        #print("hola")
        if GPIO.input(ev) != self._prevStatus[ev]:
            if GPIO.input(ev)==GPIO.LOW:
                #print('%s: Down: %s - %s' % (self._name,ev,self._pins[ev]))
                self.ui.write(e.EV_KEY,self._pins[ev],1)
            else:
                #print('%s: Up: %s - %s' % (self._name,ev,self._pins[ev]))
                self.ui.write(e.EV_KEY,self._pins[ev],0)
            self._prevStatus[ev] = GPIO.input(ev)

        self.ui.syn()

    def loop(self):
        while self.active:
            for pin in self._pins.keys():
                self.keyPress(pin)
    #        GPIO.add_event_detect(pin, GPIO.RISING, callback=keyUp,bouncetime=250) # wait for falling


    def destroy(self):
        self.active=False
        time.sleep(0.5)
        GPIO.cleanup()


