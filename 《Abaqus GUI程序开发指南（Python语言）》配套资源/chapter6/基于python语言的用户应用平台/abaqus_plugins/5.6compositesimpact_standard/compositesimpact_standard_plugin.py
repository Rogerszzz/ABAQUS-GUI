# -* - coding:UTF-8 -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
from compositesimpact_standardDB import compositesimpact_standardDB
#######################################################################
#      Class definition  ϵͳ����                                                                                           #
#      �ļ���Ϊcompositesimpact_standard_plugin.py                                                          #
#######################################################################

class compositesimpact_standard_plugin(AFXForm):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
 
        AFXForm.__init__(self, owner)

        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='compositesgeneratefunc',
            objectName='CompositesGenerateFunc', registerQuery=False)
        #ָ���ں�ִ���ļ����亯����objectNameΪ�ں˺����ļ�����methodΪ�ڲ�������

        pickedDefault = ''

        #����Ϊע�����ؼ��Ĺؼ��ֲ�����Ĭ��ֵ����ϵͳ�Զ�����
        self.lengthKw = AFXFloatKeyword(self.cmd, 'length', True, 100)
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True, 100)
        if not self.radioButtonGroups.has_key('eletype'):
            self.eletypeKw1 = AFXIntKeyword(None, 'eletypeDummy', True)
            self.eletypeKw2 = AFXStringKeyword(self.cmd, 'eletype', True)
            self.radioButtonGroups['eletype']\
                =(self.eletypeKw1, self.eletypeKw2, {})
        self.radioButtonGroups['eletype'][2][53] = 'Solid'
        if not self.radioButtonGroups.has_key('eletype'):
            self.eletypeKw1 = AFXIntKeyword(None, 'eletypeDummy', True)
            self.eletypeKw2 = AFXStringKeyword(self.cmd, 'eletype', True)
            self.radioButtonGroups['eletype']\
                =(self.eletypeKw1, self.eletypeKw2, {})
        self.radioButtonGroups['eletype'][2][54] = 'Continuum Shell'
        self.NXKw = AFXIntKeyword(self.cmd, 'NX', True, 10)
        self.NYKw = AFXIntKeyword(self.cmd, 'NY', True, 10)
        self.biasKw = AFXFloatKeyword(self.cmd, 'bias', True, 1)
        self.layuptableKw = AFXTableKeyword(self.cmd, 'layuptable', True)
        self.layuptableKw.setColumnType(0, AFXTABLE_TYPE_STRING)
        self.layuptableKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.layuptableKw.setColumnType(2, AFXTABLE_TYPE_INT)
        self.yesnocohesiveKw = AFXBoolKeyword(self.cmd, 'yesnocohesive', 
            AFXBoolKeyword.TRUE_FALSE, True, True)
        self.gthickKw = AFXFloatKeyword(self.cmd, 'gthick', True, 0.01)
        self.pthickKw = AFXFloatKeyword(self.cmd, 'pthick', True, 0.01)
        self.modelName2Kw = AFXStringKeyword(self.cmd, 'modelName2', True)
        self.materialName2Kw = AFXStringKeyword(self.cmd, 'materialName2', True)
        self.heightKw = AFXStringKeyword(self.cmd, 'height', True, '15')
        self.radiusKw = AFXStringKeyword(self.cmd, 'radius', True, '10')
        self.velocityKw = AFXFloatKeyword(self.cmd, 'velocity', True, 1000)
        self.globalsizeKw = AFXFloatKeyword(self.cmd, 'globalsize', True, 2)
        self.modelNameKw = AFXStringKeyword(self.cmd, 'modelName', True)
        self.materialNameKw = AFXStringKeyword(self.cmd, 'materialName', True)
        self.timeperiodKw = AFXFloatKeyword(self.cmd, 'timeperiod', True, 0.005)
        self.frictionKw = AFXFloatKeyword(self.cmd, 'friction', True, 0.1)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):
        #��ϵͳ�Զ�����
        import compositesimpact_standardDB
        return compositesimpact_standardDB.compositesimpact_standardDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        # ��ϵͳ�Զ�����
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass

        #���´���Ϊ�жϸ����ؼ����ݵĺϷ��ԣ��������жϽ��������Ӧ�Ĵ�����ʾ��Ϣ

        if self.lengthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'L MUST BE POSITIVE NUMBER.')
            return False
        #���峤С�ڵ���0ʱ����
        elif self.widthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'W MUST BE POSITIVE NUMBER.')
            return False
        #�����С�ڵ���0ʱ����
        elif self.radiusKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'R MUST BE POSITIVE NUMBER.')
            return False
        #����ͷ�뾶С�ڵ���0ʱ����
        elif self.heightKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'H  MUST BE POSITIVE NUMBER.')
            return False
        #����ͷ�߶�С�ڵ���0ʱ����
        elif self.NXKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT NUMBER MUST BE POSITIVE NUMBER.')
            return False
        #����������Ԫ����С�ڵ���0ʱ����
        elif self.NYKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT NUMBER MUST BE POSITIVE NUMBER.')
            return False
        #�����Ӻ���Ԫ����С�ڵ���0ʱ����
        elif self.eletypeKw1.getValue()!=53 and self.eletypeKw1.getValue()!=54:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the element type is not defined.')
            return False
        #��ѡ��ť��δѡ��Ԫ����ʱ����
        elif self.velocityKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'IMPACT VELOCITY MUST BE POSITIVE NUMBER.')
            return False
        #����ͷ����ٶ�С�ڵ���0ʱ����        
        elif self.globalsizeKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT GLOBALSIZE MUST BE POSITIVE NUMBER.')
            return False
        #����ͷ����ߴ�С�ڵ���0ʱ����
        elif self.materialNameKw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for impactor.')
            return False
        #��δѡȡ��ͷ����ʱ����
        elif self.materialName2Kw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for cohesive.')
            return False
        #��δѡȡ������ʱ����
        elif self.frictionKw.getValue()<0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'FRICTION MUST BE POSITIVE NUMBER.')
            return False
        #��Ħ��ϵ��С��0ʱ����
        elif self.biasKw.getValue()<0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'BIAS MUST BE POSITIVE NUMBER OR ZERO.')
            return False
        #���������ƫ�ö�С��0ʱ����
        elif self.timeperiodKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'TIME PERIOD MUST BE POSITIVE NUMBER.')
            return False
        #�������Ӧʱ��С�ڵ���0ʱ����
        elif self.gthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'GEOMETRY THICKNESS OF COHESIVE MUST BE POSITIVE.')
            return False
        #����伸�κ��С�ڵ���0ʱ����
        elif self.pthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'PHYSICAL THICKNESS OF COHESIVE MUST BE POSITIVE .')
            return False
        #�����������С�ڵ���0ʱ����
        elif self.layuptableKw.getValue(0,0)=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the layup material is not giving.')
            return False
        #���̲���в���δָ��ʱ����
        
        #����ʡ��
        else:
            return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):
        # ��ϵͳ�Զ�����
        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
