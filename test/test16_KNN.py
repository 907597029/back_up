from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()#knn

iris = datasets.load_iris()   #花的数据集

print(iris)

knn.fit(iris.data, iris.target) #data里面包含了特征 花瓣的个数 花瓣的长度 颜色 之类的 taget里面得是 0 1 2 三种花的名称

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])

print(predictedLabel)