from scipy.optimize import curve_fit
import numpy as np
from pylab import *
from DataGenerator import generateData

def mySin(x, a=1, b=1):
    return a*sin(b*x)

def fit(xValues, yValues):

    popt, pcov = curve_fit(mySin, xValues, yValues)
    yValuesFit = [ mySin(xV, popt[0], popt[1]) for xV in xValues ]

    return yValuesFit

if __name__=='__main__':
    xValues = arange(0, 7, 0.1)
    yValues = generateData( xValues, [-2, 2])

    yValuesFit = fit(xValues, yValues)

    figure(1)
    plot(xValues, yValues, 'go')
    plot(xValues, yValuesFit, 'b')
    sinValues = [ sin(x) for x in xValues]
    plot(xValues, sinValues, 'r')
    grid(True)
    show()