# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:14:12 2019

@author: hsieh
"""
import numpy as np
import pandas as pd
k=list('ABCDEFGHIJK')
v=[[np.random.randint(-10,10) for x in range(10)] for i in range(10)]
df=pd.DataFrame(dict(zip(k,v))) 
print(df,end='\n\n')
'''
df1=df[(df.A >0) & (df.C > 0) ] [[x for x in df.columns if x not in list('A')]];print(df1)
df2=df[::-1][list(df.columns)];print(df2)
df3=df[1::3][sorted(list(set(df.columns)-set(list('BEF'))))];print(df3,'\n')
df4=df[1::3][['B','E']];print(df4,'\n')
# 唯一錯誤 不能使用切片 df5=df[1::3][['A'::1]];print(df5,'\n')
'''

## loc 可以 布林,列舉,排除,等差數列 幾乎所有運算都可以
'''
df1=df.loc[(df.A >0) & (df.C >0),'B'::] ;print(df1,'\n')
df2=df.loc[::-1, ['B','D']];print(df2,'\n')
df3=df.loc[1:3, [x for x in list(df.columns) if x not in list('EFJ')]];print(df3,'\n')
df4=df.loc[1:3, list('ABEFJC')];print(df4,'\n')
'''
df5=df.loc[1::3,sorted(list(set(df.columns)-set(list('ABCD'))))];print(df5)

