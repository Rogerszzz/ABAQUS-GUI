# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
#######################################################################
# Class definition
#######################################################################
class createPlateWithholeDB(AFXDataDialog):
    ID_Mybutton = AFXDataDialog.ID_LAST          #分配ID
    def __init__(self, form):

        AFXDataDialog.__init__(self, form, '带孔板参数化建模程序',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='参数', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='零件名 :', 
            tgt=form.partnameKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='宽度(w):', 
            tgt=form.widthKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='高度(h):', 
            tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='半径(r):', 
            tgt=form.radiusKw, sel=0)
        GroupBox_3 = FXGroupBox(p=self, text='示意图', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, r'planewithhole.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_3, text='', ic=icon)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_Mybutton, 
            createPlateWithholeDB.onCmdMybutton)
        FXButton(p=self, text='打印', ic=None, tgt=self, 
            sel=self.ID_Mybutton,
            opts=BUTTON_NORMAL,
            x=0, y=0, w=0, h=0, pl=0)

    def onCmdMybutton(self, sender, sel, ptr):
        if SELID(sel) == self.ID_Mybutton:                        #使用SELID函数获取消息ID
            print 'Button 1 was pressed.'                          
            #在DOS界面下输出提示信息
            mw = getAFXApp().getAFXMainWindow()
            mw.writeToMessageArea('Button 1 was pressed.' )        
            #在abaqus/CAE主窗口下方的提示区显示提示信息
            return 1

