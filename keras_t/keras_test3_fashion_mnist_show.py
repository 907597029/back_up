import keras
from keras.datasets import fashion_mnist#0到9的手写数字，在mnist中有60000张28*28的训练集手写数字 10000张测试集的数字 每个测试集x对应了一个结果y
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt

#数据预处理
(x_train,y_train),(x_test,y_test)= fashion_mnist.load_data()#训练集图片x 训练集结果y 测试集图片x 测试集结果y
print(x_train.shape,y_train.shape)#60000张训练集图片x_train 60000个训练集结果y
print(x_test.shape,y_test.shape)#10000张测试集图片x_train 10000个测试集结果y

#可视化数据集的结果 标签
# 每个培训和测试示例都分配给以下标签之一：
# 0 T恤/上衣
# 1裤子
# 套头衫
# 3连衣裙
# 4外套
# 5凉鞋
# 6件衬衫
# 7运动鞋
# 8袋
# 9踝靴
# im = plt.imshow(x_train[59999],cmap="gray")
y_name = {0:'T恤/上衣',1:'裤子',2:'套头衫',3:'连衣裙',4:'外套',5:'凉鞋',6:'件衬衫',7:'运动鞋',8:'袋',9:'踝靴'}
j=10000
for i in range(len(x_train)):
    im = plt.imshow(x_train[i+j])
    print('第{}'.format(i+j+1),'个是',y_name[y_train[i+j]])
    plt.show()

#
# # 因为优化目标函数SGD不能用二维数组 所以转换为一维的数组
# x_train = x_train.reshape(60000,28*28)
# x_test = x_test.reshape(10000,28*28)
#
# print(x_train.shape)
# #训练过程中数字太大 会出问题
# x_train = x_train/255
# x_test = x_test/255
#
# #独热编码 比如 把 y_train[5] 变成 [0,0,0,0,0,1,0,0,0,0] 这里第一个是手写的“0” train[0]的手写“5”其实是第六位
# y_train = keras.utils.to_categorical(y_train,10)
# y_test = keras.utils.to_categorical(y_test,10)
#
# #模型定义
# model = Sequential()#定义区块模型 ????
# model.add(Dense(512,activation="relu",input_shape=(784,)))#一次add就是加了一个全连接层 activation是激活函数
# model.add(Dense(256,activation="relu"))
# model.add(Dense(128,activation="relu"))
# model.add(Dense(64,activation="relu"))
# model.add(Dense(32,activation="relu"))
# model.add(Dense(16,activation="relu"))
# model.add(Dense(10,activation="softmax"))#让结果符合概率分布 就算两个相差特别大的数 在经过softmax后 都会变成相近的数
#
# model.summary()
#
# model.compile(optimizer=SGD(),loss="categorical_crossentropy",metrics=['accuracy'])#模型编译
# model.fit(x_train,y_train,batch_size=64,epochs=5,validation_data=(x_test,y_test))#模型的训练 训练集图片x 训练集输出y 每一次64个 epochs 训练周期5 validation data 验证数据
#
# #模型评价
# score = model.evaluate(x_test,y_test)
# print("LOSS:",score[0])
# print("ACCU:",score[1])#准确率