from Joystick import joystick

def loop():
    while True:
        pass

if __name__ == '__main__':  # Program start from here
    #P1=joystick([7,11,12,13,15,16,18,22],["w","s","a","d","z","x","c","v"],"P1")
    #P2 = joystick([29,31,32,33,35,36,37,38], ["up","down","left","right","b","n","m","k"],"P2")
    #for test
    tst=joystick([11],"w","test")
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        #for test
        tst.destroy()
        #P1.destroy()
        #P2.destroy()