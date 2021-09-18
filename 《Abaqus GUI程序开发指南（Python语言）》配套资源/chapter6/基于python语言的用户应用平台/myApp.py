#-*-coding: UTF-8-*-
# -*- coding: mbcs -*-  
from abaqusGui import *
import sys
#从aircraft包中导入主窗口文件
from aircraft.caeMainWindow import CaeMainWindow
#初始化应用对象
app = AFXApp('My Application', 'FAI03', '用户自定义应用平台', 2012, 1, 1)
app.init(sys.argv)
#构建主窗口
# 
CaeMainWindow(app)
#创建应用程序
#
app.create()
#启动应用程序
#
app.run() 