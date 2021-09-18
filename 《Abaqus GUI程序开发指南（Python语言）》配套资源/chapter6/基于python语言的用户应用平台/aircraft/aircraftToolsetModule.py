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
#������������
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
    #Ϊ�������������ID
    def __init__(self):

        AFXToolsetGui.__init__(self, '���Ĺ�����')
        #��ʼ�����߰�
        FXMAPFUNC(self, SEL_COMMAND, self.ID_Ctest, 
            AircraftToolsetModule.onCmdCtest)  
        self.Ctest = CtestForm(self)
        #�����������һ
        FXMAPFUNC(self, SEL_COMMAND, self.ID_HONEYCOMB, 
            AircraftToolsetModule.onCmdHONEYCOMB)  
        self.HONEYCOMB = honeycombForm(self)
        #�������������
        FXMAPFUNC(self, SEL_COMMAND, self.ID_OVERSTRETHING, 
            AircraftToolsetModule.onCmdOVERSTRETHING)  
        self.OVERSTRETHING = overstrethingForm(self)
        #�������������
        FXMAPFUNC(self, SEL_COMMAND, self.ID_HELP, 
            AircraftToolsetModule.onCmdHelp)
        #������������ģ������ĵ�����
        FXMAPFUNC(self, SEL_COMMAND, self.ID_FINDMATERIALS, 
             AircraftToolsetModule.onCmdFindMaterials)
        self.FINDMATERIALS=materialcheck_plugin(self)               
        #������������壺������ѧ���ܲ�ѯ
        #
        #***************************************************************
        group = AFXToolbarGroup(self,'�ṹ��Ʒ�������','�ṹ��Ʒ�������')
        #����������������Ϊ'�ṹ��Ʒ�������'
        icon = afxCreatePNGIcon(r"icon\air.PNG")
        #����ͼ��
        FXLabel(p=group, text='', ic=icon)
        #�ڹ���������ӱ�ǩ
        #
        AFXToolButton(p=group, label="\t���ϲ��ϵ�����������ٽ�ģ����", 
            icon = afxCreatePNGIcon(r"icon\Ctest.PNG"), 
            tgt=CtestForm(self), sel=AFXMode.ID_ACTIVATE)
        #���ӹ������һ���ܼ�
        AFXToolButton(p=group, label="\t�����η��Ѳ�������ģ����", 
            icon = afxCreatePNGIcon(r"icon\honeycomb_icon.PNG"), 
            tgt=honeycombForm(self), sel=AFXMode.ID_ACTIVATE)
        #���ӹ�����������ܼ�       
        AFXToolButton(p=group, label="\t��������Ѳ�������ģ����", 
            icon = afxCreatePNGIcon(r"icon\overstrething_icon.PNG"), 
            tgt=self, sel=AircraftToolsetModule.ID_OVERSTRETHING)
        #���ӹ�����������ܼ�
        AFXToolButton(p=group, label="\t���Ͽ��ѯ", 
            icon = afxCreatePNGIcon(r"icon\findmaterial.png"), 
            tgt=self, sel=AircraftToolsetModule.ID_FINDMATERIALS)    
        #���ӹ�������Ĺ��ܼ�
        AFXToolButton(p=group, label="\t�����ĵ�", 
            icon = afxCreatePNGIcon(r"icon\help.png"), 
            tgt=self, sel=AircraftToolsetModule.ID_HELP)  
        #���ӹ�������幦�ܼ�      

        #�����˵�
        #***************************************************************
        menu = AFXMenuPane(self)
        #�����˵���
        AFXMenuTitle(self, '���ϲ��Ͻṹ����', None, menu)
        #�������˵���'���ϲ��Ͻṹ����'
        AFXMenuCommand(self, menu, '���ϲ��ϳ�����˲�������ģ����', 
            afxCreatePNGIcon(r"icon\impact_icon.PNG"), 
            impactForm(self), AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, menu, '�����η��ѽ�ģ����', 
            afxCreatePNGIcon(r"icon\honeycomb_icon.PNG"), 
            honeycombForm(self), AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, menu, '��������ѽ�ģ����',
            afxCreatePNGIcon(r"icon\overstrething_icon.PNG"), 
            overstrethingForm(self), AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, menu, '������������ٽ�ģ����',
            afxCreatePNGIcon(r"icon\Ctest.PNG"), 
            CtestForm(self), AFXMode.ID_ACTIVATE)
        #�����ĸ��Ӳ˵�����������ִ�ж���
        subMenu = AFXMenuPane(self)   
        AFXMenuCascade(self, menu, '�Ӳ˵�һ', None, subMenu) 
        AFXMenuCommand(self, subMenu, '����Ŀ1', None, 
            self, AFXMode.ID_ACTIVATE)
        AFXMenuCommand(self, subMenu, '����Ŀ2', None, 
            self, AFXMode.ID_ACTIVATE)
        #���������˵�
        #
        #***************************************************************
        #�����ɳ���ť
        group = AFXToolboxGroup(self)       
        #Ϊ�ɳ�����������������
        VFrame_1 = FXVerticalFrame(p=group, opts=0, x=0, y=0, 
            w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        #���������Ų���
        popup = FXPopup(getAFXApp().getAFXMainWindow(),opts=POPUP_HORIZONTAL) 
        #����������壬��ָ�����Ų�����ˮƽ������ֱ
        squareIcon =afxCreatePNGIcon(r"icon\honeycomb_icon.PNG")
        circleIcon =afxCreatePNGIcon(r"icon\impact_icon.PNG")        
        triangleIcon = afxCreatePNGIcon(r"icon\overstrething_icon.PNG")
        #��������ͼ��
        AFXFlyoutItem(popup, '\tFlyout Button1', squareIcon, 
            honeycombForm(self), AFXMode.ID_ACTIVATE) 
        AFXFlyoutItem(popup, '\tFlyout Button 2', circleIcon,
            impactForm(self), AFXMode.ID_ACTIVATE)
        AFXFlyoutItem(popup, '\tFlyout Button 3', triangleIcon, 
            self, AircraftToolsetModule.ID_OVERSTRETHING) 
        #�ڷɳ���ť����������������
        AFXFlyoutButton(group, popup) 
        #���ɷɳ���ť
        #
        #**************************************************************
    #���幦�����һ�������ִ�к���
    def onCmdCtest(self, sender, sel, ptr):
        CtestForm.activate(self.Ctest)
        #��������һ������GUI�����
        return 1

    #���幦��������������ִ�к���
    def onCmdHONEYCOMB(self, sender, sel, ptr):
        honeycombForm.activate(self.HONEYCOMB) 
        #����������������GUI�����
        return 1
    #
    #���幦��������������ִ�к���
    def onCmdOVERSTRETHING(self, sender, sel, ptr):

        overstrethingForm.activate(self.OVERSTRETHING) 
        #����������
        return 1
    #
    #���幦������Ĵ������ִ�к���
    def onCmdFindMaterials(self, sender, sel, ptr):
        materialcheck_plugin.activate(self.FINDMATERIALS)
        #����������
        return 1
    #
    #���幦������崥�����ִ�к���        
    def onCmdHelp(self, sender, sel, ptr):

        thisPath = os.path.abspath(__file__)
        thisDir = os.path.dirname(thisPath)
        #ָ���ļ�·��
        w = win32com.client.Dispatch('Word.Application')
        w.Visible = 1
        w.DisplayAlerts = 0
        #����ϵͳoffice��Word����
        fileName = os.path.join(thisDir, r'HELP.doc')
        #ָ�򱾵���Ϊ'HELP.doc'�İ����ļ�
        doc = w.Documents.Open(FileName =fileName)
        #�򿪱���.doc�ļ�
        return 1
    
    def getKernelInitializationCommand(self):
        return 'import aircraft.CtestKernel\
               \nimport toolset2.impact.impactKernel\
               \nimport aircraft.honeycombKernel\
               \nimport aircraft.overstrethingKernel'
        #�����ں˳�ʼ����