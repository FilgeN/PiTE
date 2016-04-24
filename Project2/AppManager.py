from DataGenerator import generateData
from Fitter import fit
from StatAnalyser import testChi2
from Plotter import plotChart
from pylab import *

class AppManager():
    def __init__(self):
        print("Enter x range [A, B]\n")
        x_A = float(input("A = "))
        print('\n')
        x_B = float(input("B = "))
        print('\n')
        step = float(input("Step = "))
        print('\n')
        print("Enter noise range [C, D]\n")
        n_C = float(input("C = "))
        print('\n')
        n_D = float(input("D = "))
        print('\n\n')
        self.xValues = arange(x_A, x_B, step)
        self.yValues = generateData(self.xValues, [n_C, n_D])

    def start(self):
        self.yValuesFit = fit(self.xValues, self.yValues)
        chi2 = testChi2(self.xValues, self.yValuesFit)
        print("Test chi-2 = " + str(chi2))
        plotChart(self.xValues, self.yValues, self.yValuesFit)



if __name__=='__main__':
    appManager = AppManager()
    appManager.start()
