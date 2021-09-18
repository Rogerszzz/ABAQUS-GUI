# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

###########################################################################
# Class definition 
#在RSG编辑界面保存后，图形界面文件由系统自动生成，基本无需修改。
###########################################################################

class compositesimpact_standardDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

         
        # Construct the base class.
        # 由系统生成，构造基础类

        AFXDataDialog.__init__(self, form, 'Composites Impact Model Creator',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
        #初始化对话框    

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
        #定义OK按键
            
        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
        #定义Apply按键
        
        GroupBox_3 = FXGroupBox(p=self, text='Composites Plate Parameters', 
            opts=FRAME_GROOVE)
        TabBook_1 = FXTabBook(p=GroupBox_3, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_1, text='Geometry Parameters', 
            ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_1 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, 
            vs=DEFAULT_SPACING)
        HFrame_3 = FXHorizontalFrame(p=TabItem_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_9 = FXGroupBox(p=HFrame_3, text='Geometry Parameters', 
            opts=FRAME_GROOVE)
        GroupBox_8 = FXGroupBox(p=GroupBox_9, text='Diagram', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, r'plate.png')
        icon = afxCreatePNGIcon(fileName)
        #定义板子示意图
        FXLabel(p=GroupBox_8, text='', ic=icon)
        AFXTextField(p=GroupBox_9, ncols=8, labelText='Length(L/mm):',
            tgt=form.lengthKw, sel=0)
        #定义文本框
        AFXTextField(p=GroupBox_9, ncols=8, labelText='Width (W/mm):',
            tgt=form.widthKw, sel=0)
        GroupBox_10 = FXGroupBox(p=HFrame_3, text=' Element Control', 
            opts=FRAME_GROOVE)
        GroupBox_12 = FXGroupBox(p=GroupBox_10, text='Element Type', 
            opts=FRAME_GROOVE)
        HFrame_5 = FXHorizontalFrame(p=GroupBox_12, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=HFrame_5, text='Solid', tgt=form.eletypeKw1, sel=53)
        FXRadioButton(p=HFrame_5, text='Continuum Shell', 
            tgt=form.eletypeKw1, sel=54)
        #定义一组单选按钮
        GroupBox_11 = FXGroupBox(p=GroupBox_10, text='Seeds Contrl', 
            opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_11, ncols=7, labelText='Elements Number(L):', 
            tgt=form.NXKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=7, labelText='Elements Number(W):', 
            tgt=form.NYKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=6, labelText='Bias:', 
            tgt=form.biasKw, sel=0)
        tabItem = FXTabItem(p=TabBook_1, text='Layup Parameters', 
            ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_2 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, 
            vs=DEFAULT_SPACING)
        vf = FXVerticalFrame(TabItem_2, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #   colored differently from its parent when the 'Color layout managers'
        #   button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 8, 4, 8, 4, form.layuptableKw, 0, 
            AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        #定义铺层信息表
        table.setPopupOptions(AFXTable.POPUP_CUT|AFXTable.POPUP_COPY\
            |AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW\
            |AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS\
            |AFXTable.POPUP_READ_FROM_FILE|AFXTable.POPUP_WRITE_TO_FILE)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 120)
        table.setColumnType(1, AFXTable.TEXT)
        table.setColumnWidth(2, 120)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 100)
        table.setColumnType(3, AFXTable.INT)
        table.setLeadingRowLabels('Material\tPly\nThickness\tRotation\nangle')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        table.setColumnJustify(1, table.CENTER)
        table.setColumnJustify(2, table.CENTER)
        table.setColumnJustify(3, table.CENTER)
        #定义表格属性
        
        listId = table.addList('45\t90\t-45\t0')
        table.setColumnType(3, AFXTable.LIST)
        table.setColumnListId(3, listId)
        #将表格第三列设置为列表属性，列表值有45,90,-45,0

        tabItem = FXTabItem(p=TabBook_1, text='Interlaminar Effect', 
            ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_3 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, 
            vs=DEFAULT_SPACING)
        GroupBox_7 = FXGroupBox(p=TabItem_3, text='Cohesive Parameters', 
            opts=FRAME_GROOVE)
        FXCheckButton(p=GroupBox_7, text='Cohesive Element', 
            tgt=form.yesnocohesiveKw, sel=0)
        #定义复选框
        AFXTextField(p=GroupBox_7, ncols=10, 
            labelText='Geometry Thickness(mm):', tgt=form.gthickKw, sel=0)
        AFXTextField(p=GroupBox_7, ncols=10, 
            labelText='Physical Thickness(mm):', tgt=form.pthickKw, sel=0)
        frame = FXHorizontalFrame(GroupBox_7, 0, 0,0,0,0, 0,0,0,0)

        # Model combo 模型选择下拉框，由系统生成
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.

        self.RootComboBox_4 = AFXComboBox(p=frame, ncols=0, nvis=1, 
            text='Model:', tgt=form.modelName2Kw, sel=0)
        self.RootComboBox_4.setMaxVisible(10)
        #设置下拉框属性
        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_4.appendItem(name)
        if not form.modelName2Kw.getValue() in names:
            form.modelName2Kw.setValue( names[0] )
        msgCount = 39
        form.modelName2Kw.setTarget(self)
        form.modelName2Kw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] \
            +'.onComboBox_4MaterialsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)'\
             % (msgCount, msgHandler) )
       
        # Materials combo材料选择下拉框，由系统生成
        #
        self.ComboBox_4 = AFXComboBox(p=frame, ncols=0, nvis=1, 
            text='  Material:', tgt=form.materialName2Kw, sel=0)
        self.ComboBox_4.setMaxVisible(10)
        # 定义一个MDB repository型下拉框，由系统生成
        self.form = form
        l=FXLabel(p=GroupBox_7,text='note:Physical thickness couldn\'t be zero.',
            opts=JUSTIFY_LEFT)
        GroupBox_5=FXGroupBox(p=self,text='Impactor Parameters',opts=FRAME_GROOVE)
        HFrame_2 = FXHorizontalFrame(p=GroupBox_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_6 = FXGroupBox(p=HFrame_2, text='Diagram', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, r'impactor.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_6, text='', ic=icon)
        #定义冲头示意图
        
        GroupBox_14 = FXGroupBox(p=HFrame_2, text='Parameters', opts=FRAME_GROOVE)
        HFrame_6 = FXHorizontalFrame(p=GroupBox_14, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        frame = FXHorizontalFrame(HFrame_6, 0, 0,0,0,0, 0,0,0,0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='Impactor Height (H/mm):',
            tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='Impactor Radius (R/mm):', 
            tgt=form.radiusKw, sel=0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='Impact Velocity (mm/s):', 
            tgt=form.velocityKw, sel=0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='Global Mesh Size  (mm):', 
            tgt=form.globalsizeKw, sel=0)
        #定义一系列文本框
        frame = FXHorizontalFrame(GroupBox_14, 0, 0,0,0,0, 0,0,0,0)

        # Model combo   
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        # 同上，由系统生成
        self.RootComboBox_3 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Model:', 
            tgt=form.modelNameKw, sel=0)
        self.RootComboBox_3.setMaxVisible(10)

        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_3.appendItem(name)
        if not form.modelNameKw.getValue() in names:
            form.modelNameKw.setValue( names[0] )
        msgCount = 40
        form.modelNameKw.setTarget(self)
        form.modelNameKw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + \
            '.onComboBox_3MaterialsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)'\
            % (msgCount, msgHandler) )

        # Materials combo
        # 同上，由系统生成
        self.ComboBox_3 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Material:', 
            tgt=form.materialNameKw, sel=0)
        self.ComboBox_3.setMaxVisible(10)
        self.form = form
        GroupBox_15 = FXGroupBox(p=self, text='Step', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_15, ncols=10, labelText='Time Period(s):', 
            tgt=form.timeperiodKw, sel=0)
        GroupBox_13 = FXGroupBox(p=self, text='Contact', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_13, ncols=10, labelText='Friction  Coef:', 
            tgt=form.frictionKw, sel=0)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):
        # 由系统生成
        AFXDataDialog.show(self)

        # Register a query on materials
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelName2Kw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].materials.registerQuery(\
            self.updateComboBox_4Materials)

        # Register a query on materials
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelNameKw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].materials.registerQuery(\
            self.updateComboBox_3Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):
        # 由系统生成
        AFXDataDialog.hide(self)

        mdb.models[self.currentModelName].materials.unregisterQuery(\
            self.updateComboBox_4Materials)

        mdb.models[self.currentModelName].materials.unregisterQuery(\
            self.updateComboBox_3Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_4MaterialsChanged(self, sender, sel, ptr):
        # 由系统生成
        self.updateComboBox_4Materials()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_4Materials(self):
        # 由系统生成
        modelName = self.form.modelName2Kw.getValue()

        # Update the names in the Materials combo
        #
        self.ComboBox_4.clearItems()
        names = mdb.models[modelName].materials.keys()
        names.sort()
        for name in names:
            self.ComboBox_4.appendItem(name)
        if names:
            if not self.form.materialName2Kw.getValue() in names:
                self.form.materialName2Kw.setValue( names[0] )
        else:
            self.form.materialName2Kw.setValue('')
        
        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_3MaterialsChanged(self, sender, sel, ptr):
        # 由系统生成
        self.updateComboBox_3Materials()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_3Materials(self):
        # 由系统生成
        modelName = self.form.modelNameKw.getValue()

        # Update the names in the Materials combo
        #
        self.ComboBox_3.clearItems()
        names = mdb.models[modelName].materials.keys()
        names.sort()
        for name in names:
            self.ComboBox_3.appendItem(name)
        if names:
            if not self.form.materialNameKw.getValue() in names:
                self.form.materialNameKw.setValue( names[0] )
        else:
            self.form.materialNameKw.setValue('')

        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )