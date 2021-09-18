# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
from test1_form import test1_form
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class createPlateWithholeDB(AFXDataDialog):

    def __init__(self, form):

        self.test1_form = test1_form(form.getOwner()) 
        AFXDataDialog.__init__(self, form, '���װ��������ģ����',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR|DECOR_RESIZE)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='����', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='����� :', 
            tgt=form.partnameKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='���(w):', 
            tgt=form.widthKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='�߶�(h):', 
            tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='�뾶(r):', 
            tgt=form.radiusKw, sel=0)
        GroupBox_3 = FXGroupBox(p=self, text='ʾ��ͼ', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, r'planewithhole.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_3, text='', ic=icon)
        GroupBox_2 = FXGroupBox(p=self, text='Test Radio Button', opts=FRAME_GROOVE)
        FXRadioButton(p=GroupBox_2, text='YES', tgt=form.radiobuttonKw1, sel=27)
        FXRadioButton(p=GroupBox_2, text='NO', tgt=form.radiobuttonKw1, sel=28)

