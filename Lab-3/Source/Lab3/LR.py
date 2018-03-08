from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
# loading dataset
irisDS= datasets.load_iris()
info = irisDS.data
tag = irisDS.target
info_train, info_test, tag_train, tag_test=train_test_split(info, tag, test_size=0.2, random_state=36)
design = LogisticRegression()
#fitting data
Q=design.fit(info_train, tag_train)
targ_nams = irisDS.target_names
# predicting data
y_predLDA=design.predict(info_test)
# accuracy
LR=metrics.accuracy_score(y_predLDA, tag_test)
print(" \n Required accuracy score is: ", LR)