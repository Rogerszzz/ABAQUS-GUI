# -* - coding:UTF-8 -*- 
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session

import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class impactDB(AFXDataDialog):
    [                                             
        ID_MY_BUTTON,                               
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1) 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

         
        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, '复合材料层压板冲击损伤自动建模程序',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('确定')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('应用')
        
        cancelBtn = self.getActionButton(self.ID_CLICKED_CANCEL)
        cancelBtn.setText('取消')

        
        FXMAPFUNC(self, SEL_RIGHTBUTTONPRESS, self.ID_MY_BUTTON, impactDB.onCmdMyBtn)     

        GroupBox_3 = FXGroupBox(p=self, text='复合材料板参数', opts=FRAME_GROOVE)
        TabBook_1 = FXTabBook(p=GroupBox_3, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_1, text='几何参数', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_1 = FXVerticalFrame(p=TabBook_1,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_3 = FXHorizontalFrame(p=TabItem_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_9 = FXGroupBox(p=HFrame_3, text='', opts=FRAME_GROOVE)
        GroupBox_8 = FXGroupBox(p=GroupBox_9, text='图示', opts=FRAME_GROOVE)
        icon = afxCreatePNGIcon(r"icon\impact_PLATE.png")
        FXLabel(p=GroupBox_8, text='', ic=icon)
        AFXTextField(p=GroupBox_9, ncols=8, labelText='长度(L/mm):', tgt=form.lengthKw, sel=0)
        AFXTextField(p=GroupBox_9, ncols=8, labelText='宽度(W/mm):', tgt=form.widthKw, sel=0)
        GroupBox_10 = FXGroupBox(p=HFrame_3, text='', opts=FRAME_GROOVE)
        GroupBox_12 = FXGroupBox(p=GroupBox_10, text='单元类型', opts=FRAME_GROOVE)
        HFrame_5 = FXHorizontalFrame(p=GroupBox_12, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=HFrame_5, text='实体单元', tgt=form.eletypeKw1, sel=53)
        FXRadioButton(p=HFrame_5, text='连续壳元', tgt=form.eletypeKw1, sel=54)
        GroupBox_11 = FXGroupBox(p=GroupBox_10, text='种子布置', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_11, ncols=7, labelText='L方向单元数量:', tgt=form.NXKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=7, labelText='W方向单元数量:', tgt=form.NYKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=6, labelText='偏置度:', tgt=form.biasKw, sel=0)
        tabItem = FXTabItem(p=TabBook_1, text='铺层参数', ic=None, opts=TAB_TOP_NORMAL,
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
        table = AFXTable(vf, 8, 4, 8, 4, form.layuptableKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_ALL)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 120)
        table.setColumnType(1, AFXTable.TEXT)
        table.setColumnWidth(2, 120)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 100)
        table.setColumnType(3, AFXTable.INT)
        table.setLeadingRowLabels('铺层材料\t铺层厚度\t铺层角度')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        table.setColumnJustify(1, table.CENTER)
        table.setColumnJustify(2, table.CENTER)
        table.setColumnJustify(3, table.CENTER)
        listId = table.addList('45\t90\t-45\t0')
        table.setColumnType(3, AFXTable.LIST)
        table.setColumnListId(3, listId)
    
    
        

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
        frame = FXHorizontalFrame(GroupBox_7, 0, 0,0,0,0, 0,0,0,0)

        # Model combo
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        #
        self.RootComboBox_4 = AFXComboBox(p=frame, ncols=0, nvis=1, text='模型:', tgt=form.modelName2Kw, sel=0)
        self.RootComboBox_4.setMaxVisible(10)

        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_4.appendItem(name)
        if not form.modelName2Kw.getValue() in names:
            form.modelName2Kw.setValue( names[0] )
        msgCount = 39
        form.modelName2Kw.setTarget(self)
        form.modelName2Kw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_4MaterialsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' % (msgCount, msgHandler) )

       
        # Materials combo
        #
        self.ComboBox_4 = AFXComboBox(p=frame, ncols=0, nvis=1, text='材料:', tgt=form.materialName2Kw, sel=0)
        self.ComboBox_4.setMaxVisible(10)

        self.form = form
        l = FXLabel(p=GroupBox_7, text='note：The Physical Thickness could n\'t be zero.', opts=JUSTIFY_LEFT)
        ll = FXLabel(p=GroupBox_7, text='注：物理厚度不能为0', opts=JUSTIFY_LEFT)
#控制控件的可用状态
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
            True, self.RootComboBox_4 ,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            False, self.RootComboBox_4 ,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            True, self.ComboBox_4 ,
            MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), None)
        self.addTransition(form.yesnocohesiveKw, AFXTransition.EQ,
            False, self.ComboBox_4 ,
            MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), None)


        GroupBox_5 = FXGroupBox(p=self, text='冲头参数', opts=FRAME_GROOVE)
        HFrame_2 = FXHorizontalFrame(p=GroupBox_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_6 = FXGroupBox(p=HFrame_2, text='图示', opts=FRAME_GROOVE)
        icon = afxCreatePNGIcon(r"icon\impactor.png")
        FXLabel(p=GroupBox_6, text='', ic=icon)
        
        GroupBox_14 = FXGroupBox(p=HFrame_2, text='参数', opts=FRAME_GROOVE)
        HFrame_6 = FXHorizontalFrame(p=GroupBox_14, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        frame = FXHorizontalFrame(HFrame_6, 0, 0,0,0,0, 0,0,0,0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='冲头高度  (H/mm):     ', tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='冲头半径  (R/mm):     ', tgt=form.radiusKw, sel=0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='冲头速度  (mm/s):     ', tgt=form.velocityKw, sel=0)
        AFXTextField(p=GroupBox_14, ncols=10, labelText='全局网格尺寸(mm):     ', tgt=form.globalsizeKw, sel=0)
        frame = FXHorizontalFrame(GroupBox_14, 0, 0,0,0,0, 0,0,0,0)

        # Model combo
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        #
        self.RootComboBox_3 = AFXComboBox(p=frame, ncols=0, nvis=1, text='模型:', tgt=form.modelNameKw, sel=0)
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
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_3MaterialsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' % (msgCount, msgHandler) )

        # Materials combo
        #
        self.ComboBox_3 = AFXComboBox(p=frame, ncols=0, nvis=1, text='材料:', tgt=form.materialNameKw, sel=0)
        self.ComboBox_3.setMaxVisible(10)
#        FXButton(p=HFrame_6, text='Creat', ic=None, tgt=None, sel=0)
        self.form = form
        GroupBox_15 = FXGroupBox(p=self, text='分析步', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_15, ncols=10, labelText='总计算时间(s):', tgt=form.timeperiodKw, sel=0)
        GroupBox_13 = FXGroupBox(p=self, text='接触参数', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_13, ncols=10, labelText='摩擦系数:', tgt=form.frictionKw, sel=0)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):

        AFXDataDialog.show(self)

        # Register a query on materials
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelName2Kw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].materials.registerQuery(self.updateComboBox_4Materials)

        # Register a query on materials
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelNameKw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].materials.registerQuery(self.updateComboBox_3Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):

        AFXDataDialog.hide(self)

        mdb.models[self.currentModelName].materials.unregisterQuery(self.updateComboBox_4Materials)

        mdb.models[self.currentModelName].materials.unregisterQuery(self.updateComboBox_3Materials)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_4MaterialsChanged(self, sender, sel, ptr):

        self.updateComboBox_4Materials()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_4Materials(self):

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

        self.updateComboBox_3Materials()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_3Materials(self):

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

    def  onCmdMyBtn(self, sender, sel, ptr):      
                                                   
        if SELID(sel) ==  self.ID_MY_BUTTON:
            print 'Button 1 was pressed.'
            modelName = self.form.modelName2Kw.getValue()
            print modelName
#            pythonfile = os.path.join(thisDir, r'impactKernel.py')
#           execfile(pythonfile)
            
              
    



