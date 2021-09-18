# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
class testFXMatrixDB(AFXDataDialog):
    def __init__(self, form):

        AFXDataDialog.__init__(self, form, 'Test FXMatrix',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
       
        m=FXMatrix(self, n=3,opts=MATRIX_BY_COLUMNS)       
        
        FXButton(m, 'Button 1')
        FXButton(m, 'Button 2')
        FXButton(m, 'Button 3')
        FXButton(m, 'Button 4')
        FXButton(m, 'Button 5')
        FXButton(m, 'Button 6') 









