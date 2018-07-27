# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:40:48 2018

@author: ME99689
"""

#%% syntax error

print(9)

#print 9

int(10.0)
#int 10.0

i=0
while(i<10):
    print(i)
    i=i+1
    
#%% exceptions
a=10
b="2"

liste=[1,2,3]
print(sum(liste))
print(a+int(b))

k=13
zero=0
print(k)

#a=k/zero #error

if(zero==0):
    a=0
else:
    a=k/zero


try:
    a=k/zero
except ZeroDivisionError:
    a=99
    
print(a)














