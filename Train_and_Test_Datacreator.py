# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:42:31 2021

@author: 91961
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
import shutil

SourceDataDirectories = ["D:\\vegData"]
DestTrainDataDirectories=["D:\\vegDataset\\training\\training-1","D:\\vegDataset\\training\\training-2","D:\\vegDataset\\training\\training-3","D:\\vegDataset\\training\\training-4"]
DestTestDataDirectories=["D:\\vegDataset\\testing\\testing-1","D:\\vegDataset\\testing\\testing-2","D:\\vegDataset\\testing\\testing-3","D:\\vegDataset\\testing\\testing-4"]
CATEGORIES = ["BeetRoot","BellPepper","BitterGourd","BottleGourd","Brinjal","Cabbage","Carrot","CauliFlower","Chilli","Cucumber","FlatBeans","Garlic","GermanTurnip","Ginger","GourdLuffaSponge","GreenBeans","LadyFinger","Lemon","Onion","Papaya","Pea","PointedGourd","Potato","Pumpkin","Radish","RidgeGourd","SnakeBeans","TaroRoot","Tomato"]
#Checking total number of categories
print(len(CATEGORIES))



def trainImageGenerator():
    count=0
    training_images_index=[]
    training_images=[]
    testing_images=[]
    for directories in DestTrainDataDirectories: # getting the directories one by one
        for category in CATEGORIES:  # getting the categories one by one 
            path = os.path.join("D:\\vegData",category)  # create path to the categories
            totalImages=len(os.listdir(path))
            noOfTrainImages=round(0.7*totalImages)
            while count!=noOfTrainImages:
                rNo=random.randint(1,totalImages)
                if rNo not in training_images_index:
                    training_images_index.append(rNo)
                    training_images.append(str(rNo)+'.jpg')
                    count=count+1
            count=0
            for img in training_images:  
                try:
                    srcPath=os.path.join(path,img)
                    dstPath=os.path.join(os.path.join(directories,category),img)
                    shutil.copy(srcPath,dstPath)
                except Exception as e:  # in the interest in keeping the output clean...
                    pass
            noOfTestImages=round(0.3*totalImages)
            while count!=noOfTestImages:
                rNo=random.randint(1,totalImages)
                if rNo not in training_images_index:
                    training_images_index.append(rNo)
                    testing_images.append(str(rNo)+'.jpg')
                    count=count+1
            count=0
            for img in testing_images:  
                try:
                    srcPath=os.path.join(path,img)
                    dstPath=os.path.join(os.path.join(DestTestDataDirectories[index],category),img)
                    shutil.copy(srcPath,dstPath)
                except Exception as e:  # in the interest in keeping the output clean...
                    pass
            training_images_index=[]
            training_images=[]
            testing_images=[]

            
                
trainImageGenerator()