from sklearn import svm
X = [[0, 0], [1, 2]]
y = [0, 2]
z= [0,3]
clf = svm.SVC()
clf.fit(X,y)
clf.fit(X,z)
print(clf.predict([[3., 3.]]))