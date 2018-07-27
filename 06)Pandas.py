# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:32:55 2018

@author: ME99689
"""

# 1) pandas hizli ve etkili for dataframes
# 2) csv and text file açıp inceleyip sonucları rahat şekilde kaydedilir.
# 3) NaN yani Miss datalar için işimizi kolaylaştırıyor
# 4) reshape yapıp datayı daha etkili şekilde kullanabiliriz.
# 5) slicing indexing kolay
# 6) time series data analizinde çok yardımcı
# 7) *** HIZLI **

# %%
import pandas as pd

dictionary= {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
            "AGE":[15,16,17,33,45,66],
            "MAAS":[100,150,240,350,110,200]
            }

dataFrame1=pd.DataFrame(dictionary)

head=dataFrame1.head()  #baştan 5 satır verir, (ön inceleme için kullanılr)
tail=dataFrame1.tail()  #sondan 5

ilk3=dataFrame1.head(3)


#%%
#pandas basic method

print(dataFrame1.columns)
print(dataFrame1.info())

print(dataFrame1.dtypes)
print(dataFrame1.describe()) #numeric feature = columns(age,maas)


#%% indexing and slicing

print(dataFrame1["NAME"])
print(dataFrame1["AGE"])

print(dataFrame1.AGE)

dataFrame1["new_fauture"]=[-1,-2,-3,-4,-5,-6]


print(dataFrame1.loc[:,"AGE"])

print(dataFrame1.loc[:3,"AGE":"NAME"])

print(dataFrame1.loc[:3,["AGE","NAME"]])

print(dataFrame1.loc[::-1,:])

print(dataFrame1.loc[:,:"NAME"])

print(dataFrame1.iloc[:,2])  # iloc ile index sliding yapılabilir.

#%% filtering

filtre1=dataFrame1.MAAS>=200

filtrelenmis_data=dataFrame1[filtre1]

filtre2=dataFrame1.AGE<20

dataFrame1[filtre1 & filtre2]

print(dataFrame1[dataFrame1.AGE>60])


#%%  List Comprehension

import numpy as np


avg_maas=dataFrame1.maas.mean()             #pandas ile

ortalama_maas_np=np.mean(dataFrame1.maas)  #numpy ile


dataFrame1["maas_seviyesi"]=["yuksek" if avg_maas> each else "dusuk" for each in dataFrame1.maas]

#
#for each in dataFrame1.MAAS:
#    if(ortalama_maas>each):
#        print("yuksek")
#    else:
#        print("dusuk")


dataFrame1.columns=[each.lower() for each in dataFrame1.columns]

#eğer column name arasında boşluk varsa yeniden adlanır _ koy
dataFrame1.columns=[each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]

#%% drop and concatenating

dataFrame1.drop(["yeni_fauture"],axis=1,inplace=True)


data1=dataFrame1.head() 
data2=dataFrame1.tail()

#vertical
data_concat=pd.concat([data1,data2],axis=0)

#horizontal
maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat=pd.concat([maas,age],axis=1) #yanyana birleştirme

 # %% transforming data
 
 #yasın iki katını yeni sutuna yaz
 dataFrame1["list_comp"]=[ each*2 for each in dataFrame1.age]


#apply()
 def multiply(age):
     return age*2
 
dataFrame1["apply_metodu"]=dataFrame1.age.apply(multiply)
















