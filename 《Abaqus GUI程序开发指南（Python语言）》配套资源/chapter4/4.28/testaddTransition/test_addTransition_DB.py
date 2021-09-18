# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
class test_addTransition_DB(AFXDataDialog):
    ID_Mybutton = AFXDataDialog.ID_LAST 
    def __init__(self, form):

        AFXDataDialog.__init__(self, form, 'Test addTransition',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_1 = FXGroupBox(p=self, text='Test addTransition',
            opts=FRAME_GROOVE)

        self.yesno1=FXCheckButton(p=GroupBox_1,
            text='Cohesive Element', tgt=form.yesnoKw, sel=0)
        self.radius1=AFXTextField(p=GroupBox_1, ncols=10, 
            labelText='radius:', tgt=form.radiusKw, sel=0)

        self.addTransition(form.yesnoKw, AFXTransition.EQ,
            False,self.radius1,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnoKw, AFXTransition.EQ,
            True,self.radius1,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)    
