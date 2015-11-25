import RPi.GPIO as gpio
import time, sys, os, glob, threading

gpio.setmode(gpio.BOARD)

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
