#! /user/bin/python
# -*- coding:UTF-8 -*-
f1=file('num.py','r')
f2=file('new_num.txt','w')        
str1=f1.read(9)
str2=f1.read(5)
f2.write('this is a new file.\n')
f2.write(str1)  
f2.write(str2)

while True:
    line=f1.readline()
    if len(line)==0:
        break
    data=line.strip().split('\t')
    N=len(data)
    for i in range(0,N):
       f2.write(data[i]+',')
    f2.write('\n')
f1.close()
f2.close()
            
