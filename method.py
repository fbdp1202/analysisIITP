# method.py

def getScore(numVlnTest, numNonVlnTest, numHitVln, numHitNonVln):
    return (numHitVln+numHitNonVln/10.)/float(numVlnTest+numNonVlnTest/10)

def getHitnum(prams, thres, score):
    A = prams['HitOneVlnOne']
    B = prams['HitOneNonVln']
    C = thres
    D = prams['totalNumTest'] - thres
    result = (score+prams['numVlnTest']*B-B*D)/(A+B)
    return result

def nonVlnFunc(x, inc, bias):
    y = []
    for i in x:
        y.append(inc*(i-bias)*100)
    return y

def basicVlnLossFunc(x, bias):
    y = []
    for i in x:
        y.append(bias*100)
    return y

def maxScoreFunc(nonVlnLoss, basicVlnLoss):
    y = []
    for i in range(len(nonVlnLoss)):
        y.append(100 - nonVlnLoss[i] - basicVlnLoss[i])
    return y

def additionLossFunc(x, inc):
    y = []
    for i in x:
        y.append(inc*i*100)
    return y

def getLoss(factor, score, data, prams):
    A = prams['HitOneNonVln']
    B = prams['HitOneVln']
    alpha = prams['AvgOneHitOne']

    numVln = prams['numVlnTest']
    loss = 1 - A*(factor-numVln) - numVln*B + alpha*numVln*B - score
    loss = loss/float(alpha*B + A)
    return loss

print('method.py')