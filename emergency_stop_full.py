import RPi.GPIO as GPIO
import time

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

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ENA1,GPIO.OUT)
GPIO.setup(ENB1,GPIO.OUT)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(ENA2,GPIO.OUT)
GPIO.setup(ENB2,GPIO.OUT)

p1=GPIO.PWM(ENA1,1000)
p2=GPIO.PWM(ENB1,1000)
p3=GPIO.PWM(ENA2,1000)
p4=GPIO.PWM(ENB2,1000)

GPIO.output(in1,GPIO.HIGH)  ## emergency stop
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.HIGH)
GPIO.output(in5,GPIO.HIGH)
GPIO.output(in6,GPIO.HIGH)
GPIO.output(in7,GPIO.HIGH)
GPIO.output(in8,GPIO.HIGH)
p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
