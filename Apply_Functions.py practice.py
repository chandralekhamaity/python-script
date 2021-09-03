# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:30:39 2021

@author: CHANDRALEKHA
"""

import pandas as pd

def adder(adder1,adder2):return adder1+adder2

d = {'Score_English':pd.Series([65,22,78,98,90,56,45,65,34,12,56,88]),
       'Score_SST':pd.Series([45,36,78,90,33,22,99,70,66,55,89,96])}

print(type(d))
print(d)
df = pd.DataFrame(d)
print(df)
print(df.pipe(adder,2))

import numpy as np

d = {'Score_Hindi':pd.Series([56,67,89,78,99,55,34,23,20,33,90,88]),
       'Score_Maths':pd.Series([45,67,87,98,90,66,33,22,56,78,12,22])}

df = pd.DataFrame(d)
print(df)
print(df.apply(np.mean,axis=1))
print(df.apply(np.mean,axis=0))

d = {'Score_English':pd.Series([65,22,78,98,90,56,45,65,34,12,56,88]),
       'Score_SST':pd.Series([45,36,78,90,33,22,99,70,66,55,89,96])}

df = pd.DataFrame(d)
print (df)

print (df.applymap(lambda x:x*2))

import math as m

print (df.applymap(lambda x:m.sqrt(x)))
