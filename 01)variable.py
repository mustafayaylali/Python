# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:57:34 2018

@author: ME99689
"""

#variable , function , object

# %%
var1=10
var2=15

gun= "pazartesi"

var3= 10.0

# %%   Run = shift+enter

s="bugun sali"

variable_type=type(s)

print("Ekran ciktisi= " + s)

var1="ankara"
var2="istanbul"
var3=var1+var2
print(var3);

var4="100"
var5="200"
var6=var4+var5
print(var6);

uzunluk=len(var6)

# %%   NUMBERS

integer_deneme=-50
float_deneme= -30.7

# %% built in functions

str1="deneme"

# float(10)  int(10.5) round(8.3)

str2="1005"   #int(str2)   string to int

type(int(str2)) 

# %%  user defined functions

var1=20
var2=50

def my_function(a,b):
    """ 
    first function
        
    parametre:
        
    return:
    """
    output= (((a+b)*50)/100.0)* a/b
    
    return output


sonuc=my_function(var1,var2)



def deneme1():
    print("second trial")

#%% default ve flexible funtions
    
def cember_cevre(r,pi=3.14):
    """
    cember cevre hesapla
    input(parametre):r,pi
    output=cemberin cevresi
    """
    output=2*pi*r
    return output

#flexible
    
def hesapla(boy,kilo,*args):
    print(len(args)) #print(args)
    output=boy+kilo
    return output
#
#def hesapla(boy,kilo,yas):
#    output=(boy+kilo)*yas
#    return output

# %%
    
age=23
name="Mustafa"
surname="Yaylali"

def tipDondur(age,name,*args,ayak_no=42):
    print("Name :",name, "Age :",age, "Ayak No:",ayak_no)
    print(type(age))
    print(float(age))
    
    output=args[0]*4
    
    return output
    
    
sonuc=tipDondur(age,name,surname)
print("args[0]*yas : ",sonuc)

# %%   lambda function

def hesapla(x):
    return x*x

sonuc=hesapla(3)

#tek satır function
sonuc2=lambda x: x*x
print(sonuc2(3))

#%%














