from Test import Test


def loop():
    while True:
        pass



if __name__ == '__main__':  # Program start from here
    test=Test(15)

    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        test.destroy()
