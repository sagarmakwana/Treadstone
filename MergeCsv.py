import numpy as np
from sklearn.decomposition import PCA


userFeatures = np.loadtxt("bytecup2016data/processedUserInfo.csv", dtype=str, delimiter=",")
train_X_User_Tags = userFeatures[:,1:]
train_X_User_Tags = train_X_User_Tags.astype(np.float)
pca = PCA(n_components=10)
transformUserTags = pca.fit_transform(train_X_User_Tags)
userFeatures = userFeatures[:,0]
userFeatures = np.concatenate((userFeatures,transformUserTags), axis=1)
userWordFeatures = np.loadtxt("bytecup2016data/pcaUserWordInfo.csv", dtype=str, delimiter=",")
userCharFeatures = np.loadtxt("bytecup2016data/pcaUserCharacterInfo.csv", dtype=str, delimiter=",")
tempCombinedUserFeatures = np.concatenate((userFeatures, userWordFeatures), axis=1)
combinedUserFeatures = np.concatenate((tempCombinedUserFeatures, userCharFeatures), axis=1)

np.savetxt('pcaUser.csv', combinedUserFeatures, delimiter=',')


with open('bytecup2016data/pcaUser.csv', 'wb') as pcaUser:
    for i in range(combinedUserFeatures.shape[0]):
        featureRow = ''
        for j in range(combinedUserFeatures.shape[1] - 1):
            featureRow += combinedUserFeatures[i, j] + ','
        featureRow += combinedUserFeatures[i, j + 1]
        featureRow += '\n'
        pcaUser.write(featureRow)
questionFeatures = np.loadtxt("bytecup2016data/processedQuestionInfo.csv", dtype=str, delimiter=",")
questionWordFeatures = np.loadtxt("bytecup2016data/pcaQuestionWordInfo.csv", dtype=str, delimiter=",")
questionCharacterFeatures = np.loadtxt("bytecup2016data/pcaQuestionCharacterInfo.csv", dtype=str, delimiter=",")
tempCombinedQuestionFeatures = np.concatenate((questionFeatures, questionWordFeatures), axis=1)
combinedQuestionFeatures = np.concatenate((tempCombinedQuestionFeatures, questionCharacterFeatures), axis=1)


with open('bytecup2016data/pcaQuestion.csv', 'wb') as pcaQuestion:
    for i in range(combinedQuestionFeatures.shape[0]):
        featureRow = ''
        for j in range(combinedQuestionFeatures.shape[1]-1):
            featureRow += combinedQuestionFeatures[i, j] + ','
        featureRow += combinedQuestionFeatures[i, j + 1]
        featureRow += '\n'
        pcaQuestion.write(featureRow)