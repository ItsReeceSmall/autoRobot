import RPi.GPIO as gpio
import time, os, sys
import pins

def setup(trigL,trigR,sonar,lmf,lmb,rmf,rmb,echoL,echoR):
    #set GPIO up
    gpio.setmode(gpio.BOARD)
    #Set up pins from a class
    i = [trigL,trigR]
    o = [sonar,lmf,lmb,rmf,rmb,echoL,echoR]
    pins = pins.Pins(i, o)

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

setup()
