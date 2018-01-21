from evdev import uinput, UInput, ecodes as e
import os
import time

os.system("sudo modprobe uinput")
ui = UInput({e.EV_KEY:[e.KEY_Z,e.KEY_X]},name="retrogame",bustype=e.BUS_USB)
print("test1")
i=0
while i<10:
    ui.write(e.EV_KEY,e.KEY_Z,1)
    i=i+1
    time.sleep(1)
print("test2")
ui.write(e.EV_KEY,e.KEY_Z,0)
