from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#print('train_img:', train_images.shape)
#print('train_lab_len:', len(train_labels))
#print('train_lab:', train_labels)

#print('test_images:', test_images.shape)
#print('test_labels:', test_labels)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28, )))
network.add(layers.Dropout(0.2))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

network.fit(train_images, train_labels, epochs=5, batch_size=500)

test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc:', test_acc)
print('loss:', test_loss)