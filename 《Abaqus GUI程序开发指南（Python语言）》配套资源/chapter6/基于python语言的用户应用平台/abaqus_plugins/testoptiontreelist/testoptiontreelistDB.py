#-*-coding: UTF-8-*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testoptiontreelistDB(AFXDataDialog):
    def __init__(self, form):

        AFXDataDialog.__init__(self, form, '控件测试',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')            
        vf = FXHorizontalFrame(p=self, opts=FRAME_SUNKEN|FRAME_THICK,    
            x=0, y=0, w=0, h=0,                                              
            pl=0, pr=DEFAULT_SPACING, pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)  
        tree = AFXOptionTreeList(vf, 8)        
        item1 = tree.addItemLast('非线性')
        item1.addItemLast('材料非线性')
        item1.addItemLast('几何非线性')
        item1.addItemLast('接触非线性')
        item2 =tree.addItemLast('失效判据')                                                                                                                                               
        item2.addItemLast('二维判据')
        item2.addItemLast('三维判据')