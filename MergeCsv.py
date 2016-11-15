import numpy as np

questionFeatures = np.loadtxt("bytecup2016data/processedQuestionInfo.csv", dtype=str, delimiter=",")
wordFeatures = np.loadtxt("bytecup2016data/pcaWordInfo.csv", dtype=str, delimiter=",")
combinedQuestionFeatures = np.concatenate((questionFeatures, wordFeatures), axis=1)

featureRow = ''
with open('bytecup2016data/pcaQuestion.csv', 'wb') as pcaQuestion:
    for i in range(combinedQuestionFeatures.shape[0] - 1):
        for j in range(combinedQuestionFeatures.shape[1]-1):
            featureRow += combinedQuestionFeatures[i, j] + ','
        featureRow += combinedQuestionFeatures[i, j + 1]
        featureRow += '\n'
        pcaQuestion.write(featureRow)

userFeatures = np.loadtxt("bytecup2016data/processedUserInfo.csv", dtype=str, delimiter=",")
charFeatures = np.loadtxt("bytecup2016data/pcaCharacterInfo.csv", dtype=str, delimiter=",")
combinedUserFeatures = np.concatenate((userFeatures, charFeatures), axis=1)
np.savetxt('pcaUser.csv', combinedUserFeatures, delimiter=',')

featureRow = ''
with open('bytecup2016data/pcaUser.csv', 'wb') as pcaUser:
    for i in range(combinedUserFeatures.shape[0] - 1):
        for j in range(combinedUserFeatures.shape[1] - 1):
            featureRow += combinedUserFeatures[i, j] + ','
        featureRow += combinedUserFeatures[i, j + 1]
        featureRow += '\n'
        pcaUser.write(featureRow)