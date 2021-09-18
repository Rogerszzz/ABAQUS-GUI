#!/usr/bin/python
#-*-coding: UTF-8-*-
#-*-coding: mbcs -*- 
from abaqusGui import *
from abaqusConstants import *
from aircraft.CtestForm import CtestForm
from aircraft.honeycombForm import honeycombForm
from aircraft.overstrethingForm import overstrethingForm
from aircraft.materialcheck.materialcheck_plugin import materialcheck_plugin 
from toolset2.impact.impactForm import impactForm
#导入各功能组件
import os
import win32com
from win32com import client
from win32com.client import Dispatch, constants
########################################################################
# Class definition
########################################################################

class AircraftToolsetModule(AFXToolsetGui):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    [ID_HELP,ID_Ctest,ID_HONEYCOMB,ID_OVERSTRETHING,ID_FINDMATERIALS] =\
        range(AFXToolsetGui.ID_LAST, AFXToolsetGui.ID_LAST +5)
    #为各功能组件分配ID
    def __init__(self):

        AFXToolsetGui.__init__(self, '复材工具条')
        #初始化工具包
        FXMAPFUNC(self, SEL_COMMAND, self.ID_Ctest, 
            AircraftToolsetModule.onCmdCtest)  
        self.Ctest = CtestForm(self)
        #关联功能组件一
        FXMAPFUNC(self, SEL_COMMAND, self.ID_HONEYCOMB, 
            AircraftToolsetModule.onCmdHONEYCOMB)  
        self.HONEYCOMB = honeycombForm(self)
        #关联功能组件二
        FXMAPFUNC(self, SEL_COMMAND, self.ID_OVERSTRETHING, 
            AircraftToolsetModule.onCmdOVERSTRETHING)  
        self.OVERSTRETHING = overstrethingForm(self)
        #关联功能组件三
        FXMAPFUNC(self, SEL_COMMAND, self.ID_HELP, 
            AircraftToolsetModule.onCmdHelp)
        #关联功能组件四：帮助文档功能
        FXMAPFUNC(self, SEL_COMMAND, self.ID_FINDMATERIALS, 
             AircraftToolsetModule.onCmdFindMaterials)
        self.FINDMATERIALS=materialcheck_plugin(self)               
        #关联功能组件五：材料力学性能查询
        #
        #***************************************************************
        group = AFXToolbarGroup(self,'结构设计分析工具','结构设计分析工具')
        #创建工具条并命名为'结构设计分析工具'
        icon = afxCreatePNGIcon(r"icon\air.PNG")
        #定义图标
        FXLabel(p=group, text='', ic=icon)
        #在工具条中添加标签
        #
        AFXToolButton(p=group, label="\t复合材料典型试验件快速建模程序", 
            icon = afxCreatePNGIcon(r"icon\Ctest.PNG"), 
            tgt=CtestForm(self), sel=AFXMode.ID_ACTIVATE)
        #增加功能组件一功能键
        AFXToolButton(p=group, label="\t六边形蜂窝参数化建模程序", 
            icon = afxCreatePNGIcon(r"icon\honeycomb_icon.PNG"), 
            tgt=honeycombForm(self), sel=AFXMode.ID_ACTIVATE)
        #增加功能组件二功能键       
        AFXToolButton(p=group, label="\t过拉伸蜂窝参数化建模程序", 
            icon = afxCreatePNGIcon(r"icon\overstrething_icon.PNG"), 
            tgt=self, sel=AircraftToolsetModule.ID_OVERSTRETHING)
        #增加功能组件三功能键
        AFXToolButton(p=group, label="\t材料库查询", 
            icon = afxCreatePNGIcon(r"icon\findmaterial.png"), 
            tgt=self, sel=AircraftToolsetModule.ID_FINDMATERIALS)    
        #增加功能组件四功能键
        AFXToolButton(p=group, label="\t帮助文档", 
            icon = afxCreatePNGIcon(r"icon\help.png"), 
            tgt=self, sel=AircraftToolsetModule.ID_HELP)  
        #增加功能组件五功能键      

        #创建菜单
        #***************************************************************
        menu = AFXMenuPane(self)
        #创建菜单栏
        AFXMenuTitle(self, '复合材料结构分析', None, menu)
        #创建主菜单，'复合材料结构分析'
        AFXMenuCommand(self, menu, '复合材料冲击损伤参数化建模程序', 
            afxCreatePNGIcon(r"icon\impact_icon.PNG"), 
            impactForm(self), AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, menu, '六边形蜂窝建模程序', 
            afxCreatePNGIcon(r"icon\honeycomb_icon.PNG"), 
            honeycombForm(self), AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, menu, '过拉伸蜂窝建模程序',
            afxCreatePNGIcon(r"icon\overstrething_icon.PNG"), 
            overstrethingForm(self), AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, menu, '典型试验件快速建模程序',
            afxCreatePNGIcon(r"icon\Ctest.PNG"), 
            CtestForm(self), AFXMode.ID_ACTIVATE)
        #创建四个子菜单，并关联其执行对象
        subMenu = AFXMenuPane(self)   
        AFXMenuCascade(self, menu, '子菜单一', None, subMenu) 
        AFXMenuCommand(self, subMenu, '子项目1', None, 
            self, AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, subMenu, '子项目2', None, 
            self, AFXMode.ID_ACTIVATE)
        #创建三级菜单
        #
        #***************************************************************
        #创建飞出按钮
        group = AFXToolboxGroup(self)       
        #为飞出工具条创建工具箱
        VFrame_1 = FXVerticalFrame(p=group, opts=0, x=0, y=0, 
            w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        #创建纵向排布框
        popup = FXPopup(getAFXApp().getAFXMainWindow(),opts=POPUP_HORIZONTAL) 
        #创建弹出面板，并指定其排布方向：水平或者竖直
        squareIcon =afxCreatePNGIcon(r"icon\honeycomb_icon.PNG")
        circleIcon =afxCreatePNGIcon(r"icon\impact_icon.PNG")        
        triangleIcon = afxCreatePNGIcon(r"icon\overstrething_icon.PNG")
        #创建三个图标
        AFXFlyoutItem(popup, '\tFlyout Button1', squareIcon, 
            honeycombForm(self), AFXMode.ID_ACTIVATE) 
        AFXFlyoutItem(popup, '\tFlyout Button 2', circleIcon,
            impactForm(self), AFXMode.ID_ACTIVATE)
        AFXFlyoutItem(popup, '\tFlyout Button 3', triangleIcon, 
            self, AircraftToolsetModule.ID_OVERSTRETHING) 
        #在飞出按钮中添加三个功能组件
        AFXFlyoutButton(group, popup) 
        #生成飞出按钮
        #
        #**************************************************************
    #定义功能组件一触发后的执行函数
    def onCmdCtest(self, sender, sel, ptr):
        CtestForm.activate(self.Ctest)
        #激活功能组件一，将其GUI界面打开
        return 1

    #定义功能组件二触发后的执行函数
    def onCmdHONEYCOMB(self, sender, sel, ptr):
        honeycombForm.activate(self.HONEYCOMB) 
        #激活功能组件二，将其GUI界面打开
        return 1
    #
    #定义功能组件三触发后的执行函数
    def onCmdOVERSTRETHING(self, sender, sel, ptr):

        overstrethingForm.activate(self.OVERSTRETHING) 
        #激活功能组件三
        return 1
    #
    #定义功能组件四触发后的执行函数
    def onCmdFindMaterials(self, sender, sel, ptr):
        materialcheck_plugin.activate(self.FINDMATERIALS)
        #激活功能组件四
        return 1
    #
    #定义功能组件五触发后的执行函数        
    def onCmdHelp(self, sender, sel, ptr):

        thisPath = os.path.abspath(__file__)
        thisDir = os.path.dirname(thisPath)
        #指定文件路径
        w = win32com.client.Dispatch('Word.Application')
        w.Visible = 1
        w.DisplayAlerts = 0
        #调用系统office→Word功能
        fileName = os.path.join(thisDir, r'HELP.doc')
        #指向本地名为'HELP.doc'的帮助文件
        doc = w.Documents.Open(FileName =fileName)
        #打开本地.doc文件
        return 1
    
    def getKernelInitializationCommand(self):
        return 'import aircraft.CtestKernel\
               \nimport toolset2.impact.impactKernel\
               \nimport aircraft.honeycombKernel\
               \nimport aircraft.overstrethingKernel'
        #定义内核初始命令