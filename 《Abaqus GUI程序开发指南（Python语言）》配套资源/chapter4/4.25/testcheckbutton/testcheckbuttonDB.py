# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testcheckbuttonDB(AFXDataDialog):
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, 'Test Check Button',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')          
        GroupBox_1 = FXGroupBox(p=self, text='Element type', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_1, text='SOLID\tѡ��ʵ�嵥Ԫ', tgt=form.ele_solidKw, sel=0)
        FXCheckButton(p=GroupBox_1, text='SEHLL\tѡ��ǵ�Ԫ', tgt=form.ele_shellKw, sel=0)

        mainWindow = getAFXApp().getAFXMainWindow()
        target = mainWindow.getTargetFromFunction('Material->Create')
        selector = mainWindow.getSelectorFromFunction('Material->Create')
        FXButton(GroupBox_1, '��������', tgt=target, sel=selector )    