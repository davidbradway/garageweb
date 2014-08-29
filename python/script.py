import webiopi

GPIO = webiopi.GPIO

DOOR_IS_OPEN = False

Garage = 0 # GPIO pin using BCM numbering

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(Garage, GPIO.OUT)

# loop function is repeatedly called by WebIOPi
def loop():
    # gives CPU some time before looping again
    webiopi.sleep(1)

#@webiopi.macro
#def toggleDoorState():
#    global DOOR_IS_OPEN
#    DOOR_IS_OPEN = not DOOR_IS_OPEN
#    return DOOR_IS_OPEN
