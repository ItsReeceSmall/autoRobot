import RPi.GPIO as gpio
import time, os, sys
import pins
import front
import sides

def setup():
    #set GPIO up
    gpio.setmode(gpio.BOARD)
    #Set up pins from a class
    lmf = 19
    lmb = 21
    rmf = 26
    rmb = 24
    sonar = 8
    trigL = 38
    echoL = 36
    trigR = 37
    echoR = 35
    # Set there categories
    inputs = [trigL,trigR]
    outputs = [sonar,lmf,lmb,rmf,rmb,echoL,echoR]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)
    print('### ALL PINS IMPORTED AND SETUP SUCCESSFULLY ###')
    while True:
        thefront = front.Front(sonar)
        thesidesLeft = sides.Sides(trigL, echoL)
        thesidesRight = sides.Sides(trigR, echoR)
        f = (thefront.Distance)
        l = (thesidesLeft.Distance)
        r = (thesidesRight.Distance)
        wheels = [rmf,rmb,lmf,lmb,f,l,r]
        thewheels = wheels.Wheels(wheels)
    #print(thefront.Distance)
    #print('left ' + thesidesLeft.Distance)
    #print('right ' + thesidesRight.Distance)
    
setup()
gpio.cleanup()
