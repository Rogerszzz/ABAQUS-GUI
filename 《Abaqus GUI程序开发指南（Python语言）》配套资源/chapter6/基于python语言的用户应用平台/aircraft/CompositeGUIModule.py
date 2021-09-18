#!/usr/bin/python
#-*-coding: UTF-8-*-
#-*-coding: mbcs -*- 
from abaqusGui import *                                     
from aircraft.CtestForm import CtestForm
#导入功能组件一
from toolset2.impact.impactForm import impactForm
#导入功能组件二：复合材料冲击损伤建模
from aircraft.honeycombForm import honeycombForm
#导入功能组件三
from aircraft.overstrethingForm import overstrethingForm
#导入功能组件四
from aircraft.materialcheck.materialcheck_plugin import materialcheck_plugin
#导入功能组件五：材料力学性能查询
class CompositeGUIModule(AFXModuleGui):
    
    def __init__(self):
    #
        mw=getAFXApp().getAFXMainWindow()
        AFXModuleGui.__init__(self, moduleName='Composites', 
            displayTypes=AFXModuleGui.PART)
        mw.appendApplicableModuleForTreeTab('Model',
            self.getModuleName() )
        #设置模型树的可用性
        mw.appendVisibleModuleForTreeTab('Model',
            self.getModuleName() )
        #设置模型树的可见性
        
        CtestForm1 = CtestForm(self)
        #实例化功能组件一
        impactForm1 = impactForm(self)  
        #实例化功能组件二
        honeycombForm1 = honeycombForm(self)
        #实例化功能组件三
        overstrethingForm1 = overstrethingForm(self)
        #实例化功能组件四
        # 
        #在模块中定义菜单
        #
        menu = AFXMenuPane(self)               
        #创建菜单栏
        AFXMenuTitle(self, '&Composites', None, menu)
        #创建主菜单，显示名为'Composites'
        AFXMenuCommand(self, menu, '&复合材料典型试验件快速建模', None,\
            CtestForm1, AFXMode.ID_ACTIVATE)
        #添加子菜单一
        AFXMenuCommand(self, menu, '&复合材料冲击损伤参数化建模', None,
            impactForm1 , AFXMode.ID_ACTIVATE)  #创建功能菜单          
        #添加子菜单二
        AFXMenuCommand(self, menu, '&六边形蜂窝参数化建模', None,
            honeycombForm1 , AFXMode.ID_ACTIVATE) 
        #添加子菜单三 
        AFXMenuCommand(self, menu, '&过拉伸蜂窝参数化建模', None,
            overstrethingForm1  , AFXMode.ID_ACTIVATE)  
        #添加子菜单四
        #
        #
        #创建工具箱
        group = AFXToolboxGroup(self)   
        #定义工具箱 
        CtestIcon =afxCreatePNGIcon(r"icon\Ctest.PNG")
        #定义功能组件一对应图标
        AFXToolButton(group, '\t典型试验件',CtestIcon, 
            CtestForm1, AFXMode.ID_ACTIVATE)
        #在工具箱中创建功能组件一的功能键
        #
        AFXToolButton(p=group, label="\t复合材料冲击损伤参数化建模程序", 
           icon = afxCreatePNGIcon(r"icon\impact_icon.PNG"), 
           tgt=impactForm(self), sel=AFXMode.ID_ACTIVATE)
        #在工具箱中创建功能组件二的功能键
        #
        AFXToolButton(p=group, label="\t六边形蜂窝参数化建模程序", 
            icon = afxCreatePNGIcon(r"icon\honeycomb_icon.PNG"), 
            tgt=honeycombForm(self), sel=AFXMode.ID_ACTIVATE)
        #在工具箱中创建功能组件三的功能键    
        #
        AFXToolButton(p=group, label="\t过拉伸蜂窝参数化建模程序", 
            icon = afxCreatePNGIcon(r"icon\overstrething_icon.PNG"), 
            tgt=overstrethingForm(self), sel=AFXMode.ID_ACTIVATE)
        #在工具箱中创建功能组件四的功能键
        #
        AFXToolButton(p=group, label="\t材料库查询", 
            icon = afxCreatePNGIcon(r"icon\findmaterial.png"), 
            tgt=materialcheck_plugin(self), 
            sel=AFXMode.ID_ACTIVATE) 
        #在工具箱中创建功能组件五的功能键
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
    def getKernelInitializationCommand(self):
        return 'import aircraft.CtestKernel\
               \nimport toolset2.impact.impactKernel\
               \nimport aircraft.honeycombKernel\
               \nimport aircraft.overstrethingKernel'
        #定义内核初始命令
#
CompositeGUIModule= CompositeGUIModule() 
#实例化自定义GUI模块