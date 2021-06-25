import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
df = pd.read_csv('F:\\Riss 2021\\AGGRO\\static\\cpdata.csv')
X = df.drop('label', axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

def random_forest(t1,t2,t3,t4):
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    lst=[[t1,t2,t3,t4]]
    lst=np.array(lst)
    lst.reshape(-1,1)

    rfc_predict = rfc.predict(lst)
    print(rfc_predict)
    ab = rfc.score(X_test, y_test)
    return str(rfc_predict[0]),ab
#     ls=pd.DataFrame(lst)

def mysvm(t1,t2,t3,t4):
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    lst = [[t1, t2, t3, t4]]
    lst = np.array(lst)
    lst.reshape(-1, 1)
    presult = svclassifier.predict(lst)
    ab = svclassifier.score(X_test, y_test)
    return presult[0],ab

def naive_bayes(t1,t2,t3,t4):
    classifier = GaussianNB()
    print("kui")
    classifier.fit(X_train,y_train)
    lst = [[t1, t2, t3, t4]]
    lst = np.array(lst)
    lst.reshape(-1, 1)
    presult = classifier.predict(lst)
    ab = classifier.score(X_test, y_test)
    return presult[0],ab

def nn_cnn(t1,t2,t3,t4):
    # clf = MLPClassifier(solver='lbfgs',
    #                     alpha=1e-5,
    #                     hidden_layer_sizes=(6,),
    #                     random_state=1)
    clf = MLPClassifier(random_state = 1, max_iter = 300)
    clf.fit(X_train, y_train)
    lst = [[t1, t2, t3, t4]]
    lst = np.array(lst)
    lst.reshape(-1, 1)
    presult = clf.predict(lst)
    ab=clf.score(X_test, y_test)
    print(ab)
    return presult[0],ab