#!/usr/bin/python
#-*-coding: UTF-8-*-
#-*-coding: mbcs -*- 
from abaqusGui import *
from abaqusConstants import *
from toolset2.impact.impactForm import impactForm
#导入功能组件
import os
import win32com
from win32com.client import Dispatch, constants
########################################################################
# Class definition
########################################################################

class AircraftToolsetModule2(AFXToolsetGui):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    [ID_IMPACT] =range(AFXToolsetGui.ID_LAST, AFXToolsetGui.ID_LAST +1)
    def __init__(self):

        AFXToolsetGui.__init__(self, '飞机复合材料结构分析')
        #初始化工具包

        FXMAPFUNC(self, SEL_COMMAND, self.ID_IMPACT, 
            AircraftToolsetModule2.onCmdIMPACT)  
        self.IMPACT = impactForm(self) 
        #增关联复合材料冲击损伤参数化建模功能  
        #
        group = AFXToolbarGroup(self,'composite tools','复合材料结构建模工具')
        icon = afxCreatePNGIcon(r"icon\airtransport.png")
        FXLabel(p=group, text='', ic=icon)
        #创建新的工具条    
        AFXToolButton(p=group, label="\t复合材料冲击损伤参数化建模程序",
            icon = afxCreatePNGIcon(r"icon\impact_icon.PNG"), 
            tgt=impactForm(self), sel=AFXMode.ID_ACTIVATE)
        #工具条中增加复合材料冲击损伤自动建模程序功能按键   
    def getKernelInitializationCommand(self):
        return 'import toolset2.impact.impactKernel'
        #定义内核初始命令
    #
    #定义功能组件触发后的执行函数    
    def onCmdIMPACT(self, sender, sel, ptr):

        impactForm.activate(self.IMPACT)
        #激活功能组件
        return 1