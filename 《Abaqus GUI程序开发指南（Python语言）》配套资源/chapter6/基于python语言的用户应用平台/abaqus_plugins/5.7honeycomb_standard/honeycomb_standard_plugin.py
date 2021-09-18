#-*-coding: UTF-8-*-
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
#######################################################################
#      ���ע���ļ�                                                                                                            #
#      �ļ���Ϊ��honeycomb_standard_plugin.py                                                                #
#######################################################################
class honeycomb_standard_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}
        self.cmd = AFXGuiCommand(mode=self, method='honeycomfun',
            objectName='honeycomb_fun', registerQuery=False)
        #ָ���ں�ִ���ļ����亯����		
	
        pickedDefault = ''
        #����Ϊע�����ؼ��Ĺؼ��ֲ�����Ĭ�ϳ�ֵ		
        if not self.radioButtonGroups.has_key('celldimention'):
            self.celldimentionKw1 = AFXIntKeyword(None, 'celldimentionDummy', True)
            self.celldimentionKw2 = AFXStringKeyword(self.cmd, 'celldimention', True)
            self.radioButtonGroups['celldimention'] = (self.celldimentionKw1, 
                 self.celldimentionKw2, {})
        self.radioButtonGroups['celldimention'][2][1] = 'Length:'
        self.celldimentionKw1.setValue(1)
        if not self.radioButtonGroups.has_key('celldimention'):
            self.celldimentionKw1 = AFXIntKeyword(None, 'celldimentionDummy', True)
            self.celldimentionKw2 = AFXStringKeyword(self.cmd, 'celldimention', True)
            self.radioButtonGroups['celldimention'] = (self.celldimentionKw1, 
                 self.celldimentionKw2, {})
        self.radioButtonGroups['celldimention'][2][2] = 'Diameter:'
        self.celllengthKw = AFXFloatKeyword(self.cmd, 'celllength', True, 1.8)
        self.celldiameterKw = AFXFloatKeyword(self.cmd, 'celldiameter', True, 3.2)
        self.thicknessKw = AFXFloatKeyword(self.cmd, 'thickness', True, 0.05)
        self.panellengthKw = AFXFloatKeyword(self.cmd, 'panellength', True, 20)
        self.panelwidthKw = AFXFloatKeyword(self.cmd, 'panelwidth', True, 20)
        self.panelheightKw = AFXFloatKeyword(self.cmd, 'panelheight', True, 20)
        self.modelNameKw = AFXStringKeyword(self.cmd, 'modelName', True)
        self.materialNameKw = AFXStringKeyword(self.cmd, 'materialName', True)
        self.partNameKw = AFXStringKeyword(self.cmd, 'partName', True, 'honeycomb')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import honeycomb_standardDB
        return honeycomb_standardDB.honeycomb_standardDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        # ���´���Ϊ�ж����ݵĺϷ���
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        if self.materialNameKw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for impactor.')
            return False
        else:
            return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
icon_honeycomb = afxCreateIcon( os.path.join(thisDir, 'icon.png') )
#����ͼ��
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
#�����ע�ᵽ��Plug-ins���˵�
toolset.registerGuiMenuButton(
    buttonText='�︴�ϲ��Ϲ��߰�|�������η����Զ���ģ����', 
    #�������ڲ˵��е���ʾ�ı�	
    object=honeycomb_standard_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=icon_honeycomb ,
    #�������ڲ˵��е���ʾͼ��	
    kernelInitString='import honeycomb_fun',
    applicableModules=ALL,
    version='1.0',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)  

