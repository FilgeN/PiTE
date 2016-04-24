from random import uniform
from pylab import *

def generateData(xValues, noise):
    # random.seed(None)
    yValues = [sin(x)+uniform(noise[0],noise[1]) for x in xValues]
    return yValues



if __name__=='__main__':
    yV = generateData( arange(0, 2, 0.1), [-5, 5] )
    print( yV )