#! /user/bin/python
# -*- coding:UTF-8 -*-
f=file('num.py','w')           #�ڹ���Ŀ¼�´���һ����Ϊnum.py���ļ�               
f.write("x=%6i\n" % 100)     #���ַ���д���ļ�num.py
f.write("y=99\n")             #���ַ���д���ļ�num.py
for i in range(1,101):
    f.write('%i\t' % i)
    if i%10==0:
        f.write('\n')
f.close()