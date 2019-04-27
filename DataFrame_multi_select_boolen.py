# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:45:13 2019

@author: hsieh
"""
import numpy as np
import pandas as pd
l=[[x+i for x in range(6)] for i in range(5)]
df=pd.DataFrame(l)
df.index=list(range(1,6,1))
df.columns=list('ABCDEF')
print()
l=df; print(l) ;print()
l=df.loc[(df.A <3) & ( df.D > 3)  ,:: ]; print(l) ;print()
l=df.loc[(df.A <3) & ( df.D > 3)  ,::2]; print(l);print()
l=df.loc[(df.A <3) & ( df.D > 3)  ,::3]; print(l);print()

    
