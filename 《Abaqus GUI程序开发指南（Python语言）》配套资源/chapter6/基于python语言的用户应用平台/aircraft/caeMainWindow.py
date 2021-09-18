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
#��aircraft���ڵ��빤�߰�AircraftToolsetModule
from toolset2.aircraftToolsetModule2 import AircraftToolsetModule2
#��toolset2���ڵ��빤�߰�AircraftToolsetModule2
from aircraft.CompositeTreeToolsetGui import CompositeTreeToolsetGui
#��aircraft���ڵ������ι��߰�CompositeTreeToolsetGui
########################################################################
# Class Definition
########################################################################
class CaeMainWindow(AFXMainWindow):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     def __init__(self, app, windowTitle='�ҵ�Ӧ�ó���'):
         # ����GUI��������ṹ
         #
         AFXMainWindow.__init__(self, app, windowTitle)

         # ע���׼abaqus/CAE���еĹ��߰�
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
         #ע���Զ��幤�߰�һ
         self.registerToolset(AircraftToolsetModule2(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR|GUI_IN_TOOLBOX)
         #ע���Զ��幤�߰���
         self.registerToolset(CompositeTreeToolsetGui(), 
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR|GUI_IN_TOOLBOX)  
         #ע���Զ������ι��߰� 
         registerPluginToolset()
         #ע��������
         self.registerHelpToolset(HelpToolsetGui(),
             GUI_IN_MENUBAR|GUI_IN_TOOLBAR)
         #ע��������߰�
         self.registerToolset(TreeToolsetGui(),GUI_IN_MENUBAR)
         #ע��abaqus/CAE���������������ι��߰�
         #
         #ע��ģ��
         self.registerModule('���ϲ���',  'aircraft.CompositeGUIModule')
         #ע���Զ���ģ��'Composites'��������ʾ���Ƹ�Ϊ'���ϲ���'
         self.registerModule('���', 'Part')
         #ע���׼abaqus/CAEģ��'Part'
         self.registerModule('����',  'Property')
         #����׼abaqus/CAEģ��'Property'��ʾ���Ƹ�Ϊ���ĸ�ʽ
         self.registerModule('Assembly',      'Assembly')
         self.registerModule('Step',          'Step')
         self.registerModule('Interaction', 'Interaction')
         self.registerModule('Load',          'Load')
         self.registerModule('Mesh',          'Mesh')
         self.registerModule('Job', 'Job')
         self.registerModule('Visualization', 'Visualization')
         self.registerModule('Sketch',        'Sketch')