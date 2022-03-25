import Rpi.GPIO as GPIO  ## Import libraries
import time

GPIO.setmode(GPIO.BCM)  ## GPIO MODE (BOARD/BCM)

GPIO_TRIGGERx = **     ## SET GPIO PINS
GPIO_ECHOx = **
GPIO_TRIGGERy = **
GPIO_ECHOy = **

GPIO.setup(GPIO_TRIGGERx, GPIO.OUT)   ## set GPIO direction (IN/out)
GPIO.setup(GPIO_ECHOx.IN)

def distancex ():
    GPIO.output(GPIO_TRIGGERx, True)  ## Set trigger to high
    time.sleep(0.00001)  ## set trigger after 0.01ms to LOW
    GPIO.output(GPIO_TRIGGERx, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHOx) == 0:   ## save StartTime
        StartTime = time.time()

    while GPIO.input(GPIO_ECHOx) == 1:  ##save time of arrival
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distancex = (TimeElapsed * 34300)/2   ##to measure the distance

    return distancex

GPIO.setup(GPIO_TRIGGERy, GPIO.OUT)
GPIO.setup(GPIO_ECHOy.IN)

def distancey():
    GPIO.output(GPIO_TRIGGERy,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERy,False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHOy) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHOy) == 0:
        StopTime = time.time()

    TimeElapsed = StopTime = StartTime
    distancey = (TimeElapsed * 34300)/2

    return distancey



if _name_ == '_main_':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

    except KeyboardInterrupt:    ##Reset by pressing CTRL+C
        print("Measurement stopped by User")
        GPIO.cleanup()
