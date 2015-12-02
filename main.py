import RPi.GPIO as gpio
import time, os, sys
import pins

def setup(trigL,trigR,sonar,lmf,lmb,rmf,rmb,echoL,echoR):
    #set GPIO up
    gpio.setmode(gpio.BOARD)
    #Set up pins from a class
    i = [trigL,trigR]
    o = [sonar,lmf,lmb,rmf,rmb,echoL,echoR]
    print('attempts to define "pins" as the imported class Pins with arrays i and o in it')
    thepins = pins.Pins(i, o)
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
setup(trigL,trigR,sonar,lmf,lmb,rmf,rmb,echoL,echoR)
gpio.cleanup()
