import RPi.GPIO as gpio
import time, sys, os

class IR:
    def __init__(self, irFL, irFR, irMID):
        self.__irFL = irFL
        self.__irFR = irFR
        self.__irMID = irMID
        self.__detection = detection
        self.__irAll()
    
    @property
    def detection(self):
        return self.__detection
    @detection.setter
    def detection(self, value):
        self.__detection = value
    
    @property
    def irFL(self):
        return self.__irFL
    @irFL.setter
    def irFL(self, value):
        self.__irFL = value
    
    @property
    def irFR(self):
        return self.__irFR
    @irFR.setter
    def irFR(self, value):
        self.__irFR = value
    
    @property
    def irMID(self):
        return self.__irMID
    @irMID.setter
    def irMID(self, value):
        self.__irMID = value
    
    def irAll(self):
        if gpio.input(irFL)==0 or gpio.input(irFR)==0 and gpio.input(irMID)==0:
            self.__detection = 1
        else:
            self.__detection = 0
