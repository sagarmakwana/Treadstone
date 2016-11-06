# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 19:08:10 2016

@author: Sagar Makwana
"""
import numpy as np
import csv

def invokeQuestionManager():
    processQuestionData()
    print 'Operation successful.'

def processQuestionData():
    global questionTags
    global upvotes
    global noOfQualityAnswers
    global questionID
    global featureMatrix
    featureMatrix = np.zeros(shape=(0, 16195))
    lineNumber = 1
    with open("bytecup2016data/question_info.txt") as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            print lineNumber
            lineNumber += 1
            featureVector = np.zeros(shape=(1, 0))
            wordIDVector = np.zeros(shape=(1, 13232))
            charIDVector = np.zeros(shape=(1, 2960))
            questionID = line[0]
            questionTags = line[1]

            wordID = line[2].strip()
            if wordID == '/':
                wordID = '13231' + '/' + '13231'
            wordID = wordID.split('/')
            wordID = map(int, wordID)

            charID = line[3].strip()
            if charID == '/':
                charID = '2959' + '/' + '2959'
            charID = charID.split('/')
            charID = map(int, charID)

            upvotes = line[4]
            noOfQualityAnswers = line[5]
            wordIDVector[0, wordID] = 1
            charIDVector[0, charID] = 1
            featureVector = np.concatenate((featureVector, np.reshape(questionID, (1, 1))), axis=1)
            featureVector = np.concatenate((featureVector, wordIDVector), axis=1)
            featureVector = np.concatenate((featureVector, charIDVector), axis=1)
            featureVector = np.concatenate((featureVector, np.reshape(upvotes, (1, 1))), axis=1)
            featureVector = np.concatenate((featureVector, np.reshape(noOfQualityAnswers, (1, 1))), axis=1)
            featureMatrix = np.concatenate((featureMatrix, featureVector), axis=0)

    np.savetxt('bytecup2016data/processedQuestionData.csv', featureMatrix, delimiter=",")

invokeQuestionManager()