#ָ���ļ�·��

icon_impact= afxCreateIcon( os.path.join(thisDir, 'icon_impact.png') )
#������ͼ��
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='�︴�ϲ��Ϲ��߰�|�︴�ϲ��ϳ����������Ԫģ�Ͳ�������ģ����', 
    #�������ڲ˵��е���ʾ�ı�
    object=compositesimpact_standard_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=icon_impact,
    #�������ڲ˵��е���ʾͼ��
    kernelInitString='import CompositesGenerateFunc',
    #��ʼ��ָ������ں�ִ���ļ�
    applicableModules=ALL,
    #���������õ�ģ��
    version='1.0',
    #�������汾
    author='jly',
    #ָ������
    description='�����������Ԫģ�͵���ȫ��������ģ',
    #�������
    helpUrl='N/A'
    #�����ļ�·��
)   #�����ע�ᵽ��Plug-ins���˵�

toolset.registerGuiToolButton('ע�Ṥ����', 
    object=compositesimpact_standard_plugin(toolset), 
    buttonText='\t���ϲ��ϳ����������Ԫģ�Ͳ�������ģ����',
    kernelInitString='import CompositesGenerateFunc', icon=icon_impact,
    version='1.0', 
    author='jly',
    applicableModules = ['Part', 'Property', 'Assembly', 'Step', 
        'Interaction', 'Load', 'Mesh', 'Job'],
    description='�����������Ԫģ�͵���ȫ��������ģ',
    helpUrl='N/A'
)   #�����ע�ᵽ�Զ��幤����������������Ϊ'ע�Ṥ����'