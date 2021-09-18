#-*-coding: UTF-8-*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testoptiontreelistDB(AFXDataDialog):
    def __init__(self, form):

        AFXDataDialog.__init__(self, form, '�ؼ�����',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')            
        vf = FXHorizontalFrame(p=self, opts=FRAME_SUNKEN|FRAME_THICK,    
            x=0, y=0, w=0, h=0,                                              
            pl=0, pr=DEFAULT_SPACING, pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)  
        tree = AFXOptionTreeList(vf, 8)        
        item1 = tree.addItemLast('������')
        item1.addItemLast('���Ϸ�����')
        item1.addItemLast('���η�����')
        item1.addItemLast('�Ӵ�������')
        item2 =tree.addItemLast('ʧЧ�о�')                                                                                                                                               
        item2.addItemLast('��ά�о�')
        item2.addItemLast('��ά�о�')