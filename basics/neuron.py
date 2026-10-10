import typing
import math
import matplotlib.pyplot as plt

class ActivationFunction():
    def ReLU(y: float):
        return max(0,y)
    def Sigmoid(y: float):
        return 1/(1+math.e**(-y))
    
    def graph(function: typing.Callable):
        X = [x for x in range(-100,101)]
        Y = [function(x) for x in X]
        plt.plot(X,Y)
        plt.title(function.__name__)
        plt.show()

ActivationFunction.graph(ActivationFunction.Sigmoid)


    
    