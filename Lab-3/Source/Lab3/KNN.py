from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#Load dataset
ID=datasets.load_iris()
info=ID.data
tag=ID.target
#trained and test data
info_train, info_test, tag_train, tag_test=train_test_split(info, tag, test_size=0.2)
#KNN function
design= KNeighborsClassifier(n_neighbors=1)
design.fit(info_train, tag_train)
#predict function
y_predKNN=design.predict(info_test)
#Accuracy
print("Accuracy for the required KNN is : ", metrics.accuracy_score(tag_test, y_predKNN))
kn1_range1=range(1, 50)
ss1=[]
for q in kn1_range1:
    KNN1=KNeighborsClassifier(n_neighbors=q)
    KNN1.fit(info_train, tag_train)
    y_predKNN=KNN1.predict(info_test)
    ss1.append(metrics.accuracy_score(tag_test, y_predKNN))
#ploting in graph
plt.plot(kn1_range1, ss1)
plt.xlabel("K values")
plt.ylabel("Accuracy")
plt.show()

