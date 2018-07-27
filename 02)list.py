# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:33:54 2018

@author: ME99689
"""

#%% List

liste=[1,2,3,4,5,6]

liste_str=["pts","sali","crs"]

value=liste[1]
print(value)

print(liste[-1]) #sonuncu deger

print(liste[0:3]) #0'dan 3'e kadar 0,1,2

liste.append(7)
liste.remove(7)
liste.reverse()

liste2=[1,5,3,2,6]
liste2.sort()  #sıralar

karisik=[1,"aa",2,"bb",3]

#%%tuple

t=(1,2,3,4,5,6)

t.count(3) #3 ten kaç tane var onu sayar
t.index(3)


#%% dictionary

dictionary={"ali":32,"veli":45,"ayse":13}

#ali,veli,ayse =keys
#32,45,13 =value

def deneme():
    dictionary={"ali":32,"veli":45,"ayse":13}
    return dictionary

dic=deneme()

# %% conditionals

#if else statement

var1=16
var2=15

if(var1>var2):
    print("var1 buyuktur var2")
elif(var1==var2):
    print("sayilar esit")
else:
    print("var1 kucuktur var2")

#liste araması IF ile
liste=[1,2,3,4,5]

value=10
if value in liste:
    print("evet {} degeri listede".format(value))
else:
    print("hayir {} listede yok".format(value))


#dictionaryı IF
keys=dictionary.keys()
if "ali" in keys:
    print("evet")
else:
    print("hayir")

# %%

# 1630.yıl = 17.yuzyil
# 109.yil =2.yy
#2000.yil =20.yy
    
#metod olacak
    #input integer yillar
    #output yy

#input=year >> 1 <=year <=2005
    
def yyHesapla(yil):
    """
    year to century
    """
    str_year=str(yil)
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #100,200,300.. 900 gibi
            return int(str_year[0])
        else:                   #123,190,257
            return int(str_year[0])+1
    else:
        if(str_year[2:4]=="00"): #1000,2000,3000.. 9000 gibi
            return int(str_year[:2])
        else:                   #123,190,257
            return int(str_year[:2])+1
        
# %% LOOPS
            
#for loop
            
for each in range(1,11):
    print(each)

for each in "ankara ist":
    print(each)
    
for each in "ankara ist".split(): #kelimeleri bosluklara göre ayır
    print(each)
        
liste=[1,5,7,12,6,99,43]

toplamListe= sum(liste)
#veya
count=0
for each in liste:
    count=count+each
        
# %% While Loop
    
i=0
while(i<4):
    print(i)
    i=i+1
    
    
sinir=len(liste)
each=0
count=0
while(each<sinir):
    count=count+liste[each]
    each=each+1

#%% listenin içindeki en küçük sayıyı bulma
    
liste=[12,55,11,89,30,66,87,45]
enKucuk=liste[0]

for sayi in liste:
    if(sayi<enKucuk):
        enKucuk=sayi
    else:
        continue
    
print("En küçük sayi:",enKucuk)
















   
    