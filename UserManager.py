# -*- coding: utf-8 -*-
import numpy as np
import csv

def invokeUserManager():
    processUserData()
    print 'Operation successful.' 


def processUserData():
    global questionTags
    global questionID
    global featureMatrix

    lineNumber = 1
    featureMatrix = np.zeros(shape=(0, 35023))

    with open("bytecup2016data/user_info.txt") as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            print lineNumber
            lineNumber += 1
            featureVector = np.zeros(shape=(1, 0))
            wordIDVector = np.zeros(shape=(1, 31100))
            charIDVector = np.zeros(shape=(1, 3779))
            tagIDVector = np.zeros(shape=(1, 143))

            userID = line[0]

            tagID = line[1].strip()
            if tagID == '/':
                tagID = '142' + '/' + '142'
            tagID = tagID.split('/')
            tagID = map(int, tagID)

            wordID = line[2].strip()
            if wordID == '/':
                wordID = '31099' + '/' + '31099'
            wordID = wordID.split('/')
            wordID = map(int, wordID)

            charID = line[3].strip()
            if charID == '/':
                charID = '3778' + '/' + '3778'
            charID = charID.split('/')
            charID = map(int, charID)

            tagIDVector[0, tagID] = 1
            wordIDVector[0, wordID] = 1
            charIDVector[0, charID] = 1

            featureVector = np.concatenate((featureVector, np.reshape(userID, (1, 1))), axis=1)
            featureVector = np.concatenate((featureVector, tagIDVector), axis=1)
            featureVector = np.concatenate((featureVector, wordIDVector), axis=1)
            featureVector = np.concatenate((featureVector, charIDVector), axis=1)
            featureMatrix = np.concatenate((featureMatrix, featureVector), axis=0)

invokeUserManager()