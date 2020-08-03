# canvas.py

import matplotlib.pyplot as plt

def drawPlot(x, y, shape, pltNum, pltTitle, pltlabel, pltXlabel, pltYlabel, color):
    plt.figure(pltNum)
    plt.title(label=pltTitle, loc='center', pad=10.)
    plt.plot(x, y, shape, color=color, label=pltlabel)
    plt.xlabel(pltXlabel)
    plt.ylabel(pltYlabel)
    plt.legend()

def showPlot():
    plt.show()

print('canvas.py')