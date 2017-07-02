#!/usr/bin/env python

import pandas as pd
import numpy as np

import tensorflow as tf
import keras
from keras.models import Model, Sequential
from keras.layers import *
from keras.optimizers import Adam

print(keras.__version__)
#version 2.0.5
print(tf.__version__)
#version 1.2.1

inputCSV = "/Data/common/survival_1.csv"

df = pd.read_csv(inputCSV)

df.admission_type = pd.Categorical(df.admission_type)
df['admission_type'] = df.admission_type.cat.codes
df.gender = pd.Categorical(df.gender)
df['gender'] = df.gender.cat.codes
df.ethnicity= pd.Categorical(df.ethnicity)
df['ethnicity'] = df.ethnicity.cat.codes

{x: df[x].dtype for x in df}

chosenColumns = ['age','admission_type','hospstay_seq','icustay_seq',
'oasis_prob', 'oasis', 'apsiii_prob','apsiii', 'height','gender','ethnicity',
'hours_vent','chosen','pbw', 'mean_tv_observed', 'tv_pbw_mean',
'los_hospital', 'los_icu',"pao2fio2_max", "pao2fio2_mean", "pao2fio2_sd",
'peep_max', 'peep_mean', 'peep_sd',
'diabetes_uncomplicated', 'diabetes_complicated', 'hypothyroidism',
'renal_failure', 'liver_disease', 'peptic_ulcer', 'aids', 'lymphoma',
'metastatic_cancer', 'solid_tumor', 'rheumatoid_arthritis',
'coagulopathy', 'obesity', 'weight_loss', 'fluid_electrolyte',
'blood_loss_anemia', 'deficiency_anemias', 'alcohol_abuse',
'drug_abuse', 'psychoses', 'depression', 'pulmonary_circulation',
'peripheral_vascular', 'hypertension', 'paralysis', 'other_neurological',
'chronic_pulmonary', 'congestive_heart_failure', 'cardiac_arrhythmias',
'valvular_disease']

df2 = df[ chosenColumns ]
y = df['h_mort']
X = df2.as_matrix()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y.values, test_size=0.2, random_state=42)



if re_weight:
    weight_val *= 0.472001959
    weight_val[labels_val==0] = 1.309028344
# x_train = x_train.reshape(60000, 784)
# x_test = x_test.reshape(10000, 784)
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train /= 255
# x_test /= 255
# print(x_train.shape, 'train samples')
# print(x_test.shape, 'test samples')

y_train = keras.utils.to_categorical(y_train, n_classes)
y_test = keras.utils.to_categorical(y_test, n_classes)

#Params
lr          = 0.001
epochs      = 2
n_classes   = 2
batch_size = 10
n_input=df2.shape[1]
re_weight = True 


# Lens Architecture

# INPUT
Inp = Input(shape=(n_input,))
# MIDDLE
x = Dense(100, activation='relu', name = "Dense_1")(Inp)
x = Dropout(0.8)(x)
# x = Dense(100, activation='relu', name = "Dense_2")(x)
# x = Dropout(0.8)(x)
# OUTPUTLAYER
output = Dense(n_classes, activation='softmax', name = "Outputlayer")(x)
# MODEL
model = Model(Inp, output)

model.summary()
model.compile(loss='categorical_crossentropy',
              optimizer='SGD',
              metrics=['accuracy'])

history = model.fit(X_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,class_weight = {0: 0.7357466, 1: 0.2642534},
                    validation_data=(X_test, y_test))

--
Train on 884 samples, validate on 221 samples
Epoch 1/2
884/884 [==============================] - 0s - loss: nan - acc: 0.7410 - val_loss: nan - val_acc: 0.7149
Epoch 2/2
884/884 [==============================] - 0s - loss: nan - acc: 0.7410 - val_loss: nan - val_acc: 0.7149

