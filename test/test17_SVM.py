from sklearn import svm

X = [[2, 0], [1, 0], [2, 3]]
y = [0, 0, 1]
classify = svm.SVC(kernel='linear')
classify.fit(X, y)

print(classify)

print(classify.support_vectors_)
print(classify.support_)
print(classify.n_support_)