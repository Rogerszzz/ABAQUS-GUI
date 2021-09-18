# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testcomboboxDB(AFXDataDialog):
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, '����������',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
        frame = FXHorizontalFrame(self, 0, 0,0,0,0, 0,0,0,0)
        #ϵͳ�Զ�����MDB repository���������򣬸�������Ϊmodel
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
        # ϵͳ�Զ�����MDB repository�����������Ӷ���Ϊpart
        self.ComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Part:', 
            tgt=form.partNameKw, sel=0)
        self.ComboBox_1.setMaxVisible(10)
        self.form = form
        #ϵͳ�Զ����ɵı�׼�������򣬶���Ϊ��
        self.ComboBox_2 = AFXComboBox(p=self, ncols=0, nvis=1, text='set:', 
            tgt=form.elesetKw, sel=0)
        self.ComboBox_2.setMaxVisible(10)
        #�������룬������Ԫ����������
        msgCount4 = 45
        form.partNameKw.setTarget(self)    #����Ŀ��
        form.partNameKw.setSelector(AFXDataDialog.ID_LAST+msgCount4)  #������ϢID
        msgHandler4 = str(self.__class__).split('.')[-1] + '.onComboBox_2elesetChanged'           
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' 
            % (msgCount4, msgHandler4) ) 
        #��Ϣӳ��
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
    #����sets����
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_2elesetChanged(self, sender, sel, ptr):    #�Զ�����������

        self.updateComboBox_2eleset()
        return 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_2eleset(self):                    #��������������

        modelName = self.form.modelNameKw.getValue()
        partName = self.form.partNameKw.getValue()
        # Update the names in the Parts combo

        if partName!='':    #�ж��Ƿ���part�������������ʱ����
            self.ComboBox_2.clearItems()
            names = mdb.models[modelName].parts[partName].sets.keys()#ָ����������м���
            names.sort()
            for name in names:
                self.ComboBox_2.appendItem(name)                 #������ӵ���������
            if names:
                if not self.form.elesetKw.getValue() in names:
                    self.form.elesetKw.setValue( names[0] )
            else:
                self.form.elesetKw.setValue('')
            
        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )

