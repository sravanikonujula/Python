import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
# load dataset
irisDS= datasets.load_iris()
info = irisDS.data
tag = irisDS.target
info_train, info_test, tag_train, tag_test=train_test_split(info, tag, test_size=0.2, random_state=36)
#LDA
design = LinearDiscriminantAnalysis()
#fitting data
Q=design.fit(info_train, tag_train).transform(info)
targ_nams = irisDS.target_names
# predicting data
y_predLDA=design.predict(info_test)
# accuracy
A=metrics.accuracy_score(y_predLDA, tag_test)
print(" \n Required accuracy score is: ", A)

plt.figure()
colours = ['orange', 'pink', 'violet']
for colour, k, targ_nam in zip(colours, [0, 1, 2], targ_nams):
    plt.scatter(Q[tag == k, 0], Q[tag == k, 1], alpha=.8, color=colour,
                label=targ_nam)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA for the choosen IRIS dataset')
plt.show()
