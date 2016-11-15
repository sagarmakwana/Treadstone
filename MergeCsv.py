import numpy as np

questionFeatures = np.loadtxt("bytecup2016data/processedQuestionInfo.csv", dtype=str, delimiter=",")
wordFeatures = np.loadtxt("bytecup2016data/pcaWordInfo.csv", dtype=str, delimiter=",")
combinedQuestionFeatures = np.concatenate((questionFeatures, wordFeatures), axis=1)
np.savetxt('pcaQuestion.csv', combinedQuestionFeatures, delimiter=',')

userFeatures = np.loadtxt("bytecup2016data/processedUserInfo.csv", dtype=str, delimiter=",")
charFeatures = np.loadtxt("bytecup2016data/pcaCharacterInfo.csv", dtype=str, delimiter=",")
combinedUserFeatures = np.concatenate((userFeatures, charFeatures), axis=1)
np.savetxt('pcaUser.csv', combinedUserFeatures, delimiter=',')