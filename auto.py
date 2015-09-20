import RPi.GPIO as gpio
import time
import sys

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

# runs setup for all the motor pins
startMotor(lmf, lmb, rmf, rmb)

# Try's statement to check if ultrasonic works
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

# Left Wheel Forward
#gpio.output(lmf, gpio.LOW)
#gpio.output(lmb, gpio.HIGH)
# Right wheel Forward
#gpio.output(rmf, gpio.LOW)
#gpio.output(rmb, gpio.HIGH)

#time.sleep(4)

# Left Wheel Back
#gpio.output(lmf, gpio.HIGH)
#gpio.output(lmb, gpio.LOW)
# Right Wheel Back
#gpio.output(rmf, gpio.HIGH)
#gpio.output(rmb, gpio.LOW)

#time.sleep(4)

gpio.cleanup()
