# analyzer.py

import numpy as np
import math
from scipy.interpolate import interp1d

from method import *
import canvas

def drawKmeans(data, prams):
    x = []
    y = []

    for factor, score in data['Kmeans']:
        x.append(factor)
        y.append(getLoss(factor, score, data, prams))

    f1 = interp1d(x, y, kind='cubic', fill_value="extrapolate")
    xnew = np.linspace(54, 250, num=205, endpoint=True)

    canvas.drawPlot(x, y, 'o', 2, 'Kmeans Loss num', 'score', 'factor', 'num', 'blue')
    canvas.drawPlot(xnew, f1(xnew), '-', 2, 'Kmeans Loss num', 'cubic', 'factor', 'num', 'red')

    return f1

def drawPredictKmeans(data, prams, f1):
    x = []
    y = []
    for factor, score in data['Kmeans']:
        x.append(float(factor))
        y.append(float(score)*100)

    f2 = interp1d(x, y, kind='cubic', fill_value="extrapolate")
    xnew = np.linspace(54, 250, num=205, endpoint=True)
    nVf = nonVlnFunc(xnew, prams['HitOneNonVln'], prams['numVlnTest'])
    bVLf = basicVlnLossFunc(xnew, prams['HitAllVlnZeroNonVln']*(1-prams['AvgOneHitOne']))
    addLossf = additionLossFunc(f1(xnew), prams['HitOneVln']*prams['AvgOneHitOne']+prams['HitOneNonVln'])
    maxScoref = maxScoreFunc(nVf, bVLf)

    canvas.drawPlot(x, y, 'o', 1, 'Kmeans Score', 'score', 'factor', 'score', 'blue')
    canvas.drawPlot(xnew, f2(xnew), '-', 1, 'Kmeans Score', 'cubic', 'factor', 'score', 'red')
    canvas.drawPlot(xnew, nVf, '-', 1, 'Kmeans Score', 'NonVlnLoss', 'factor', 'score', 'green')
    canvas.drawPlot(xnew, bVLf, '-', 1, 'Kmeans Score', 'basicVlnLoss', 'factor', 'score', 'purple')
    canvas.drawPlot(xnew, addLossf, '-', 1, 'Kmeans Score', 'additionLoss', 'factor', 'score', 'orange')
    canvas.drawPlot(xnew, maxScoref, '-', 1, 'Kmeans Score', 'maxScore', 'factor', 'score', 'black')

def analysisKmeans(data, prams):
    f1 = drawKmeans(data, prams)
    drawPredictKmeans(data, prams, f1)

def analysisHitNum(data, prams):
    print('\n'+"="*18+"  analysisHitNum "+"="*18)
    for name in data:
        for factor, score in data[name]:
            if factor == None or factor == 'x' or factor == 0 or factor == 'factor':
                continue
            hitNum = getHitnum(prams, factor, score)
            print('{:18s} : Hit Number is ({:2.3f} / {:>3d})  %{:2.3f}'.format(name, hitNum, factor, float(hitNum/factor*100)))

print('analyzer.py')