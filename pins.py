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
        