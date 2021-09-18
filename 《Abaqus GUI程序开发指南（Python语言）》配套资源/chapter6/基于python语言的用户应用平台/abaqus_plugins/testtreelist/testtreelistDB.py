from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testtreelistDB(AFXDataDialog):
    [                                             
        ID_CLICKED,                               
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1) 
    def __init__(self, form):

        AFXDataDialog.__init__(self, form, 'Test Treelist',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')            
        vf = FXHorizontalFrame(p=self, opts=FRAME_SUNKEN|FRAME_THICK,    
            x=0, y=0, w=100, h=0,                                              
            pl=0, pr=DEFAULT_SPACING, pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)  
        self.tree = FXTreeList(vf, 10, tgt=self, sel=self.ID_CLICKED,                 
            opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|                                  
            TREELIST_SHOWS_BOXES|TREELIST_ROOT_BOXES|                          
            TREELIST_SHOWS_LINES|LAYOUT_FIX_WIDTH,      
            x=0, y=0, w=120, h=0)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CLICKED, testtreelistDB.onCmdTree)   
        Icon1 =afxCreateIcon( os.path.join(thisDir, 'ico1.png') )
        Icon2 =afxCreateIcon( os.path.join(thisDir, 'ico2.png') ) 
                                            
        option1 = self.tree.addItemLast(None, 'Option 1')                      
        self.tree.addItemLast(option1, 'Option 1a',oi=Icon1,ci=Icon2)                            
        self.tree.addItemLast(option1, 'Option 1b')                            
        option2 = self.tree.addItemLast(None, 'Option 2')                      
        self.tree.addItemLast(option2, 'Option 2a')                            
        option2b = self.tree.addItemLast(option2, 'Option 2b')                 
        self.tree.addItemLast(option2b, 'Option 2bi')                          
        option3 = self.tree.addItemLast(None, 'Option 3')                                                                                                                                                  
    def onCmdTree(self, sender, sel, ptr):

        w = self.tree.getFirstItem()
        while(w):
            if self.tree.isItemSelected(w):
                item=self.tree.getCurrentItem()     
                text=self.tree.getItemText(item)
                print '%s was selected.' % text   
                break
            if w.getFirst():
                w=w.getFirst()
                continue
            while not w.getNext() and w.getParent():
                 w=w.getParent()
            w=w.getNext()