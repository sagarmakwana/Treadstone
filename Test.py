# First XGBoost model for Pima Indians dataset
import numpy as np
import xgboost as xgb

data = np.genfromtxt('mergeInfo.csv', delimiter = ',')
validate_X = np.genfromtxt('validateDataSet.csv', delimiter = ',')
train_X = data[:,0:np.size(data,1)-1]
train_Y =data[:,np.size(data,1)-1]


#dataset = np.genfromtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
#train_X = dataset[:,0:8]
#train_Y = dataset[:,8]

print train_X.shape

dtrain = xgb.DMatrix(train_X,label=train_Y)
#dtest = xgb.DMatrix(transform_X[0:50000,:],label=train_Y[0:50000])
dvalidate = xgb.DMatrix(validate_X)
param = {'bst:max_depth':3, 'bst:eta':0.1, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = 'auc'
plst = param.items()
#evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 10
bst = xgb.train( plst, dtrain, num_round )


ypred = bst.predict(dvalidate)

ypred = np.reshape(ypred,(ypred.shape[0],1))

result = np.genfromtxt('bytecup2016data/validate_nolabel.csv',delimiter=',',skip_header=1,dtype=str)

result = np.concatenate((result,ypred),axis= 1)

np.savetxt('result.csv',result,delimiter=',',fmt="%s")


np.savetxt("prediction.csv",ypred,delimiter=",")
