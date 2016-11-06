# First XGBoost model for Pima Indians dataset
import numpy
import xgboost as xgb

# load data
dataset = numpy.genfromtxt('pima-indians-diabetes.csv', delimiter=",")
# split data into X and y
X = dataset[:,0:8]
Y = dataset[:,8]


dtrain = xgb.DMatrix(X,label=Y)
dtest = xgb.DMatrix(X[0:100,0:8],label=Y[0:100])
param = {'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic' }
param['nthread'] = 4
param['eval_metric'] = 'auc'
plst = param.items()
evallist  = [(dtest,'eval'), (dtrain,'train')]
num_round = 10
bst = xgb.train( plst, dtrain, num_round, evallist )


ypred = bst.predict(dtest)

print ypred

