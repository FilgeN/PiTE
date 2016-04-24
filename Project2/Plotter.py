from pylab import *

def plotChart(xValues, yValues, yValuesFit):
    figure(1)
    plot(xValues, yValues, 'go')
    plot(xValues, yValuesFit, 'b')
    sinValues = [sin(x) for x in xValues]
    plot(xValues, sinValues, 'r')
    grid(True)
    show()

if __name__ == '__main__':
    plotChart(arange(0,4,0.1), arange(0,8,0.2))
