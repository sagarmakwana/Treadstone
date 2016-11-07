# First XGBoost model for Pima Indians dataset
import numpy as np
import xgboost as xgb
import scipy.stats as scistat
from sklearn.decomposition import PCA

data = np.genfromtxt('mergeInfo.csv', delimiter = ',')

train_X = data[:,0:np.size(data,1)-1]
train_Y =data[:,np.size(data,1)-1]


#dataset = np.genfromtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
#train_X = dataset[:,0:8]
#train_Y = dataset[:,8]

print train_X.shape

train_X = scistat.zscore(train_X,axis = 0)
#Perform PCA
pca = PCA(n_components="mle")
transform_X = pca.fit_transform(train_X)

print transform_X.shape

dtrain = xgb.DMatrix(transform_X,label=train_Y)
dtest = xgb.DMatrix(transform_X[0:50000,:],label=train_Y[0:50000])
param = {'bst:max_depth':3, 'bst:eta':0.1, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = 'auc'
plst = param.items()
evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 10
bst = xgb.train( plst, dtrain, num_round, evallist )


ypred = bst.predict(dtest)

np.savetxt("prediction.csv",ypred,delimiter=",")
