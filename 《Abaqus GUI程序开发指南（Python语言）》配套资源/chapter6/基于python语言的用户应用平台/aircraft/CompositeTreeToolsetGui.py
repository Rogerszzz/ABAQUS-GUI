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
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1)            #����ID
    def makeTabs(self):
#        self.makeModelTab()                          #��ʾģ�����б�
#        self.makeMaterialLibraryTab()                #��ʾ���Ͽ��б�
#        self.makeResultsTab()                        #��ʾ������б�
        self.makeMyTab()                              #��ʾ�Զ������б�
    def makeMyTab(self):

        vf = getAFXApp().getAFXMainWindow().appendTreeTab('���ϲ���','Composites')
        #���������������������ǩ������Ϊ'���ϲ���'
        getAFXApp().getAFXMainWindow().setApplicabilityForTreeTab(
            'Composites', 'Part, Property,Composites')
        getAFXApp().getAFXMainWindow().setVisibilityForTreeTab(
            'Composites', 'Part, Property,Composites')
        #�������ι��߰���'Part, Property,Composites'����ģ���п���
        FXLabel(vf, 'This is my tab')
        #������ʾ��ǩ
        self.tree = FXTreeList(vf, 10, tgt=self, sel=self.ID_CLICKED, 
            opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|
            TREELIST_SHOWS_BOXES|TREELIST_ROOT_BOXES|
            TREELIST_SHOWS_LINES|LAYOUT_FIX_WIDTH,     
            x=0, y=0, w=120, h=0)                                
        #
        #�������б�ָ����Ŀ����ID
        FXMAPFUNC(self, SEL_DOUBLECLICKED, self.ID_CLICKED, 
            CompositeTreeToolsetGui.onCmdTree)
        #��Ϣӳ�䣺ָ����������˫�������б���Ŀʱ�Ķ���
        #
        Icon1 =afxCreateIcon(r"icon\ico1.png")           #����ͼ��
        Icon2 =afxCreateIcon(r"icon\ico2.png")           #����ͼ��  
        Icon3 =afxCreateIcon(r"icon\impact_icon.png")    #����ͼ��  
        Icon4 =afxCreateIcon(r"icon\overstrething_icon.png")   #����ͼ�� 
        Icon5 =afxCreateIcon(r"icon\honeycomb_icon.png")       #����ͼ�� 
        option1 = self.tree.addItemLast(None, 'Option 1')      
        #���б������һ����Ŀ       
        self.tree.addItemLast(option1, 'Option 1a',oi=Icon1,ci=Icon2)     
        #�����б�һ����Ŀ����Ӷ�������Ŀ����ָ����ѡ��ǰ���ͼ�� 
        self.tree.addItemLast(option1, 'Option 1b')  
        #ͬ��
        option2 = self.tree.addItemLast(None, 'Option 2') 
        #���б������һ����Ŀ               
        option2a = self.tree.addItemLast(option2, 'Option 2a') 
        #�����б�һ����Ŀ����Ӷ�������Ŀ��                         
        option2b = self.tree.addItemLast(option2, 'Option 2b')
        #�����б�һ����Ŀ����Ӷ�������Ŀ��
        self.tree.addItemLast(option2b, 'Option 2bi')   
        #�����б������Ŀ�������������Ŀ��                       
        option3 = self.tree.addItemLast(None, 'Option 3',oi=Icon3,ci=Icon3)
        #���б������һ����Ŀ
        self.IMPACT = impactForm(self)
        #ʵ�����������һ
        option4 = self.tree.addItemLast(None, 'Option 4',oi=Icon4,ci=Icon4) 
        #���б������һ����Ŀ 
        self.OVERSTRETHING = overstrethingForm(self)
        #ʵ�������������
        option5 = self.tree.addItemLast(None, 'Option 5',oi=Icon5,ci=Icon5) 
        #���б������һ����Ŀ  
        self.HONEYCOMB = honeycombForm(self) 
        #ʵ�������������
#
#***********************************************************************
    #����˫�������б�ʱ�Ķ���
    def onCmdTree(self, sender, sel, ptr):                           
        w = self.tree.getFirstItem()               #��ȡ��һ��
        while(w):
            if self.tree.isItemSelected(w):        #�ж��Ƿ�ѡ��
                item=self.tree.getCurrentItem()    #��ȡ��ǰ��ѡ�� 
                text=self.tree.getItemText(item)   #��ȡ��ǰѡ���ı�
                print '%s was selected.' % text    #��DOS���������ʾ��
                if text=='Option 3':
                    impactForm.activate(self.IMPACT)
                #��������˫��'Option 3'ʱ������impactForm����
                if text=='Option 4':
                    overstrethingForm.activate(self.OVERSTRETHING)
                #��������˫��'Option 4'ʱ������overstrethingForm����
                if text=='Option 5':
                    honeycombForm.activate(self.HONEYCOMB)
                #��������˫��'Option 4'ʱ������overstrethingForm����
                break
            if w.getFirst():
                w=w.getFirst()
                #��ȡ��һ������Ŀ
                continue
                #����ѭ��
            while not w.getNext() and w.getParent():
                 w=w.getParent()
                 #������û��ͬ����Ŀʱ�����ȡ�丸����Ŀ
            w=w.getNext()
            #��ȡ��һ����Ŀ