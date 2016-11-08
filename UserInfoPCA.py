import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

print "Starting operation"
data = pd.read_csv('bytecup2016data/processedUserInfo.csv', sep=",", header=None)
print "Data loaded"
train_QID = np.reshape(data.loc[:,0], (data.shape[0],1))
train_X = data.loc[:,1:np.size(data,1)-1]
train_X = train_X.astype(np.float)
print "PCA Start"
pca = PCA(n_components=2500)
transform_X = pca.fit_transform(train_X)
print "PCA End"
with open('bytecup2016data/pcaUserInfo.csv', 'wb') as pcaUserInfoFile:
    for index in range(transform_X.shape[0]):
        reducedFeature = str(train_QID[index,0]) + ","
        columnIndex = 0
        for columnIndex in range(transform_X.shape[1]-1):
            reducedFeature += str(transform_X[index,columnIndex]) + ","
        reducedFeature += str(transform_X[index,columnIndex+1]) + "\n"
        pcaUserInfoFile.write(reducedFeature)
print "Operation Successful"
