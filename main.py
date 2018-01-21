from Joystick import joystick
from Joystick import joystickMCP

def loop():
    while True:
        pass

if __name__ == '__main__':  # Program start from here
    P1=joystick([12,13,16,15,18,22,7,11],["w","s","a","d","z","x","c","v"],"P1")
    P2 = joystick([29,31,35,33,37,32,36,40], ["up","down","left","right","b","n","m","k"],"P2")
    settingBtn=joystickMCP([1,2,3],["i","o","p"],"set")
    #for test
    #tst=joystick([11],"w","test")
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        #for test
        #tst.destroy()
        P1.destroy()
        P2.destroy()
        settingBtn.destroy()
