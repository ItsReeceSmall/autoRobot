import RPi.GPIO as gpio
import time, sys, os

class Wheels:
  def __init__(self, wheels):
    self.__wheels = wheels
    self.wheelsGo()
    
  @property
  def wheels(self):
    return self.__wheels
  @wheels.setter
  def wheels(self, value):
    self.__wheels = value
  
  def wheelsGo(self):
    print ('#######################')
    print ('Left: ' + str(l))        # Prints the distance on screen to show what the pi is detecting
    if l < 25:
        lmfPWM.ChangeDutyCycle(65)
        print('')
        print ('lmf speed = 65')
        lmbPWM.ChangeDutyCycle(0)
        rmfPWM.ChangeDutyCycle(100)
        print ('rmf speed = 100')
        print(' ')
        rmbPWM.ChangeDutyCycle(0)
        time.sleep(1)
        print ('reset to 100 and 96')
        print (' ')
        lmfPWM.ChangeDutyCycle(100)
        rmfPWM.ChangeDutyCycle(96)                    # If the distance is lower than 25cm then the code below is ran.
    print ('Right: ' + str(r))      # Prints the distance on screen to show what the pi is detecting
    if r < 25:
        lmfPWM.ChangeDutyCycle(100)
        print('')
        print ('lmf speed = 100')
        lmbPWM.ChangeDutyCycle(0)
        rmfPWM.ChangeDutyCycle(65)
        print ('rmf speed = 65')
        print('')
        rmbPWM.ChangeDutyCycle(0)
        time.sleep(1)
        print ('reset to 96')
        print (' ')
        rmfPWM.ChangeDutyCycle(96)                   # If the distance is lower than 25cm then the code below is ran.
    print ('Front: ' + str(f))      # Prints the distance on screen to show what the pi is detecting
    if f < 40:                      # If the front sensor is less than 40cm away from a block, it will run the code below
        lmfPWM.ChangeDutyCycle(0)
        lmbPWM.ChangeDutyCycle(0)       # All the motors are stopped, set to 0
        rmfPWM.ChangeDutyCycle(0)
        rmbPWM.ChangeDutyCycle(0)
        if l < r:                # Checks if the left distance is less than the right, if True, code below is ran
            print('Going Back')
            lmbPWM.ChangeDutyCycle(55)  # The wheels go backwards
            rmbPWM.ChangeDutyCycle(55) 
            time.sleep(2)               # For 2 seconds
            print('Rotating Right')
            lmbPWM.ChangeDutyCycle(53)
            rmfPWM.ChangeDutyCycle(53)  # The Wheels rotate opposite ways to turn away from the block
            time.sleep(1.7)             # For 1.7 seconds
            lmbPWM.ChangeDutyCycle(0)   # Both wheels stop and are set to 0
            rmfPWM.ChangeDutyCycle(0)
        if r < l:                # Checks if the right distance is less than the left, if True, code below is ran
            print('Going Back')
            lmbPWM.ChangeDutyCycle(55)  # The wheels go backwards
            rmbPWM.ChangeDutyCycle(55)
            time.sleep(2)               # For 2 seconds
            print('Rotating Left')
            lmfPWM.ChangeDutyCycle(53)
            rmbPWM.ChangeDutyCycle(53)  # The wheels rotate opposite ways to turn away from the block
            time.sleep(1.7)             # For 1.7 seconds
            lmfPWM.ChangeDutyCycle(0)   # Both wheels stop and are set to 0
            rmbPWM.ChangeDutyCycle(0)
        print('Normal Speed')
        lmfPWM.ChangeDutyCycle(100)
        rmfPWM.ChangeDutyCycle(96)     # Wheels return to normal speed before restarting the loop and checking for blockages again.
        lmbPWM.ChangeDutyCycle(0)
        rmbPWM.ChangeDutyCycle(0)
