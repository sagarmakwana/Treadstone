# First XGBoost model for Pima Indians dataset
import numpy
import xgboost as xgb
import pickle


X = pickle.load(open("bytecup2016data/trainingFeatures.p","rb"))
Y = pickle.load(open("bytecup2016data/trainingLabel.p","rb"))


dtrain = xgb.DMatrix(X,label=Y)
dtest = xgb.DMatrix(X[0:1000,0:8],label=Y[0:1000])
param = {'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = 'auc'
plst = param.items()
evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 10
bst = xgb.train( plst, dtrain, num_round, evallist )


ypred = bst.predict(dtest)

print ypred

