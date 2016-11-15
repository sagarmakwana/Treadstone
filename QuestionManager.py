# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 19:08:10 2016

@author: Sagar Makwana
"""
import numpy as np
import csv

def invokeQuestionManager():
    global questionFile
    global wordFile
    global characterFile
    with open('bytecup2016data/processedQuestionInfo.csv', 'wb') as questionFile, \
            open('bytecup2016data/processedQuestionWordInfo.csv', 'wb') as wordFile, \
            open('bytecup2016data/processedQuestionCharacterInfo.csv', 'wb') as characterFile:
        processQuestionData()
    print 'Operation successful.'

# This function will process question_info.txt and write the expanded version into processedQuestionInfo.csv

def processQuestionData():
    global questionTags
    global upvotes
    global noOfAnswers
    global noOfQualityAnswers
    global questionID
    global featureRow
    global wordRow
    global characterRow
    lineNumber = 1
    with open("bytecup2016data/question_info.txt") as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):

            featureRow = ''
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
            noOfAnswers = line[5]
            noOfQualityAnswers = line[6]

            wordIDVector[0, wordID] = 1
            charIDVector[0, charID] = 1

            featureVector = np.concatenate((featureVector, np.reshape(questionID, (1, 1))), axis=1)
            featureVector = np.concatenate((featureVector, np.reshape(questionTags, (1, 1))), axis=1)
            # featureVector = np.concatenate((featureVector, wordIDVector), axis=1)
            # featureVector = np.concatenate((featureVector, charIDVector), axis=1)
            featureVector = np.concatenate((featureVector, np.reshape(upvotes, (1, 1))), axis=1)
            featureVector = np.concatenate((featureVector, np.reshape(noOfAnswers, (1, 1))), axis=1)
            featureVector = np.concatenate((featureVector, np.reshape(noOfQualityAnswers, (1, 1))), axis=1)

            for i in range(featureVector.shape[1]-1):
                featureRow += featureVector[0,i] + ','
            featureRow += featureVector[0, i+1]
            featureRow += '\n'

            questionFile.write(featureRow)

            for i in range(wordIDVector.shape[1]-1):
                wordRow += wordIDVector[0,i] + ','
            wordRow += wordIDVector[0,i+1]
            wordRow += '\n'

            wordFile.write(wordRow)

            for i in range(charIDVector.shape[1] - 1):
                characterRow += charIDVector[0, i] + ','
            characterRow += charIDVector[0, i + 1]
            characterRow += '\n'

            characterFile.write(wordRow)



invokeQuestionManager()

