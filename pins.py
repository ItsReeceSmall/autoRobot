class Pins:
    def __init__(self, inputs, outputs):
        self.__inputs = inputs
        self.__outputs = outputs
        
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

    def setupPins(self):
        # RPi code to setup inputs
        for pin in self.__inputs:
            GPIO.setup(pin, GPIO.IN)

        # RPi code to setup outputs
        for pin in self.__outputs:
            GPIO.setup(pin, GPIO.OUT)


