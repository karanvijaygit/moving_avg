#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:54:19 2019

@author: karan
"""
# Moving Average
import numpy as np
moving_average = []
input = np.array([3,5,7,2,8,10,11,65,72,81,99,100,150])
window = 3
for index,value in enumerate(input):
    bunch = np.array([input[index],input[index+1],input[index+2]])
    bunch_avg = np.mean(bunch)
    moving_average.append(bunch_avg)
    if index > (len(input) - window - 1):
        break
print(moving_average)
    
