# coding: UTF-8
from numpy import *
import operator


# 根据输入测试实例进行k-近邻分类
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 处理输入格式问题，从txt文件中读取数据
def file2matrix(filename, dim2):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, dim2))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split(',')
        returnMat[index, :] = listFromLine[0:dim2]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


# hoRatio是测试样本占总样本数的比例
def datingClassTest(k):
    hoRatio = 0.9
    datingDataMat, datingLabels = file2matrix('data.txt', 4)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], k)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):    errorCount += 1.0
    print("正确率: %f" % (1 - (errorCount / float(numTestVecs))))


# 测试函数，方便对新的单个数据进行测试
def classifyPerson():
    resultList = ['YES', 'NO']
    Months = float(input("Recency quantitative Months Input"))
    Times = float(input("Frequency quantitative Times Input"))
    blood = float(input("Monetary quantitative c.c. blood Input"))
    Timequan = float(input("Time quantitative Months Input"))
    datingDataMat, datingLabels = file2matrix('data.txt', 4)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([Months, Times, blood, Timequan])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 10)
    print('此人在2007年3月是否献血:', resultList[classifierResult - 1])
