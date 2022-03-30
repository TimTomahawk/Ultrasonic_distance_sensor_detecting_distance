import RPi.GPIO as GPIO
import time
from ultrasonic_distance import distancex,distancey
from Rawcolor_sensing_v2 import CS_1_white,CS_1_blue,CS_2_white,CS_2_blue

ENA1 = 2
ENB1 = 11
in1 = 3
in2 = 4
in3 = 10
in4 = 9
ENA2 = 20
ENB2 = 26
in5 = 5
in6 = 6
in7 = 13
in8 = 19
temp1=1

xPosition = 10
yPosition = 20
tDistance = 3

white_white = 1500   ## white frequency while detecting white
white_blue = 1000    ## blue freqneucy value while detecting white
blue_white = 500    ## white frequency value while detecting blue
blue_blue = 450     ##blue frequency value while detecting blue

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ENA1,GPIO.OUT)
GPIO.setup(ENB1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(ENA2,GPIO.OUT)
GPIO.setup(ENB2,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)

p1=GPIO.PWM(ENA1,1000)
p2=GPIO.PWM(ENB1,1000)
p3=GPIO.PWM(ENA2,1000)
p4=GPIO.PWM(ENB2,1000)

p1.start(25)
p2.start(25)
p3.start(25)
p4.start(25)

while 1:
    curr_x = distancex()
    time.sleep(0.2)
    curr_y = distancey()
    time.sleep(0.2)
    color_white_1 = CS_1_white()
    time.sleep(0.2)
    color_blue_1 = CS_1_blue()
    time.sleep(0.2)
    color_white_2 = CS_2_white()
    time.sleep(0.2)
    color_blue_2 = CS_2_blue()
    time.sleep(0.2)

    diffx = curr_x - xPosition
    diffy = curr_y - yPosition

    if (color_white_1 >= white_white and color_white_2 >= white_white and color_blue_1 <= white_blue and color_blue_2 <= white_blue and abs(diffx) >= tDistance and abs(diffy) >= tDistance):  ## going straight
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.HIGH)
        GPIO.output(in8,GPIO.LOW)
        p1.start(40)
        p2.start(40)
        p3.start(40)
        p4.start(40)
    elif(color_white_1 >= blue_white and color_blue_1 <= blue_blue and color_white_2 >= white_white and color_blue_2 <= white_blue):          ## turning to the left
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        p1.start(30)
        p2.start(0)
        p3.start(30)
        p4.start(0)
    elif(color_white_1 >= white_white and color_blue_1 <= white_blue and color_white_2 >= blue_white and color_blue_2 <= blue_blue):    ## turnign to the right
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        p1.start(30)
        p2.start(0)
        p3.start(30)
        p4.start(0)
    elif(color_white_1 >= blue_white and color_blue_1 <= blue_blue and color_white_2 >= blue_white and color_blue_2 <= blue_blue):      ##intersection issue
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.HIGH)
        GPIO.output(in8,GPIO.LOW)
        p1.start(40)
        p2.start(40)
        p3.start(40)
        p4.start(40)
    elif():     ## while turning needs to ask for help

    elif(color_white_1 >= white_white and color_white_2 >= white_white and color_blue_1 <= white_blue and color_blue_2 <= white_blue and abs(diffx) <= tDistance and abs(diffy) <= tDistance):  ## when to stop
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        p1.start(0)
        p2.start(0)
        p3.start(0)
        p4.start(0)
        break
    else:
        GPIO.cleanup()
        time.sleep(5)
