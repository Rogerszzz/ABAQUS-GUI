#-*-coding: UTF-8-*-
# -*- coding: mbcs -*-  
from abaqusGui import *
import sys
#��aircraft���е����������ļ�
from aircraft.caeMainWindow import CaeMainWindow
#��ʼ��Ӧ�ö���
app = AFXApp('My Application', 'FAI03', '�û��Զ���Ӧ��ƽ̨', 2012, 1, 1)
app.init(sys.argv)
#����������
# 
CaeMainWindow(app)
#����Ӧ�ó���
#
app.create()
#����Ӧ�ó���
#
app.run() 