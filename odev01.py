# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:10:58 2016

@author: Ottoman
"""

#import random
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()

s1 = np.random.uniform(0.5,1.5)
m1 = np.random.uniform(-5,5)
s2 = np.random.uniform(0.5,1.5)
m2 = np.random.uniform(-5,5)

d1 = m1 + s1 * np.random.randn(10000)
d2 = m2 + s2 *np.random.randn(10000)

a1 = np.rint(d1)
a2 = np.rint(d2)



y1,x1, patches1 = plt.hist(a1,40,range=(-20,20), normed = True)
y2,x2, patches2 = plt.hist(a2,40,range=(-20,20), normed = True)

#y1=[x for x in array1]
#y2=[x for x in array2]


plt.show()

wd = 0
for i in range(0,len(y1)):
    if y1[i]!=0:
        y1[i]= y1[i]+1
       
    for i in range(0,len(y2)):
        if y2[i]!=0:
            y2[i]=y2[i]+1
           
for j in range(0,len(y1)):
    if y1[j]!=0:
        for g in range(0,len(y2)):
            if y2[g]!=0:
                wd += abs(j-g)*abs(y1[j]-y2[g])
                if(y1[j]>y2[g]):
                    g+=1
                if(y1[j]<y2[g]):
                    j+=1  
            
#i=0            
#while(i!=j):
 #       if(dizi2[i]!=0):
  #          while(u!=g):
   #             while(dizi4[u]!=0):
    #                wd += abs(u-i)*abs(dizi2[i]-dizi4[u])
     #           u+=1
      #          if(dizi2[i]==0):
       #             i+=1
        #i+=1
