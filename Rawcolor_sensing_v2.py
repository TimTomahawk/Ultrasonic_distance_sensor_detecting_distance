import RPi.GPIO as GPIO   ## import raspberry pi GPIO control library
import time        ## import time library

GPIO.setmode(GPIO.BCM)  ## set up setmode

s2 = 8                  ## line 6-13 are the pins
s3 = 7
signal_1 = 12
NUM_CYCLES = 10         ## num cycle in for loop

s4 = 17
s5 = 27
signal_2 = 22

GPIO.setup(signal_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)         ##setup pin function
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)

GPIO.setup(signal_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s4,GPIO.OUT)
GPIO.setup(s5,GPIO.OUT)

def CS_1_white():                ## function for first color sensor to detect clear(white) color

    GPIO.output(s2,GPIO.HIGH)         # s2 setup as high and s3 setup as low detects the frequency for white color
    GPIO.output(s3,GPIO.LOW)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_1, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    white_1  = NUM_CYCLES / duration   #in Hz
    return white_1

def CS_1_blue():  ## function for first color sensor to detect blue color

    GPIO.output(s2,GPIO.LOW)      ## s2 setup as low, s3 setup as high detects the frequency for blue color
    GPIO.output(s3,GPIO.HIGH)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_1, GPIO.FALLING)
    duration = time.time() - start
    blue_1 = NUM_CYCLES / duration
    return blue_1

def CS_2_white():   ## function for second color sensor to detect white color

    GPIO.output(s4,GPIO.HIGH)
    GPIO.output(s5,GPIO.LOW)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_2, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    white_2  = NUM_CYCLES / duration   #in Hz
    return white_2

def CS_2_blue():  ## function for second color sensor to detect blue color

    GPIO.output(s4,GPIO.LOW)
    GPIO.output(s5,GPIO.HIGH)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_2, GPIO.FALLING)
    duration = time.time() - start
    blue_2 = NUM_CYCLES / duration
    return blue_2

    time.sleep(0.5)


def endprogram():    ## function for press crtl+c to stop 
    GPIO.cleanup()

if __name__=='__main__':

    try:
        while True:
            white_1 = CS_1_white()
            #time.sleep(0.2)
            blue_1 = CS_1_blue()
            #time.sleep(0.2)
            white_2 = CS_2_white()
            #time.sleep(0.2)
            blue_2 = CS_2_blue()
            #time.sleep(0.2)
            print("Measured white_1 = %.1f hz" % white_1)
            print("Measured blue_1 = %.1f hz" % blue_1)
            print("Measured white_2 = %.1f hz" % white_2)
            print("Measured blue_2 = %.1f hz" % blue_2)
            time.sleep(0.2)
    except KeyboardInterrupt:
        endprogram()
