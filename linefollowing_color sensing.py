from grove.gpio_rpi import GPIO
from grove.grove_i2c_motor_driver import MotorDrive
from ultrosonic_distance import distancex
from ultrosonic_distance import distancey


tDistance = 3  ## Tolerable distance 3cm

GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)

Lefttop_IR = GPIO(16, direction = GPIO.IN)  ## GPIO (PORT*) Lefttop IR out
Righttop_IR = GPIO(18, direction = GPIO.IN) ## GPIO port * righttop IR out
Leftbottom_IR = GPIO(20, direction = GPIO.IN)  ## GPIO port * leftbottom IR out\
Rightbottom_IR = GPIO(22, direction = GPIO.IN)   #### GPIO port * rightbottom IR out\

xCurrent = distancex
yCurrent = distancey
diffx = xCurrent - xPosition
diffy = yCurrent - yPosition

motor = MotorDriver()     ## initialise motor drive control
while 1:
    if (GPIO.read(16)==True and GPIO.read(18)==True and abs(diffx) >= tDistance and abs(diffy) >= tDistance):            ## moving straight
        MotorDriver.set_dir(clock_wise1 = True, Clock_wise2 = True,Clock_wise3 = True, Clock_wise4 = True)
        MotorDriver.set_speed(speed1 = 60, speed2 = 60, speed3 = 60, speed4 = 60)

    elif(GPIO.read(16)==False and GPIO.read(18)==True):          ## correct to the left
        MotorDriver.set_dir(clock_wise1 = False, clock_wise2 = True, clock_wise3 = True, Clock_wise4 = False)
        MotorDriver.set_speed( speed1 = 40, speed2 = 40, speed3 = 40, speed4 = 40)

    elif(GPIO.read(16)==True and GPIO.read(18)==False):   ## correction to the right
        MotorDriver.set_dir(clock_wise1 = True, clock_wise2 = False, clock_wise3 = False, Clock_wise4 = True)
        MotorDriver.set_speed( speed1 = 40, speed2 = 40, speed3 = 40, speed4 = 40)

    elif(GPIO.read(16)==False and GPIO.read(18)==False):  ## Intersection issue
        MotorDriver.set_dir(clock_wise1 = True, Clock_wise2 = True,Clock_wise3 = True, Clock_wise4 = True)
        MotorDriver.set_speed(speed1 = 30, speed2 = 30, speed3 = 30, speed4 = 30)

    elif(GPIO.read(16 == True and GPIO.read(18) == True and abs(diffx) == 0 and abs(diffy) == 0)):    ## turning movement
        MotorDriver.set_dir(clock_wise1 = True, clock_wise2 = False, clock_wise3 = False, clock_wise4 = True)
        MotorDriver.set_speed(Spee1 = 30, speed2 = 0, speed3 = 0, speed4 = 0)

    elif(GPIO.read(16) == True and GPIO.read(18) == True and abs(diffx) <= tDistance and abs(diffy) <= tDistance):      ##when motor stops
        MotorDriver.set_dir( clock_wise 1 = False, Clock_wise2 = False, clock_wise3 = False, clock_wise4 = False)
        MotorDriver.set_speed(Speed1=0, speed2=0, speed3=0, speed4 = 0)
    else:
        sleep(5)
        break
