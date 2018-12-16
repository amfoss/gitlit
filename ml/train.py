import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn import metrics

import sys
import joblib

labels=[]
features=[]
file=open('data.csv').read()
list=file.split('\r\n')
data=np.array(list)
data1=[i.split(',') for i in data]
data1=data1[0:-1]
for i in data1:
	labels.append(i[5])
data1=np.array(data1)
features=data1[:,:-1]
features=features[:,[0,1,2,3,4]]

#print features

features=np.array(features).astype(np.float)

##### HAS TO BE CHANGED TO ALL ENTRIES OF THE DATASET

features_train=features
labels_train=labels

# features_test=features[10000:]
# labels_test=labels[10000:]



print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier(min_samples_split=7, verbose=True)
clf4.fit(features_train, labels_train)
importances = clf4.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf4.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking

print("Feature ranking:")
for f in range(features_train.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))


# pred4=clf4.predict(features_test)
# print(classification_report(labels_test, pred4))
# print 'The accuracy is:', accuracy_score(labels_test, pred4)
# print metrics.confusion_matrix(labels_test, pred4)

#sys.setrecursionlimit(9999999)

joblib.dump(clf4, 'classifier/model.pkl', compress=9)
print("dump done")