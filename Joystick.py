#!/usr/bin/env python
import RPi.GPIO as GPIO
import pyautogui

pins={}
class joystick:
    def __init__(self,ppins,keys,name):
        self._name=name
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
            pyautogui.keyDown(self._pins[ev])
        else:
            print('%s: Up: %s - %s' % (self._name,ev,self._pins[ev]))
            pyautogui.keyUp(self._pins[ev])


    def addEvents(self):
        for pin in self._pins.keys():
            GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.keyPress,bouncetime=50) # wait for falling
    #        GPIO.add_event_detect(pin, GPIO.RISING, callback=keyUp,bouncetime=250) # wait for falling


    def destroy(self):
    	GPIO.cleanup()                     # Release resource

    if __name__ == '__main__':     # Program start from here
        init()
        setup()
        try:
            loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            destroy()