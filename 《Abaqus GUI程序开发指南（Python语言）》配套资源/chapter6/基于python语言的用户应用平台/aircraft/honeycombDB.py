#-*-coding: UTF-8-*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class honeycombDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '六边形蜂窝自动建模程序',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('确定')       
        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('应用')
        cancelBtn = self.getActionButton(self.ID_CLICKED_CANCEL)
        cancelBtn.setText('取消')
            
        GroupBox_1 = FXGroupBox(p=self, text='示意图', opts=FRAME_GROOVE)
        icon = afxCreatePNGIcon(r"icon\honeycomb_diagram.PNG")
        FXLabel(p=GroupBox_1, text='', ic=icon)
        GroupBox_4 = FXGroupBox(p=self, text='', opts=FRAME_GROOVE)
        HFrame_2 = FXHorizontalFrame(p=GroupBox_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_2 = FXGroupBox(p=HFrame_2, text='晶格几何参数', opts=FRAME_GROOVE)
        HFrame_1 = FXHorizontalFrame(p=GroupBox_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VFrame_2 = FXVerticalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
#定义radiobutton        
        FXRadioButton(p=VFrame_2, text='晶格边长', tgt=form.celldimentionKw1, sel=1)
        FXRadioButton(p=VFrame_2, text='晶格直径', tgt=form.celldimentionKw1, sel=2)
        if isinstance(VFrame_2, FXHorizontalFrame):
            FXVerticalSeparator(p=VFrame_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=VFrame_2, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=VFrame_2, text='蜂窝厚度', opts=JUSTIFY_LEFT)
        VFrame_3 = FXVerticalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        self.celllengthtext=AFXTextField(p=VFrame_3, ncols=8, labelText='l(mm):', tgt=form.celllengthKw, sel=0)
        self.celldiametertext=AFXTextField(p=VFrame_3, ncols=8, labelText='D(mm):', tgt=form.celldiameterKw, sel=0)
        AFXTextField(p=VFrame_3, ncols=8, labelText='t(mm):', tgt=form.thicknessKw, sel=0)
#定义text控件的可用性        
        self.addTransition(form.celldimentionKw1, AFXTransition.EQ,
            1, self.celllengthtext,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.celldimentionKw1, AFXTransition.EQ,
            1, self.celldiametertext,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)    
        self.addTransition(form.celldimentionKw1, AFXTransition.EQ,
            2, self.celldiametertext,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.celldimentionKw1, AFXTransition.EQ,
            2,self.celllengthtext,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)     
               
        GroupBox_3 = FXGroupBox(p=HFrame_2, text='蜂窝板几何尺寸', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_3, ncols=12, labelText='长度(L):', tgt=form.panellengthKw, sel=0)
        AFXTextField(p=GroupBox_3, ncols=12, labelText='宽度(W):', tgt=form.panelwidthKw, sel=0)
        AFXTextField(p=GroupBox_3, ncols=12, labelText='高度(H):', tgt=form.panelheightKw, sel=0)
        GroupBox_5 = FXGroupBox(p=self, text='材料及属性', opts=FRAME_GROOVE)
        HFrame_4 = FXHorizontalFrame(p=GroupBox_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        frame = FXHorizontalFrame(HFrame_4, 0, 0,0,0,0, 0,0,0,0)

        # Model combo
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        #
        self.RootComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='模型:', tgt=form.modelNameKw, sel=0)
        self.RootComboBox_1.setMaxVisible(10)

        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_1.appendItem(name)
        if not form.modelNameKw.getValue() in names:
            form.modelNameKw.setValue( names[0] )
        msgCount = 15
        form.modelNameKw.setTarget(self)
        form.modelNameKw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_1MaterialsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' % (msgCount, msgHandler) )

        # Materials combo
        #
        self.ComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='材料:', tgt=form.materialNameKw, sel=0)
        self.ComboBox_1.setMaxVisible(10)

        self.form = form
        AFXTextField(p=HFrame_4, ncols=9, labelText='零件名:', tgt=form.partNameKw, sel=0)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):

        AFXDataDialog.show(self)

        # Register a query on materials
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelNameKw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].materials.registerQuery(self.updateComboBox_1Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):

        AFXDataDialog.hide(self)

        mdb.models[self.currentModelName].materials.unregisterQuery(self.updateComboBox_1Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_1MaterialsChanged(self, sender, sel, ptr):

        self.updateComboBox_1Materials()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_1Materials(self):

        modelName = self.form.modelNameKw.getValue()

        # Update the names in the Materials combo
        #
        self.ComboBox_1.clearItems()
        names = mdb.models[modelName].materials.keys()
        names.sort()
        for name in names:
            self.ComboBox_1.appendItem(name)
        if names:
            if not self.form.materialNameKw.getValue() in names:
                self.form.materialNameKw.setValue( names[0] )
        else:
            self.form.materialNameKw.setValue('')

        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )

