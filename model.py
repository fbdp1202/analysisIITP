# model.py

from openpyxl import load_workbook
from openpyxl import Workbook

import method

def makeDataRow(data, row):
    if not row[0] in data:
        data[row[0]] = []
    data[row[0]].append(row[1:3])

def load_excel_data(data, fileName):
    load_wb = load_workbook(fileName, data_only=True)
    load_ws = load_wb['Sheet1']

    data = {}
    for row in load_ws.rows:
        row_value = []
        for cell in row:
            row_value.append(cell.value)
        makeDataRow(data, row_value)

    data['Kmeans'].sort()
    return data

def setPrams(data):
    prams = {}
    totalNumTest = 300
    numVlnTest = 54
    numNonVlnTest = totalNumTest - numVlnTest

    prams['type'] = 'value'
    prams['totalNumTest'] = 300
    prams['numVlnTest'] = 54
    prams['numNonVlnTest'] = totalNumTest - numVlnTest

    prams['HitZeroVlnAllNonVln'] = method.getScore(numVlnTest,numNonVlnTest,0,numNonVlnTest)
    prams['HitOneNonVln'] = method.getScore(numVlnTest,numNonVlnTest, 0, 1)
    prams['HitOneVln'] = method.getScore(numVlnTest,numNonVlnTest, 1, 0)
    prams['HitAllVlnZeroNonVln'] = method.getScore(numVlnTest,numNonVlnTest,numVlnTest,0)

    prams['AvgOneHitOne'] = float(data['AllOne'][0][1])/float(prams['HitAllVlnZeroNonVln'])
    prams['HitOneVlnOne'] = prams['HitOneVln'] * prams['AvgOneHitOne']
    return prams

def checkDataSet(data, prams):
    print('\n'+"="*20+"  Print data  "+"="*20)
    for name in data:
        for factor, score in data[name]:
            print("{0:22s} {1:10s} {2:10s}".format(name, str(factor), str(score)))

    print('\n'+"="*20+"  Print prams "+"="*20)
    for name, value in prams.items():
        print("{0:33s} {1:25s}".format(name, str(value)))

def makeDataSet(fileName):
    data = {}
    data = load_excel_data(data, fileName)
    prams = setPrams(data)
    checkDataSet(data, prams)
    return data, prams

print('Load model.py')
