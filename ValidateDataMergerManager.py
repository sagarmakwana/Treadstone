import numpy as np
import csv

def invokeDataMergeManager():
    global mergeFile
    print 'Operation started.'
    with open('bytecup2016data/validateDataSet.csv', 'wb') as mergeFile:
        mergeData()
    print 'Operation successful.'

def mergeData():
    questionFeatures = np.loadtxt("bytecup2016data/pcaQuestionInfo.csv", dtype=str, delimiter=",")
    userFeatures = np.loadtxt("bytecup2016data/pcaUserInfo.csv", dtype=str, delimiter=",")
    questionIdToFeatureMap = convertToDictionary(questionFeatures)
    userIdToFeatureMap = convertToDictionary(userFeatures)
    print 'Dictionaries ready'
    with open("bytecup2016data/validate_nolabel.txt") as tsv:
        for line in csv.reader(tsv, dialect=","):
            questionId = line[0]
            userId = line[1]
            combinedFeatureVectorString = questionIdToFeatureMap[questionId] + "," + userIdToFeatureMap[userId] + "\n"
            mergeFile.write(combinedFeatureVectorString)


def convertToDictionary(featureVector):
    featureMap = {}
    for keyIndex in range(featureVector.shape[0]):
        featureValue = ""
        featureIndex = 0
        for featureIndex in range(1, featureVector.shape[1] - 1):
            featureValue += featureVector[keyIndex, featureIndex] + ","
        featureValue += featureVector[keyIndex, featureIndex + 1]
        featureMap[featureVector[keyIndex, 0]] = featureValue
    return featureMap

invokeDataMergeManager()