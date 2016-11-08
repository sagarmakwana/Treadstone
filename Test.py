# First XGBoost model for Pima Indians dataset
import numpy as np
import xgboost as xgb
import pandas as pd

print 'Operation started.'
data = pd.read_csv('bytecup2016data/mergeInfo.csv', sep = ',', header=None)
validate_X = pd.read_csv('bytecup2016data/validateDataSet.csv', sep = ',', header=None)
validate_X = validate_X.as_matrix()

train_X = data.ix[:,range(data.shape[1]-1)].values
train_Y = data.ix[:,data.shape[1]-1].values

print 'Data loaded'

#dataset = np.genfromtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
#train_X = dataset[:,0:8]
#train_Y = dataset[:,8]

dtrain = xgb.DMatrix(train_X,label=train_Y)
dvalidate = xgb.DMatrix(validate_X)
param = {'bst:max_depth':3, 'bst:eta':0.1, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = 'auc'
plst = param.items()
num_round = 10
bst = xgb.train( plst, dtrain, num_round )
print 'XGBoost completed.'

ypred = bst.predict(dvalidate)
ypred = np.reshape(ypred,(ypred.shape[0],1))
result = np.genfromtxt('bytecup2016data/validate_nolabel.txt',delimiter=',',dtype=str)
result = np.concatenate((result,ypred),axis= 1)
np.savetxt('result.csv',result,delimiter=',',fmt="%s")
print 'Operation successful.'
np.savetxt("prediction.csv",ypred,delimiter=",")
