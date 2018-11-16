#!/usr/bin/env python
# coding: utf-8

# In[7]:


from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
import h5py
import matplotlib.pyplot as plt
from keras.preprocessing import image
import os


# In[8]:


datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')


# In[9]:


fnames = [os.path.join('/home/a/Downloads/cats_and_dogs_small/train/cats', fname) for
        fname in os.listdir('/home/a/Downloads/cats_and_dogs_small/train/cats')]


model = models.Sequential()
model.add(layers.Conv2D(32, (3,3),activation='relu',input_shape = (150,150,3)))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.MaxPool2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model. add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.summary()


# In[14]:


model.compile(loss='binary_crossentropy',optimizer=optimizers.RMSprop(lr=1e-4),metrics=['acc'])


# In[15]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range = 0.2,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,)
test_datagen = ImageDataGenerator(rescale=1./255)


# In[16]:


train_generator = train_datagen.flow_from_directory(
        '/home/a/Downloads/cats_and_dogs_small/train',
        target_size=(150,150),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        '/home/a/Downloads/cats_and_dogs_small/validation',
        target_size=(150,150),
        batch_size=32,
        class_mode='binary')


# In[18]:


hitory = model.fit_generator(
        train_generator,
        steps_per_epoch=50,
        epochs = 100,
        validation_data = validation_generator,
        validation_steps = 50)

model.save('cats_and_dogs_small.h5')
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




