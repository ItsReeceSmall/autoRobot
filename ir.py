import RPi.GPIO as gpio
import time, sys, os

class IR:
  def __init__(self, irFL, irFR, irMID):
