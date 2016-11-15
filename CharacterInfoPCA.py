import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

print "Starting operation"
dataQuestion = pd.read_csv('bytecup2016data/processedQuestionCharacterInfo.csv', sep=",", header=None)
dataUser = pd.read_csv('bytecup2016data/processedUserCharacterInfo.csv', sep=",", header=None)
print "Data loaded"
# train_QID = np.reshape(data.loc[:,0], (data.shape[0],1))
train_X_Question = dataQuestion.loc[:, :]
train_X_Question = train_X_Question.astype(np.float)

train_X_User = dataUser.loc[:, :]
train_X_User = train_X_User.astype(np.float)

print "PCA Start"
pca = PCA(n_components=2500)
transform_X_Question = pca.fit_transform(train_X_Question)
transform_X_User = pca.fit_transform(train_X_User)
print "PCA End"
with open('bytecup2016data/pcaCharacterInfo.csv', 'wb') as pcaCharacterInfoFile:
    for index in range(transform_X_Question.shape[0]):
        reducedFeature = ""
        columnIndex = 0
        for columnIndex in range(transform_X_Question.shape[1]-1):
            reducedFeature += str(transform_X_Question[index,columnIndex]) + ","
        reducedFeature += str(transform_X_Question[index,columnIndex+1]) + ","
        for columnIndex in range(transform_X_Question.shape[1] - 1):
            reducedFeature += str(transform_X_Question[index, columnIndex]) + ","
        reducedFeature += str(transform_X_Question[index, columnIndex + 1]) + "\n"
        pcaCharacterInfoFile.write(reducedFeature)
print "Operation Successful"