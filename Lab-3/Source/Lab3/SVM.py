from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.datasets import load_digits
C = 1.0
#loading datasets with digits information
D=load_digits()
Info=D.data
tag=D.target
info_train, info_test, tag_train, tag_test=train_test_split(Info, tag, test_size=0.2)
#linear
design = svm.SVC(kernel='linear')
design.fit(info_train, tag_train)
#prediction for linear
tag_predlinear=design.predict(info_test)
#linear kernal with accuracy
L=str(metrics.accuracy_score(tag_test, tag_predlinear))
print("Required Accuracy for linear kernel of SVC " + L)
#RBF
design = svm.SVC(kernel='rbf')
design.fit(info_train, tag_train)
#predction function for rbf
tag_predrbf=design.predict(info_test)
#accuracy for rbf
R=str(metrics.accuracy_score(tag_test, tag_predrbf))
print("Required accuracy rbf kernel for SVC " + R)



