import RPi.GPIO as gpio
import time, os, sys
import pins

def setup(trigL, trigR, sonar, lmf, lmb, rmf, rmb, echoL, echoR):
    #set GPIO up
    print ('pins are called in fine')
    gpio.setmode(gpio.BOARD)
    print ('GPIO.BOARD is setup')
    #Set up pins from a class
    print(' attempts to do i as array')
    inputs = [trigL,trigR]
    print(' does i as an array thing')
    print(' attempts the same with o')
    outputs = [sonar,lmf,lmb,rmf,rmb,echoL,echoR]
    print('successfully does the same with o')
    print('attempts to define "pins" as the imported class Pins with arrays i and o in it')
    pins = pins.Pins(inputs, outputs)
    print('success')

# all the pins we will use
lmf = 19
lmb = 21
rmf = 26
rmb = 24
sonar = 8
trigL = 38
echoL = 36
trigR = 37
echoR = 35
print ('pins are defined')
print ('setup() is ran')
setup(trigL, trigR, sonar, lmf, lmb, rmf, rmb, echoL, echoR)
gpio.cleanup()
