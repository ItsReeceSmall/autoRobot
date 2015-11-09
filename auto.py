import RPi.GPIO as gpio
#from Adafruit_PWM_Servo_Driver_py3 import PWM
import time
import sys

#def getLeftDist():

def getSideDist(TRIG, ECHO):
    gpio.setup(TRIG,gpio.OUT)
    gpio.setup(ECHO,gpio.IN)
    gpio.output(TRIG, False)
    #print "Waiting For Sensor To Settle"
    time.sleep(1)
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)
    while gpio.input(ECHO)==0:
      pulse_start = time.time()
    while gpio.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    #print ("Distance: " + str(distance) + "cm")
    return distance

def getDistance(sonar):
    gpio.setup(sonar, gpio.OUT)
    # Send 10us pulse to trigger
    gpio.output(sonar, True)
    time.sleep(0.00001)
    gpio.output(sonar, False)
    start = time.time()
    count=time.time()
    gpio.setup(sonar, gpio.IN)
    while gpio.input(sonar)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    while gpio.input(sonar)==1 and time.time()-count<0.1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound 34000(cm/s) divided by 2
    distance = elapsed * 17000
    return distance

# sets up all the motor pins
def startMotor(lmf, lmb, rmf, rmb):
    gpio.setup(lmf, gpio.OUT)
    gpio.setup(lmb, gpio.OUT)
    gpio.setup(rmf, gpio.OUT)
    gpio.setup(rmb, gpio.OUT)

# sets what board type we will use
gpio.setmode(gpio.BOARD)

# all the pins we will use
lmf = 19
lmb = 21
rmf = 24
rmb = 26
sonar = 8
trigL = 38
echoL = 36
trigR = 37
echoR = 35
# runs setup for all the motor pins
startMotor(lmf, lmb, rmf, rmb)

#Wheels
    # Right wheel Forward
rmfPWM = gpio.PWM(rmf,100)
rmbPWM = gpio.PWM(rmb,100)
rmfPWM.start(0)
rmbPWM.start(0)
rmfPWM.ChangeDutyCycle(0)
rmbPWM.ChangeDutyCycle(96)
    # Left Wheel Forward
lmfPWM = gpio.PWM(lmf,100)
lmbPWM = gpio.PWM(lmb,100)
lmfPWM.start(0)
lmbPWM.start(0)
lmfPWM.ChangeDutyCycle(100)
lmbPWM.ChangeDutyCycle(0)
    
while True:
    left = getSideDist(trigL, echoL)
    print (left)
    if left < 25:
        lmfPWM.ChangeDutyCycle(100)
        print 'lmf speed = 100'
        lmbPWM.ChangeDutyCycle(0)
        rmfPWM.ChangeDutyCycle(85)
        print 'rmf speed = 85'
        rmbPWM.ChangeDutyCycle(0)
    right = getSideDist(trigR, echoR)
    print (right)
    if right < 25:
        lmfPWM.ChangeDutyCycle(85)
        print 'lmf speed = 85'
        lmbPWM.ChangeDutyCycle(0)
        rmfPWM.ChangeDutyCycle(100)
        print 'rmf speed = 100'
        rmbPWM.ChangeDutyCycle(0)

# Try's statement to check if ultrasonic works
'''
try:
# runs over and over checking the ultrasonic sensor
    while True:
    # sets 'dist' to the value of the ultrasonic sensor, and imports 'sonar' to the pin number 8
        dist = getDistance(sonar)
        time.sleep(0.5)
        # optional print
        print (dist)
except:
# if there is a problem, program then this is printed and the sensor is no longer checked.
    print('Program interrupted')
'''
time.sleep(10)
gpio.cleanup()
sys.exit()
# Left Wheel Back
#gpio.output(lmf, gpio.HIGH)
#gpio.output(lmb, gpio.LOW)
# Right Wheel Back
#gpio.output(rmf, gpio.HIGH)
#gpio.output(rmb, gpio.LOW)
