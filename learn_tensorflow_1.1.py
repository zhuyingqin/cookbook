import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers
print(tf.__version__)           # 输出版本号

# 训练参数与测试参数分开
(x_train, y_train), (x_test, y_test) = keras.datasets.boston_housing.load_data()
print(x_train.shape, ' ', y_train.shape)
print(x_test.shape, ' ', y_test.shape)

# 构建模型
model = keras.Sequential([
    layers.Dense(32, activation='sigmoid', input_shape=(13,)),
    layers.Dense(32, activation='sigmoid'),
    layers.Dense(32, activation='sigmoid'),
    layers.Dense(1)
])

# 配置模型
model.compile(optimizer=keras.optimizers.SGD(0.1),
             loss='mean_squared_error',  # keras.losses.mean_squared_error
             metrics=['mse'])
model.summary()

# 训练
model.fit(x_train, y_train, batch_size=50, epochs=50, validation_split=0.1, verbose=1)

result = model.evaluate(x_test, y_test)
print(model.metrics_names)
print(result)
