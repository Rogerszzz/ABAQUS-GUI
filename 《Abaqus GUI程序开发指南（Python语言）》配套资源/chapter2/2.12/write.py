#! /user/bin/python
# -*- coding:UTF-8 -*-
f=file('num.py','w')           #在工作目录下创建一个名为num.py的文件               
f.write("x=%6i\n" % 100)     #将字符串写入文件num.py
f.write("y=99\n")             #将字符串写入文件num.py
for i in range(1,101):
    f.write('%i\t' % i)
    if i%10==0:
        f.write('\n')
f.close()