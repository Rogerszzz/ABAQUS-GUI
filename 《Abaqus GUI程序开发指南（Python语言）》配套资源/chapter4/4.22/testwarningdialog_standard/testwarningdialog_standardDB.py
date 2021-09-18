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

class testwarningdialog_standardDB(AFXDataDialog):
   
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #
       
        AFXDataDialog.__init__(self, form, '´´½¨´ø¿×°å',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
       
    

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='name:', tgt=form.partnameKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='Width (w):', tgt=form.widthKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='height(h):', tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='radius(r):', tgt=form.radiusKw, sel=0)
        GroupBox_2 = FXGroupBox(p=self, text='Diagram', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, r'platewithhole.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_2, text='', ic=icon)