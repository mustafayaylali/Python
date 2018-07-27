# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:04:32 2018

@author: ME99689
"""

# %%
class Calisan:
    
    zam_orani=1.8
    counter=0
    
    def __init__(self,isim,soyisim,maas): #constructor
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@hotmail.com"
        
        Calisan.counter=Calisan.counter+1
        
    def giveNameSurname(self):
        return (self.isim+" "+self.soyisim)
    
    def zam_yap(self):
        self.maas=self.maas+self.maas*self.zam_orani

        
#isci1=Calisan("Ali","Korkmaz",100)
#print(isci1.maas)
#print(isci1.giveNameSurname())


#class variable
calisan1=Calisan("Abdülkadir","Ömür",4100)
#print("Ilk maas:" , calisan1.maas)
#calisan1.zam_yap()
#print("Yeni maas:" , calisan1.maas)

calisan2=Calisan("Burak","Yilmaz",2200)
calisan3=Calisan("Gustova","Colman",1200)
calisan4=Calisan("Adrian","Mierjezevski",2500)

liste=[calisan1,calisan2,calisan3,calisan4]

max_maas=-1
index=-1

for each in liste:
    if(each.maas>max_maas):
        max_maas=each.maas
        index=each

print("En yüksek maas=",max_maas, "ve adı:",index.giveNameSurname())

#%%


