#!/usr/bin/python
#-*-coding: UTF-8-*-
#-*-coding: mbcs -*- 
from abaqusGui import * 
from toolset2.impact.impactForm import impactForm 
from aircraft.honeycombForm import honeycombForm
from aircraft.overstrethingForm import overstrethingForm
class CompositeTreeToolsetGui(TreeToolsetGui):
    [                                             
        ID_CLICKED                              
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1)            #分配ID
    def makeTabs(self):
#        self.makeModelTab()                          #显示模型树列表
#        self.makeMaterialLibraryTab()                #显示材料库列表
#        self.makeResultsTab()                        #显示结果树列表
        self.makeMyTab()                              #显示自定义树列表
    def makeMyTab(self):

        vf = getAFXApp().getAFXMainWindow().appendTreeTab('复合材料','Composites')
        #在主窗口左侧新增分栏标签，命名为'复合材料'
        getAFXApp().getAFXMainWindow().setApplicabilityForTreeTab(
            'Composites', 'Part, Property,Composites')
        getAFXApp().getAFXMainWindow().setVisibilityForTreeTab(
            'Composites', 'Part, Property,Composites')
        #设置树形工具包在'Part, Property,Composites'三个模块中可用
        FXLabel(vf, 'This is my tab')
        #新增提示标签
        self.tree = FXTreeList(vf, 10, tgt=self, sel=self.ID_CLICKED, 
            opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|
            TREELIST_SHOWS_BOXES|TREELIST_ROOT_BOXES|
            TREELIST_SHOWS_LINES|LAYOUT_FIX_WIDTH,     
            x=0, y=0, w=120, h=0)                                
        #
        #定义树列表，指定其目标与ID
        FXMAPFUNC(self, SEL_DOUBLECLICKED, self.ID_CLICKED, 
            CompositeTreeToolsetGui.onCmdTree)
        #消息映射：指定当鼠标左键双击树形列表项目时的动作
        #
        Icon1 =afxCreateIcon(r"icon\ico1.png")           #定义图标
        Icon2 =afxCreateIcon(r"icon\ico2.png")           #定义图标  
        Icon3 =afxCreateIcon(r"icon\impact_icon.png")    #定义图标  
        Icon4 =afxCreateIcon(r"icon\overstrething_icon.png")   #定义图标 
        Icon5 =afxCreateIcon(r"icon\honeycomb_icon.png")       #定义图标 
        option1 = self.tree.addItemLast(None, 'Option 1')      
        #树列表中添加一级项目       
        self.tree.addItemLast(option1, 'Option 1a',oi=Icon1,ci=Icon2)     
        #在树列表一级项目中添加二级子项目，并指定其选中前后的图标 
        self.tree.addItemLast(option1, 'Option 1b')  
        #同上
        option2 = self.tree.addItemLast(None, 'Option 2') 
        #树列表中添加一级项目               
        option2a = self.tree.addItemLast(option2, 'Option 2a') 
        #在树列表一级项目中添加二级子项目，                         
        option2b = self.tree.addItemLast(option2, 'Option 2b')
        #在树列表一级项目中添加二级子项目，
        self.tree.addItemLast(option2b, 'Option 2bi')   
        #在树列表二级项目中添加三级子项目，                       
        option3 = self.tree.addItemLast(None, 'Option 3',oi=Icon3,ci=Icon3)
        #树列表中添加一级项目
        self.IMPACT = impactForm(self)
        #实例化功能组件一
        option4 = self.tree.addItemLast(None, 'Option 4',oi=Icon4,ci=Icon4) 
        #树列表中添加一级项目 
        self.OVERSTRETHING = overstrethingForm(self)
        #实例化功能组件二
        option5 = self.tree.addItemLast(None, 'Option 5',oi=Icon5,ci=Icon5) 
        #树列表中添加一级项目  
        self.HONEYCOMB = honeycombForm(self) 
        #实例化功能组件三
#
#***********************************************************************
    #定义双击树形列表时的动作
    def onCmdTree(self, sender, sel, ptr):                           
        w = self.tree.getFirstItem()               #获取第一项
        while(w):
            if self.tree.isItemSelected(w):        #判断是否被选择
                item=self.tree.getCurrentItem()    #获取当前所选项 
                text=self.tree.getItemText(item)   #获取当前选项文本
                print '%s was selected.' % text    #在DOS窗口输出提示语
                if text=='Option 3':
                    impactForm.activate(self.IMPACT)
                #当鼠标左键双击'Option 3'时，调用impactForm程序
                if text=='Option 4':
                    overstrethingForm.activate(self.OVERSTRETHING)
                #当鼠标左键双击'Option 4'时，调用overstrethingForm程序
                if text=='Option 5':
                    honeycombForm.activate(self.HONEYCOMB)
                #当鼠标左键双击'Option 4'时，调用overstrethingForm程序
                break
            if w.getFirst():
                w=w.getFirst()
                #获取第一个子项目
                continue
                #继续循环
            while not w.getNext() and w.getParent():
                 w=w.getParent()
                 #当后面没有同级项目时，则获取其父级项目
            w=w.getNext()
            #获取下一个项目