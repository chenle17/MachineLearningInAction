import numpy as np
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    inXNew = np.tile(inX, (dataSetSize, 1))
    diffMat = inXNew - dataSet
    sqDiffMat = diffMat**2
    sqlDistances = sqDiffMat.sum(axis=1)
    distances = sqlDistances**0.5
    sortedDistIndicies = np.argsort(distances)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        var = classCount.get(voteIlabel, 0)
        classCount[voteIlabel] = var + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)

    returnMat = np.zeros((numberOfLines,3))

    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1])) # datingTestSet2.txt
        # classLabelVector.append(listFromLine[-1]) # datingTestSet.txt
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataset):
    minValue = dataset.min(0)
    maxValue = dataset.max(0)
    ranges = maxValue - minValue
    # normDataSet = np.zeros(dataset.shape)
    m = dataset.shape[0]
    normDataSet = dataset -np.tile(minValue,(m,1))
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    return normDataSet,ranges,minValue

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:],
                                  datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %s, the real answer is: %s" % (classifierResult,datingLabels[i]))
        if (classifierResult != datingLabels[i]):errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/numTestVecs))

def classifyPerson():
    resultList = ['not ao all','in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing vidoe games"))
    ffMIles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

    normMat ,range , minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMIles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/range,normMat,datingLabels,3)
    print("you will ...:", resultList[classifierResult-1])

def img2Vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    fr.readlines()



