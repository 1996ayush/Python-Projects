# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:34:47 2020

@author: khare
"""

f_t= "paris"
str1=" "
l=list(f_t)


if l[0]=="A" or  l[0]=="E" or l[0]=="I" or l[0]=="O" or l[0]=="U":
    l.append("way")

else:
    l.remove(f_t[0])
    l.append(f_t[0])
    l.append("ay")
    
print(str1.join(l))    
    
       