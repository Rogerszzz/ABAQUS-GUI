# -*- coding: mbcs -*-  
# -* - coding:UTF-8 -*- 
##################################################################################
# Created by jly4553 on Tue Mar 11 08:20:31 2012 

##################################################################################
from abaqus import *
from abaqusConstants import * 
from caeModules import *
from driverUtils import executeOnCaeStartup
def CtestKernel(gthick,pthick,eletype,layuptable,yesnocohesive,modelName1,materialName,modelName2,partName,CSYSKW):
    print '该功能组件缺少内核执行文件，无法执行。'
