import RPi.GPIO as GPIO  ## Import libraries
import time

GPIO.setmode(GPIO.BCM)  ## GPIO MODE (BOARD/BCM)

GPIO_TRIGGERx = 23     ## SET GPIO PINS
GPIO_ECHOx = 24
GPIO_TRIGGERy = 25
GPIO_ECHOy = 16

GPIO.setup(GPIO_TRIGGERx, GPIO.OUT)   ## set GPIO direction (IN/out)
GPIO.setup(GPIO_ECHOx, GPIO.IN)
GPIO.setup(GPIO_TRIGGERy, GPIO.OUT)
GPIO.setup(GPIO_ECHOy, GPIO.IN)

def distancex():
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
    dist_x = (TimeElapsed * 34300)/2   ##to measure the distance

    return dist_x

def distancey():
    GPIO.output(GPIO_TRIGGERy,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERy,False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHOy) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHOy) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    dist_y = (TimeElapsed * 34300)/2

    return dist_y



if __name__ == '__main__':
    try:
        while True:
            dist_x = distancex()
            time.sleep(0.5)
            dist_y = distancey()
            print ("Measured Distance_x = %.1f cm" % dist_x)
            print ("Measured Distance_y = %.1f cm" % dist_y)
            time.sleep(0.5)

    except KeyboardInterrupt:    ##Reset by pressing CTRL+C
        print("Measurement stopped by User")
        GPIO.cleanup()
