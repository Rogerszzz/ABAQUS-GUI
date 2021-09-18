#!/usr/bin/python
#-*-coding: UTF-8-*-
# -*- coding: mbcs -*-      
from abaqusConstants import *
from abaqusGui import *
from sessionGui import *
from kernelAccess import mdb,session
from canvasGui import CanvasToolsetGui
from viewManipGui import ViewManipToolsetGui
from aircraft.aircraftToolsetModule import AircraftToolsetModule
#从aircraft包内导入工具包AircraftToolsetModule
from toolset2.aircraftToolsetModule2 import AircraftToolsetModule2
#从toolset2包内导入工具包AircraftToolsetModule2
from aircraft.CompositeTreeToolsetGui import CompositeTreeToolsetGui
#从aircraft包内导入树形工具包CompositeTreeToolsetGui
########################################################################
# Class Definition
########################################################################
class CaeMainWindow(AFXMainWindow):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     def __init__(self, app, windowTitle='我的应用程序'):
         # 构建GUI程序基础结构
         #
         AFXMainWindow.__init__(self, app, windowTitle)

         # 注册标准abaqus/CAE固有的工具包
         #
         self.registerToolset(FileToolsetGui(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR)
         self.registerToolset(ModelToolsetGui(), 
             GUI_IN_MENUBAR)
         self.registerToolset(CanvasToolsetGui(), 
             GUI_IN_MENUBAR)
         self.registerToolset(ViewManipToolsetGui(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR)
         self.registerToolset(AnnotationToolsetGui(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBOX)
         self.registerToolset(CustomizeToolsetGui(), 
             GUI_IN_MENUBAR|GUI_IN_TOOL_PANE)
         self.registerToolset(DatumToolsetGui(), 
             GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE)
         self.registerToolset(EditMeshToolsetGui(), 
             GUI_IN_TOOLBOX | GUI_IN_TOOL_PANE)
         self.registerToolset(SelectionToolsetGui(), GUI_IN_TOOLBAR)                   
         
         self.registerToolset(AircraftToolsetModule(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR|GUI_IN_TOOLBOX)
         #注册自定义工具包一
         self.registerToolset(AircraftToolsetModule2(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR|GUI_IN_TOOLBOX)
         #注册自定义工具包二
         self.registerToolset(CompositeTreeToolsetGui(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR|GUI_IN_TOOLBOX)  
         #注册自定义树形工具包 
         registerPluginToolset()
         #注册插件工具
         self.registerHelpToolset(HelpToolsetGui(),
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR)
         #注册帮助工具包
         self.registerToolset(TreeToolsetGui(),GUI_IN_MENUBAR)
         #注册abaqus/CAE主窗口左侧固有树形工具包
         #
         #注册模块
         self.registerModule('复合材料',  'aircraft.CompositeGUIModule')
         #注册自定义模块'Composites'并将其显示名称改为'复合材料'
         self.registerModule('零件', 'Part')
         #注册标准abaqus/CAE模块'Part'
         self.registerModule('属性',  'Property')
         #将标准abaqus/CAE模块'Property'显示名称改为中文格式
         self.registerModule('Assembly',      'Assembly')
         self.registerModule('Step',          'Step')
         self.registerModule('Interaction', 'Interaction')
         self.registerModule('Load',          'Load')
         self.registerModule('Mesh',          'Mesh')
         self.registerModule('Job', 'Job')
         self.registerModule('Visualization', 'Visualization')
         self.registerModule('Sketch',        'Sketch')