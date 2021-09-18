# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testcomboboxDB(AFXDataDialog):
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, '测试下拉框',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
        frame = FXHorizontalFrame(self, 0, 0,0,0,0, 0,0,0,0)
        #系统自动创建MDB repository类型下拉框，父级对象为model
        self.RootComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Model:', tgt=form.modelNameKw, sel=0)
        self.RootComboBox_1.setMaxVisible(10)
        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_1.appendItem(name)
        if not form.modelNameKw.getValue() in names:
            form.modelNameKw.setValue( names[0] )
        msgCount = 7
        form.modelNameKw.setTarget(self)
        form.modelNameKw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_1PartsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)'
             % (msgCount, msgHandler) )
        # 系统自动创建MDB repository类型下拉框，子对象为part
        self.ComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Part:', 
            tgt=form.partNameKw, sel=0)
        self.ComboBox_1.setMaxVisible(10)
        self.form = form
        #系统自动生成的标准型下拉框，对象为空
        self.ComboBox_2 = AFXComboBox(p=self, ncols=0, nvis=1, text='set:', 
            tgt=form.elesetKw, sel=0)
        self.ComboBox_2.setMaxVisible(10)
        #新增代码，创建单元集合下拉框
        msgCount4 = 45
        form.partNameKw.setTarget(self)    #设置目标
        form.partNameKw.setSelector(AFXDataDialog.ID_LAST+msgCount4)  #设置消息ID
        msgHandler4 = str(self.__class__).split('.')[-1] + '.onComboBox_2elesetChanged'           
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' 
            % (msgCount4, msgHandler4) ) 
        #消息映射
    def show(self):

        AFXDataDialog.show(self)
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelNameKw.setValue(self.currentModelName)
        mdb.models[self.currentModelName].parts.registerQuery(self.updateComboBox_1Parts)
        mdb.models[self.currentModelName].parts.registerQuery(self.updateComboBox_2eleset)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):

        AFXDataDialog.hide(self)

        mdb.models[self.currentModelName].parts.unregisterQuery(self.updateComboBox_1Parts)
        mdb.models[self.currentModelName].parts.unregisterQuery(self.updateComboBox_2eleset)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_1PartsChanged(self, sender, sel, ptr):

        self.updateComboBox_1Parts()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_1Parts(self):

        modelName = self.form.modelNameKw.getValue()

        # Update the names in the Parts combo
        #
        self.ComboBox_1.clearItems()
        names = mdb.models[modelName].parts.keys()
        names.sort()
        for name in names:
            self.ComboBox_1.appendItem(name)
        if names:
            if not self.form.partNameKw.getValue() in names:
                self.form.partNameKw.setValue( names[0] )
        else:
            self.form.partNameKw.setValue('')

        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )
    #新增sets更新
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_2elesetChanged(self, sender, sel, ptr):    #自定义下拉框函数

        self.updateComboBox_2eleset()
        return 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_2eleset(self):                    #更新下拉框内容

        modelName = self.form.modelNameKw.getValue()
        partName = self.form.partNameKw.getValue()
        # Update the names in the Parts combo

        if partName!='':    #判断是否有part，避免在无零件时报错
            self.ComboBox_2.clearItems()
            names = mdb.models[modelName].parts[partName].sets.keys()#指向零件的所有集合
            names.sort()
            for name in names:
                self.ComboBox_2.appendItem(name)                 #逐项添加到下拉框中
            if names:
                if not self.form.elesetKw.getValue() in names:
                    self.form.elesetKw.setValue( names[0] )
            else:
                self.form.elesetKw.setValue('')
            
        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )

