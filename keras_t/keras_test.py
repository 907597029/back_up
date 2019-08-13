import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.datasets import fashion_mnist
import sklearn

(x_train,y_train),(x_test,y_test)= fashion_mnist.load_data()#训练集图片x 训练集结果y 测试集图片x 测试集结果y