import keras
from keras.datasets import mnist#0到9的手写数字，在mnist中有60000张28*28的训练集手写数字 10000张测试集的数字 每个测试集x对应了一个结果y
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
from datetime import datetime

#数据预处理
(x_train,y_train),(x_test,y_test)= mnist.load_data()#训练集图片x 训练集结果y 测试集图片x 测试集结果y
print(x_train.shape,y_train.shape)#60000张训练集图片x_train 60000个训练集结果y
print(x_test.shape,y_test.shape)#10000张测试集图片x_train 10000个测试集结果y

#可视化数据集的结果 灰度图
image = plt.imshow(x_train[0],cmap="gray")
plt.show()

# 因为多层感知机不能用二维数组 所以转换为一维的数组
x_train = x_train.reshape(60000,28*28)
x_test = x_test.reshape(10000,28*28)

print(x_train.shape)
print(x_train)
#训练过程中数字太大 对每一个权重值有变化 缩小到0-1 可以缩小脏数据的影响
x_train = x_train/255
x_test = x_test/255

#独热编码 比如 把 y_train[5] 变成 [0,0,0,0,0,1,0,0,0,0] 这里第一个是手写的“0” train[0]的手写“5”其实是第六位
y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)

t1 = datetime.now()
#模型定义
model = Sequential()#定义序贯模型
model.add(Dense(512,activation="relu",input_shape=(784,)))#一次add就是加了一个全连接层 activation是激活函数
model.add(Dense(256,activation="relu"))
model.add(Dense(128,activation="relu"))
model.add(Dense(64,activation="relu"))
model.add(Dense(32,activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dense(10,activation="softmax"))#让结果符合概率分布 让结果放缩到 0-1 就算两个相差特别大的数 在经过softmax后 都会变成相近的数

model.summary()

model.compile(optimizer=SGD(),loss="categorical_crossentropy",metrics=['accuracy'])#模型编译 optimizer优化器 loss损失函数 metrics准确值
model.fit(x_train,y_train,batch_size=64,epochs=5,validation_data=(x_test,y_test))#模型的训练 训练集图片x 训练集输出y 每一次64个 epochs 训练周期5 validation data 验证数据

t2 = datetime.now()
time = t2 - t1
#模型评价
score = model.evaluate(x_test,y_test)
print("LOSS:",score[0])
print("ACCU:",score[1])#准确率

print("---------time----------:{}s",format(time.seconds))