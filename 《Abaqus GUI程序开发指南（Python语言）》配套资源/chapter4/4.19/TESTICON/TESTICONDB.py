# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class TESTICONDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, 'Test Icon',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)           
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')

        fileName1 = os.path.join(thisDir, 'icon_up.png')
        icon_up = afxCreatePNGIcon(fileName1) 
        fileName2 = os.path.join(thisDir, 'icon_down.bmp')
        icon_down = afxCreateBMPIcon(fileName2)            
        FXButton(p=self, text='\tUP', ic=icon_up , tgt=None, sel=0)
        FXButton(p=self, text='\tDOWN', ic=icon_down, tgt=None, sel=0)
