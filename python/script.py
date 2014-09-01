import webiopi

GPIO = webiopi.GPIO

GARAGE = 0 # GPIO pin using BCM numbering

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(GARAGE, GPIO.OUT)

# loop function is repeatedly called by WebIOPi
def loop():
    # gives CPU some time before looping again
    webiopi.sleep(1)
