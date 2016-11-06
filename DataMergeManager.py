import numpy as np
import csv
import pickle

def invokeDataMergeManager():
    mergeData()
    #dumpMergedData()
    print 'Operation successful.'

def mergeData():
    global featureArray
    global labelArray
    labelList = []
    featureList = []
    with open("bytecup2016data/invited_info_train.txt") as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            questionId = line[0]
            userId = line[1]
            label = line[2]
            questionIdToFeatureMap = pickle.load(open("bytecup2016data/processedQuestionData.p", "rb"))
            userIdToFeatureMap = pickle.load(open("bytecup2016data/processedUserData.p", "rb"))
            combinedFeatureVector = np.concatenate([questionIdToFeatureMap[questionId], userIdToFeatureMap[userId]], axis=1)
            combinedFeatureList = np.ndarray.tolist(combinedFeatureVector)
            featureList.append(combinedFeatureList)
            labelList.append(label)
        featureArray = np.asarray(featureList)
        labelArray = np.asarray(featureList)
        print featureArray.shape
        print label.shape



invokeDataMergeManager()