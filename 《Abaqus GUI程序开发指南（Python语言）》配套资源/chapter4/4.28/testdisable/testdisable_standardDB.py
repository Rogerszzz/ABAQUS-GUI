# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session

class testdisable_standardDB(AFXDataDialog):
    ID_Mybutton = AFXDataDialog.ID_LAST 
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Test Disable',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='Test Disable', 
            opts=FRAME_GROOVE)
        self.testdisable1=FXCheckButton(p=GroupBox_1, 
            text='Test Disable', tgt=form.testdisableKw, sel=0)
        self.radius1=AFXTextField(p=GroupBox_1, ncols=10, 
            labelText='radius:', tgt=form.radiusKw, sel=0)
        self.button1=FXButton(p=self, text='≤‚ ‘', ic=None, tgt=self, 
            sel=self.ID_Mybutton,
            opts=BUTTON_NORMAL,
            x=0, y=0, w=0, h=0, pl=0)              #◊‘∂®“Âpush button
        self.form=form

    def processUpdates(self):
    
        if self.form.testdisableKw.getValue() == False:
    
               self.button1.disable()
               self.radius1.disable()
        else:
               self.button1.enable()
               self.radius1.enable()
                        