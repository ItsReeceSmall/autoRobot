import RPi.GPIO as gpio
import time, os, sys

class Pins:
    def __init__(self, inputs, outputs):
        self.__inputs = inputs
        self.__outputs = outputs
        self.printPins()
        
    @property
    def Inputs(self):
        return self.__inputs
    
    @Inputs.setter
    def Inputs(self, value):
        self.__inputs = value
        
    @property
    def Outputs(self):
        return self.__outputs
        
    @Outputs.setter
    def Outputs(self, value):
        self.__outputs = value
    
    # Need to write code to setup all the pins that have been passed in
    
    def printPins(self):
        for pin in self.__inputs:
            gpio.setup(pin, gpio.IN)
            print ('### Pin ' + str(pin) + ' is setup')
        for pin in self.__outputs:
            gpio.setup(pin, gpio.OUT)
            print ('### Pin ' + str(pin) + ' is setup')
            # Right Wheel Forward
        rmfPWM = gpio.PWM(wheelPins.rmf,100)  # Right Motor Forward, sets power output to 100
        rmbPWM = gpio.PWM(wheelPins.rmb,100)  # Right Motor Back, sets power output to 100
        rmfPWM.start(0) # starts on 0
        rmbPWM.start(0) # starts on 0
        rmfPWM.ChangeDutyCycle(96)  # Right Motor Forward changes its power its recieving to 96
        rmbPWM.ChangeDutyCycle(0)   # Right Motor Back has 0 recieving power as we dont want it to go back
            # Left Wheel Forward
        lmfPWM = gpio.PWM(wheelPins.lmf,100)  # Left Motor Forward, sets power output to 100
        lmbPWM = gpio.PWM(wheelPins.lmb,100)  # Left Motor Back, sets power output to 100
        lmfPWM.start(0) # starts on 0
        lmbPWM.start(0) # starts on 0
        lmfPWM.ChangeDutyCycle(100) # Left Motor Forward changes its power its recieving to 96
        lmbPWM.ChangeDutyCycle(0)   # Left Motor Back has 0 recieving power as we dont want it to go back
