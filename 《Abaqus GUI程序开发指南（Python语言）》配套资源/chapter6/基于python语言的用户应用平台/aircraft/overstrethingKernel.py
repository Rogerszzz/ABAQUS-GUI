#! /user/bin/python
#-*-coding: UTF-8-*-
from abaqusConstants import *  
from caeModules import *       
from abaqus import *
import sys
def overstrethingkernel(modelName,materialName,partName,celllength,\
        cellwidth,thickness,panellength,panelwidth,panelheight):                                            
    print '该功能组件缺少内核执行文件，无法执行。'