# -* - coding:UTF-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
class testProgressBarDB(AFXDataDialog):
    ID_START = AFXDataDialog.ID_LAST
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, '测试进度条',
            self.OK|self.CANCEL, DECOR_RESIZE|DIALOG_ACTIONS_SEPARATOR)
        FXButton(self, '开始读取', None, self, self.ID_START)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_START, testProgressBarDB.onDoSomething)
        self.scannerDB = ScannerDB(self)
    def onDoSomething(self, sender, sel, ptr):
        self.scannerDB.create()
        self.scannerDB.showModal(self)
        getAFXApp().repaint()
        files =[]
        for i in range(1,10000):
            files.append('file_%d.txt' % (i))
        N=len(files)
        self.scannerDB.setTotal(N)
        for i in range( 1, N+1 ):
            self.scannerDB.setProgress(i)        #实时刷新进度条显示值
        self.scannerDB.hide()
class ScannerDB(AFXDialog):
    def __init__(self, owner):
        AFXDialog.__init__(self, owner, '显示进度', 
            0, 0, DIALOG_ACTIONS_NONE)           #创建对话框
        self.scanner = AFXProgressBar(self, None, 0, 
            LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|
            FRAME_SUNKEN|FRAME_THICK|AFXPROGRESSBAR_ITERATOR, 
            0, 0, 200, 22)              #创建迭代型进度条
        self.scanner2 = AFXProgressBar(self, None, 0, 
            LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|
            FRAME_SUNKEN|FRAME_THICK|AFXPROGRESSBAR_PERCENTAGE, 
            0, 0, 200, 22)              #创建百分比型进度条
#        self.scanner3 = AFXProgressBar(self, None, 0,            
#            AFXPROGRESSBAR_SCANNER, 
#            0, 0, 200, 22)              #创建扫描型进度条
    def setTotal(self, total):
        self.scanner.setTotal(total)
        self.scanner2.setTotal(total)
        #SCANNER型进度条无需设置
    def setProgress(self, progress):
        self.scanner.setProgress(progress)
        self.scanner2.setProgress(progress)
        #SCANNER型进度条无需设置