#!/usr/bin/python
#-*-coding: UTF-8-*-
#-*-coding: mbcs -*- 
from abaqusGui import *                                     
from aircraft.CtestForm import CtestForm
#���빦�����һ
from toolset2.impact.impactForm import impactForm
#���빦������������ϲ��ϳ�����˽�ģ
from aircraft.honeycombForm import honeycombForm
#���빦�������
from aircraft.overstrethingForm import overstrethingForm
#���빦�������
from aircraft.materialcheck.materialcheck_plugin import materialcheck_plugin
#���빦������壺������ѧ���ܲ�ѯ
class CompositeGUIModule(AFXModuleGui):
    
    def __init__(self):
    #
        mw=getAFXApp().getAFXMainWindow()
        AFXModuleGui.__init__(self, moduleName='Composites', 
            displayTypes=AFXModuleGui.PART)
        mw.appendApplicableModuleForTreeTab('Model',
            self.getModuleName() )
        #����ģ�����Ŀ�����
        mw.appendVisibleModuleForTreeTab('Model',
            self.getModuleName() )
        #����ģ�����Ŀɼ���
        
        CtestForm1 = CtestForm(self)
        #ʵ�����������һ
        impactForm1 = impactForm(self)  
        #ʵ�������������
        honeycombForm1 = honeycombForm(self)
        #ʵ�������������
        overstrethingForm1 = overstrethingForm(self)
        #ʵ�������������
        # 
        #��ģ���ж���˵�
        #
        menu = AFXMenuPane(self)               
        #�����˵���
        AFXMenuTitle(self, '&Composites', None, menu)
        #�������˵�����ʾ��Ϊ'Composites'
        AFXMenuCommand(self, menu, '&���ϲ��ϵ�����������ٽ�ģ', None,\
            CtestForm1, AFXMode.ID_ACTIVATE)
        #����Ӳ˵�һ
        AFXMenuCommand(self, menu, '&���ϲ��ϳ�����˲�������ģ', None,
            impactForm1 , AFXMode.ID_ACTIVATE)  #�������ܲ˵�          
        #����Ӳ˵���
        AFXMenuCommand(self, menu, '&�����η��Ѳ�������ģ', None,
            honeycombForm1 , AFXMode.ID_ACTIVATE) 
        #����Ӳ˵��� 
        AFXMenuCommand(self, menu, '&��������Ѳ�������ģ', None,
            overstrethingForm1  , AFXMode.ID_ACTIVATE)  
        #����Ӳ˵���
        #
        #
        #����������
        group = AFXToolboxGroup(self)   
        #���幤���� 
        CtestIcon =afxCreatePNGIcon(r"icon\Ctest.PNG")
        #���幦�����һ��Ӧͼ��
        AFXToolButton(group, '\t���������',CtestIcon, 
            CtestForm1, AFXMode.ID_ACTIVATE)
        #�ڹ������д����������һ�Ĺ��ܼ�
        #
        AFXToolButton(p=group, label="\t���ϲ��ϳ�����˲�������ģ����", 
           icon = afxCreatePNGIcon(r"icon\impact_icon.PNG"), 
           tgt=impactForm(self), sel=AFXMode.ID_ACTIVATE)
        #�ڹ������д�������������Ĺ��ܼ�
        #
        AFXToolButton(p=group, label="\t�����η��Ѳ�������ģ����", 
            icon = afxCreatePNGIcon(r"icon\honeycomb_icon.PNG"), 
            tgt=honeycombForm(self), sel=AFXMode.ID_ACTIVATE)
        #�ڹ������д�������������Ĺ��ܼ�    
        #
        AFXToolButton(p=group, label="\t��������Ѳ�������ģ����", 
            icon = afxCreatePNGIcon(r"icon\overstrething_icon.PNG"), 
            tgt=overstrethingForm(self), sel=AFXMode.ID_ACTIVATE)
        #�ڹ������д�����������ĵĹ��ܼ�
        #
        AFXToolButton(p=group, label="\t���Ͽ��ѯ", 
            icon = afxCreatePNGIcon(r"icon\findmaterial.png"), 
            tgt=materialcheck_plugin(self), 
            sel=AFXMode.ID_ACTIVATE) 
        #�ڹ������д������������Ĺ��ܼ�
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
    def getKernelInitializationCommand(self):
        return 'import aircraft.CtestKernel\
               \nimport toolset2.impact.impactKernel\
               \nimport aircraft.honeycombKernel\
               \nimport aircraft.overstrethingKernel'
        #�����ں˳�ʼ����
#
CompositeGUIModule= CompositeGUIModule() 
#ʵ�����Զ���GUIģ��