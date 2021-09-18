#-*-coding: UTF-8-*-
# -*- coding: mbcs -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class CtestDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '复合材料许用值试验快速建模系统-jly4553',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('确定')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('应用')
        cancelBtn = self.getActionButton(self.ID_CLICKED_CANCEL)
        cancelBtn.setText('取消')
            
        GroupBox_3 = FXGroupBox(p=self, text='参数', opts=FRAME_GROOVE)
        TabBook_1 = FXTabBook(p=GroupBox_3, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_1, text='零件参数', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_4 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        GroupBox_17 = FXGroupBox(p=TabItem_4, text='', opts=FRAME_GROOVE)
        frame = AFXVerticalAligner(GroupBox_17, 0, 0,0,0,0, 0,0,0,0)

        # Model combo
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        #
        self.RootComboBox_4 = AFXComboBox(p=frame, ncols=0, nvis=1, text='选择模型:   ', tgt=form.modelName1Kw, sel=0)
        self.RootComboBox_4.setMaxVisible(10)

        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_4.appendItem(name)
        if not form.modelName1Kw.getValue() in names:
            form.modelName1Kw.setValue( names[0] )
        msgCount = 155
        form.modelName1Kw.setTarget(self)
        form.modelName1Kw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_4PartsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' % (msgCount, msgHandler) )

        # Parts combo
        #
        self.ComboBox_4 = AFXComboBox(p=frame, ncols=0, nvis=1, text='选择基础零件:   ', tgt=form.partNameKw, sel=0)
        self.ComboBox_4.setMaxVisible(10)
        #添加坐标系选取按钮，在视图中选取创建的坐标系。        
        pickHf = FXHorizontalFrame(p=frame, opts=0, x=0, y=0, w=0, h=0,                                          
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)                                           
        # Note: Set the selector to indicate that this widget should not be                                           
        #       colored differently from its parent when the 'Color layout managers'                                  
        #       button is checked in the RSG Dialog Builder dialog.                                                   
        pickHf.setSelector(99)                                                                                        
        label = FXLabel(p=pickHf, text='坐标系： (空)    ', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)                     
        pickHandler = CtestDBPickHandler(form, form.CSYSKWKw, '从视图中选取坐标系', DATUM_CSYS, ONE, label)  
#        icon = afxCreatePNGIcon(os.path.join(thisDir, 'icon\selectIcon.png')) 
        icon =afxCreatePNGIcon(r"icon\selectIcon.png")                                             
        FXButton(p=pickHf, text='\t在视图中选择坐标系', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,        
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)                           

              
        self.form = form
        l = FXLabel(p=GroupBox_17, text='注:新零件名称将在原零件名称基础上增加后缀 \'-mesh\'.', opts=JUSTIFY_LEFT)
        GroupBox_21 = FXGroupBox(p=TabItem_4, text='单元类型', opts=FRAME_GROOVE)
        HFrame_7 = FXHorizontalFrame(p=GroupBox_21, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=HFrame_7, text='连续壳元', tgt=form.eletypeKw1, sel=1)
        FXRadioButton(p=HFrame_7, text='实体单元', tgt=form.eletypeKw1, sel=2)
        tabItem = FXTabItem(p=TabBook_1, text='铺层信息', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_2 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_2, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 7, 4, 7, 4, form.layuptableKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_CUT|AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS|AFXTable.POPUP_READ_FROM_FILE|AFXTable.POPUP_WRITE_TO_FILE)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 120)
        table.setColumnType(1, AFXTable.TEXT)
        table.setColumnWidth(2, 120)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 100)
        table.setColumnType(3, AFXTable.INT)
        table.setLeadingRowLabels('     材料	      铺层厚度  	   铺层角度')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_1, text='层间效应', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_3 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        GroupBox_7 = FXGroupBox(p=TabItem_3, text='层间参数', opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_7, text='粘接单元', tgt=form.yesnocohesiveKw, sel=0)
        self.gthick1=AFXTextField(p=GroupBox_7, ncols=10, labelText='几何厚度(mm):', tgt=form.gthickKw, sel=0)
        self.pthick1=AFXTextField(p=GroupBox_7, ncols=10, labelText='物理厚度(mm):', tgt=form.pthickKw, sel=0)
        GroupBox_22 = FXGroupBox(p=TabItem_3, text='层间材料', opts=FRAME_GROOVE)
        frame = FXHorizontalFrame(GroupBox_22, 0, 0,0,0,0, 0,0,0,0)

        # Model combo
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        #
        self.RootComboBox_5 = AFXComboBox(p=frame, ncols=0, nvis=1, text='模型:', tgt=form.modelName2Kw, sel=0)
        self.RootComboBox_5.setMaxVisible(10)

        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_5.appendItem(name)
        if not form.modelName2Kw.getValue() in names:
            form.modelName2Kw.setValue( names[0] )
        msgCount = 156
        form.modelName2Kw.setTarget(self)
        form.modelName2Kw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_5MaterialsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' % (msgCount, msgHandler) )

        # Materials combo
        #
        self.ComboBox_5 = AFXComboBox(p=frame, ncols=0, nvis=1, text='材料:', tgt=form.materialNameKw, sel=0)
        self.ComboBox_5.setMaxVisible(10)

        self.form = form
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            True, self.gthick1,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            False, self.gthick1,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            True, self.pthick1,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            False, self.pthick1,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            True, self.RootComboBox_5 ,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            False, self.RootComboBox_5 ,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            True, self.ComboBox_5 ,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            False, self.ComboBox_5 ,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):

        AFXDataDialog.show(self)

        # Register a query on parts
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelName1Kw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].parts.registerQuery(self.updateComboBox_4Parts)

        # Register a query on materials
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelName2Kw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].materials.registerQuery(self.updateComboBox_5Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):

        AFXDataDialog.hide(self)

        mdb.models[self.currentModelName].parts.unregisterQuery(self.updateComboBox_4Parts)

        mdb.models[self.currentModelName].materials.unregisterQuery(self.updateComboBox_5Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_4PartsChanged(self, sender, sel, ptr):

        self.updateComboBox_4Parts()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_4Parts(self):

        modelName = self.form.modelName1Kw.getValue()

        # Update the names in the Parts combo
        #
        self.ComboBox_4.clearItems()
        names = mdb.models[modelName].parts.keys()
        names.sort()
        for name in names:
            self.ComboBox_4.appendItem(name)
        if names:
            if not self.form.partNameKw.getValue() in names:
                self.form.partNameKw.setValue( names[0] )
        else:
            self.form.partNameKw.setValue('')

        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_5MaterialsChanged(self, sender, sel, ptr):

        self.updateComboBox_5Materials()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_5Materials(self):

        modelName = self.form.modelName2Kw.getValue()

        # Update the names in the Materials combo
        #
        self.ComboBox_5.clearItems()
        names = mdb.models[modelName].materials.keys()
        names.sort()
        for name in names:
            self.ComboBox_5.appendItem(name)
        if names:
            if not self.form.materialNameKw.getValue() in names:
                self.form.materialNameKw.setValue( names[0] )
        else:
            self.form.materialNameKw.setValue('')

        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )
#定义类

class CtestDBPickHandler(AFXProcedure):

        count = 0
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def __init__(self, form, keyword, prompt, entitiesToPick, numberToPick, label):

                self.form = form
                self.keyword = keyword
                self.prompt = prompt
                self.entitiesToPick = entitiesToPick # Enum value
                self.numberToPick = numberToPick # Enum value
                self.label = label
                self.labelText = label.getText()

                AFXProcedure.__init__(self, form.getOwner())

                CtestDBPickHandler.count += 1
                self.setModeName('CtestDBPickHandler%d' % (CtestDBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

                return  AFXPickStep(self, self.keyword, self.prompt, 
                    self.entitiesToPick, self.numberToPick, sequenceStyle=TUPLE)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):

                self.label.setText( self.labelText.replace('空', '已选取') )
                return None
