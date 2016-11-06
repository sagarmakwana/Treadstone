import numpy as np
import csv

def invokeDataMergeManager():
    global mergeFile
    with open('bytecup2016data/mergeInfo.csv', 'wb') as mergeFile:
        mergeData()
    print 'Operation successful.'

def mergeData():
    questionFeatures = np.loadtxt("bytecup2016data/processedQuestionInfo.csv", dtype=str, delimiter=",")
    userFeatures = np.loadtxt("bytecup2016data/processedUserInfo.csv", dtype=str, delimiter=",")
    questionIdToFeatureMap = convertToDictionary(questionFeatures)
    userIdToFeatureMap = convertToDictionary(userFeatures)
    with open("bytecup2016data/invited_info_train_dummy.txt") as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            questionId = line[0]
            userId = line[1]
            label = line[2]
            combinedFeatureVectorString = questionIdToFeatureMap[questionId] + "," + userIdToFeatureMap[userId] + "," + label + "\n"
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