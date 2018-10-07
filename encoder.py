# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:25:05 2018

@author: Abhishek
"""

import os
import face_recognition
import pickle

#this file creates two files: encodings, names and saves them as pickles

# Load a sample picture and learn how to recognize it.

ans = {}

for name in os.listdir('myData'):
    image = face_recognition.load_image_file('myData/' + name)
    en = face_recognition.face_encodings(image)
    ans[name[:-4]] = en
    print(name)

with open('name_encoding_dict.pickle', 'wb') as f:
    pickle.dump(ans, f)

print('done')

######------------forgot make a dict. should change the lists to dict