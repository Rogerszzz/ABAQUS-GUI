# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class createPlateWithholeDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '带孔板参数化建模程序',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='参数', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='零件名 :', tgt=form.partnameKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='宽度(w):', tgt=form.widthKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='高度(h):', tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='半径(r):', tgt=form.radiusKw, sel=0)
        GroupBox_3 = FXGroupBox(p=self, text='示意图', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, r'planewithhole.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_3, text='', ic=icon)
