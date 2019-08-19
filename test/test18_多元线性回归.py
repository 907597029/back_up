from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

#x总里程 躺数 独热编码012车     y 总小时
dataPath = r"MultipleRerDummyDemo.csv"
deliveryData = genfromtxt(dataPath, delimiter=',')

print("data",deliveryData)

X = deliveryData[:, :-1]
Y = deliveryData[:, -1]

regr = linear_model.LinearRegression()

regr.fit(X, Y)

print("coefficients")
print(regr.coef_)
print("intercept")
print(regr.intercept_)