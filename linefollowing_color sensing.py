from grove.gpio_rpi import GPIO
from grove.grove_i2c_motor_driver import MotorDrive
from ultrasonic_distance import distancex, distancey
import time

tDistance = 3  ## Tolerable distance 3cm

GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)


Left_IR = GPIO(16, direction = GPIO.IN)  ## GPIO (PORT*) left color sensor
Right_IR = GPIO(18, direction = GPIO.IN) ## GPIO port * right color sensor


xPosition = 10   ##this number called from input from user
yPosition = 20   ## this number called form input from user

motor = MotorDrive()     ## initialise motor drive control
while 1:
    curr_x = distancex()
    time.sleep(0.5)
    curr_y = distancey()
    time.sleep(0.5) # could probably be smaller

    diffx = curr_x - xPosition
    diffy = curr_y - yPosition


    if (GPIO.read(16)==True and GPIO.read(18)==True and abs(diffx) >= tDistance and abs(diffy) >= tDistance):            ## moving straight
        motor.set_dir(clock_wise1 = True, Clock_wise2 = True,Clock_wise3 = True, Clock_wise4 = True)
        motor.set_speed(speed1 = 60, speed2 = 60, speed3 = 60, speed4 = 60)

    elif(GPIO.read(16)==False and GPIO.read(18)==True):          ## correct to the left
        motor.set_dir(clock_wise1 = False, clock_wise2 = True, clock_wise3 = True, Clock_wise4 = False)
        motor.set_speed( speed1 = 40, speed2 = 40, speed3 = 40, speed4 = 40)

    elif(GPIO.read(16)==True and GPIO.read(18)==False):   ## correction to the right
        motor.set_dir(clock_wise1 = True, clock_wise2 = False, clock_wise3 = False, Clock_wise4 = True)
        motor.set_speed( speed1 = 40, speed2 = 40, speed3 = 40, speed4 = 40)

    elif(GPIO.read(16)==False and GPIO.read(18)==False):  ## Intersection issue
        motor.set_dir(clock_wise1 = True, Clock_wise2 = True,Clock_wise3 = True, Clock_wise4 = True)
        motor.set_speed(speed1 = 30, speed2 = 30, speed3 = 30, speed4 = 30)

    elif(GPIO.read(16 == True and GPIO.read(18) == True and abs(diffx) <= tDistance and abs(diffy) > tDistance)):    ## turning movement
        motor.set_dir(clock_wise1 = True, clock_wise2 = False, clock_wise3 = False, clock_wise4 = True)
        motor.set_speed(Spee1 = 30, speed2 = 0, speed3 = 0, speed4 = 30)

    elif(GPIO.read(16) == True and GPIO.read(18) == True and abs(diffx) <= tDistance and abs(diffy) <= tDistance):      ##when motor stops
        motor.set_dir( clock_wise1 = False, Clock_wise2 = False, clock_wise3 = False, clock_wise4 = False)
        motor.set_speed(Speed1=0, speed2=0, speed3=0, speed4 = 0)
    else:
        time.sleep(5)
        break
