import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

s2 = 8
s3 = 7
signal_1 = 12
NUM_CYCLES = 10

s4 = 17
s5 = 27
signal_2 = 22

GPIO.setup(signal_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)

GPIO.setup(signal_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s4,GPIO.OUT)
GPIO.setup(s5,GPIO.OUT)

def CS_1_white():

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.LOW)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_1, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    white_1  = NUM_CYCLES / duration   #in Hz
    return white_1

def CS_1_blue():

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_1, GPIO.FALLING)
    duration = time.time() - start
    blue_1 = NUM_CYCLES / duration
    return blue_1

def CS_2_white():

    GPIO.output(s4,GPIO.HIGH)
    GPIO.output(s5,GPIO.LOW)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_2, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    white_2  = NUM_CYCLES / duration   #in Hz
    return white_2

def CS_2_blue():

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


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':

    try:
        white_1 = CS_1_white()
        time.sleep(0.2)
        blue_1 = CS_1_blue()
        time.sleep(0.2)
        white_2 = CS_2_white()
        time.sleep(0.2)
        blue_2 = CS_2_blue()
        time.sleep(0.2)
        print("Measured white_1 = %.1f hz" % white_1)
        print("Measured blue_1 = %.1f hz" % blue_1)
        print("Measured white_2 = %.1f hz" % white_2)
        print("Measured blue_2 = %.1f hz" % blue_2)
        time.sleep(0.5)


    except KeyboardInterrupt:
        endprogram()
