# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:45:13 2019

@author: hsieh
"""
import numpy as np
import pandas as pd

k=list('ABCDE')
v=[[np.random.randint(-5,5) for x in range(5)] for i in range(5)]
df=pd.DataFrame(dict(zip(k,v))) 
df=df.replace(0,np.nan)
print(df);print()
print(df.isnull().stack()[lambda df:df==True]);print()
print(list(df.isnull().stack()[lambda df:df==True].index))





#print(df)


    
