from Joystick import joystick

from evdev import uinput, UInput, ecodes as e

def loop():
    while True:
        pass

if __name__ == '__main__':  # Program start from here
    #P1=joystick([12,13,16,15,18,22,7,11],[e.KEY_W,e.KEY_S,e.KEY_A,e.KEY_D,e.KEY_Z,e.KEY_X,e.KEY_C,e.KEY_V],"P1")
    P2 = joystick([29,31,35,33,37,32,36,40], [e.KEY_UP,e.KEY_DOWN,e.KEY_LEFT,e.KEY_RIGHT,e.KEY_B,e.KEY_N,e.KEY_M,e.KEY_K],"P2")
   # settingBtn=joystickMCP([1,2,3],[e.KEY_I,e.KEY_O,e.KEY_P],"set")
    #for test
    #tst=joystick([11],"w","test")
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        #for test
        #tst.destroy()
        P1.destroy()
        #P2.destroy()
    #    settingBtn.destroy()
