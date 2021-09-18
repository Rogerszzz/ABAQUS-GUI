#!/usr/bin/python
#-*-coding: UTF-8-*-
#-*-coding: mbcs -*- 
from abaqusGui import *
from abaqusConstants import *
from toolset2.impact.impactForm import impactForm
#���빦�����
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

        AFXToolsetGui.__init__(self, '�ɻ����ϲ��Ͻṹ����')
        #��ʼ�����߰�

        FXMAPFUNC(self, SEL_COMMAND, self.ID_IMPACT, 
            AircraftToolsetModule2.onCmdIMPACT)  
        self.IMPACT = impactForm(self) 
        #���������ϲ��ϳ�����˲�������ģ����  
        #
        group = AFXToolbarGroup(self,'composite tools','���ϲ��Ͻṹ��ģ����')
        icon = afxCreatePNGIcon(r"icon\airtransport.png")
        FXLabel(p=group, text='', ic=icon)
        #�����µĹ�����    
        AFXToolButton(p=group, label="\t���ϲ��ϳ�����˲�������ģ����",
            icon = afxCreatePNGIcon(r"icon\impact_icon.PNG"), 
            tgt=impactForm(self), sel=AFXMode.ID_ACTIVATE)
        #�����������Ӹ��ϲ��ϳ�������Զ���ģ�����ܰ���   
    def getKernelInitializationCommand(self):
        return 'import toolset2.impact.impactKernel'
        #�����ں˳�ʼ����
    #
    #���幦������������ִ�к���    
    def onCmdIMPACT(self, sender, sel, ptr):

        impactForm.activate(self.IMPACT)
        #��������
        return 1