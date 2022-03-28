import RPi.GPIO as GPIO
import time

s2 = 8
s3 = 7
signal_1 = 12
NUM_CYCLES = 10

s4 = 17
s5 = 27
signal_2 = 22

def setup_1():  ## def setup
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")

def setup_2():  ## def setup
  GPIO.setup(signal_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s4,GPIO.OUT)
  GPIO.setup(s5,GPIO.OUT)
  print("\n")

def loop_1():
  temp = 1
  while(1):

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.LOW)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_1, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    white_1  = NUM_CYCLES / duration   #in Hz
    print("white value_1 - ",white_1)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_1, GPIO.FALLING)
    duration = time.time() - start
    blue_1 = NUM_CYCLES / duration
    print("blue value_1 - ",blue_1)

    time.sleep(0.5)

def loop_2():
  temp = 1
  while(1):

    GPIO.output(s4,GPIO.HIGH)
    GPIO.output(s5,GPIO.LOW)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_2, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    white_2  = NUM_CYCLES / duration   #in Hz
    print("white value_2 - ",white_2)

    GPIO.output(s4,GPIO.LOW)
    GPIO.output(s5,GPIO.HIGH)

    time.sleep(0.3)

    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal_2, GPIO.FALLING)
    duration = time.time() - start
    blue_2 = NUM_CYCLES / duration
    print("blue value_2 - ",blue_2)

    time.sleep(0.5)


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':

    #setup_1()
    setup_2()

    try:
        #loop_1()
        #time.sleep(0.2)
        loop_2()
        time.sleep(0.2)

    except KeyboardInterrupt:
        endprogram()
