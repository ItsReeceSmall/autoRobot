import RPi.GPIO as GPIO
import pins

def setup():
    #set GPIO up
    
    #Set up pins from a class
    i = [1,2,3]
    o = [4,5,6]
    pins = pins.Pins(i, o)
    
    # test comment
    