from Fitter import mySin
from pylab import *
from DataGenerator import generateData
from Fitter import fit

def testChi2(xValues, yValues):
    chiValues = []
    for i in range( len(xValues) ):
        chiValues.append( yValues - mySin(xValues[i]) )

    avarage = sum(yValues)/len(yValues)

    variancesValues = [ (y-avarage)**2 for y in yValues]

    deviationValues = [ vv**(0.5) for vv in variancesValues ]

    for i in range( len(yValues) ):
        chiValues[i] = ( chiValues[i]/deviationValues[i] )**2

    chi2 = sum(chiValues)

    return  chi2

if __name__=='__main__':
    xValues = arange(0, 7, 0.1)
    yValues = generateData(xValues, [-2, 2])

    yValuesFit = fit(xValues, yValues)
    chi2 = testChi2(xValues, yValuesFit)

    print(chi2)
