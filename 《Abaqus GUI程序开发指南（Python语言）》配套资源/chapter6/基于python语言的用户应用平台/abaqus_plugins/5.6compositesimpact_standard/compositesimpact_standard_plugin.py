# -* - coding:UTF-8 -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
from compositesimpact_standardDB import compositesimpact_standardDB
#######################################################################
#      Class definition  系统生成                                                                                           #
#      文件名为compositesimpact_standard_plugin.py                                                          #
#######################################################################

class compositesimpact_standard_plugin(AFXForm):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
 
        AFXForm.__init__(self, owner)

        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='compositesgeneratefunc',
            objectName='CompositesGenerateFunc', registerQuery=False)
        #指向内核执行文件及其函数，objectName为内核函数文件名，method为内部函数名

        pickedDefault = ''

        #以下为注册各类控件的关键字并设置默认值，由系统自动生成
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
        #由系统自动生成
        import compositesimpact_standardDB
        return compositesimpact_standardDB.compositesimpact_standardDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        # 由系统自动生成
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass

        #以下代码为判断各个控件数据的合法性，并根据判断结果给出对应的错误提示信息

        if self.lengthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'L MUST BE POSITIVE NUMBER.')
            return False
        #当板长小于等于0时报错
        elif self.widthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'W MUST BE POSITIVE NUMBER.')
            return False
        #当板宽小于等于0时报错
        elif self.radiusKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'R MUST BE POSITIVE NUMBER.')
            return False
        #当冲头半径小于等于0时报错
        elif self.heightKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'H  MUST BE POSITIVE NUMBER.')
            return False
        #当冲头高度小于等于0时报错
        elif self.NXKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT NUMBER MUST BE POSITIVE NUMBER.')
            return False
        #当板子纵向单元数量小于等于0时报错
        elif self.NYKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT NUMBER MUST BE POSITIVE NUMBER.')
            return False
        #当板子横向单元数量小于等于0时报错
        elif self.eletypeKw1.getValue()!=53 and self.eletypeKw1.getValue()!=54:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the element type is not defined.')
            return False
        #单选按钮：未选择单元类型时报错
        elif self.velocityKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'IMPACT VELOCITY MUST BE POSITIVE NUMBER.')
            return False
        #当冲头冲击速度小于等于0时报错        
        elif self.globalsizeKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT GLOBALSIZE MUST BE POSITIVE NUMBER.')
            return False
        #当冲头网格尺寸小于等于0时报错
        elif self.materialNameKw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for impactor.')
            return False
        #当未选取冲头材料时报错
        elif self.materialName2Kw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for cohesive.')
            return False
        #当未选取层间材料时报错
        elif self.frictionKw.getValue()<0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'FRICTION MUST BE POSITIVE NUMBER.')
            return False
        #当摩擦系数小于0时报错
        elif self.biasKw.getValue()<0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'BIAS MUST BE POSITIVE NUMBER OR ZERO.')
            return False
        #当层板网格偏置度小于0时报错
        elif self.timeperiodKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'TIME PERIOD MUST BE POSITIVE NUMBER.')
            return False
        #当冲击响应时间小于等于0时报错
        elif self.gthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'GEOMETRY THICKNESS OF COHESIVE MUST BE POSITIVE.')
            return False
        #当层间几何厚度小于等于0时报错
        elif self.pthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'PHYSICAL THICKNESS OF COHESIVE MUST BE POSITIVE .')
            return False
        #当层间物理厚度小于等于0时报错
        elif self.layuptableKw.getValue(0,0)=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the layup material is not giving.')
            return False
        #当铺层表中材料未指定时报错
        
        #其他省略
        else:
            return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):
        # 由系统自动生成
        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
#指定文件路径

icon_impact= afxCreateIcon( os.path.join(thisDir, 'icon_impact.png') )
#定义插件图标
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='★复合材料工具包|★复合材料冲击损伤有限元模型参数化建模程序', 
    #定义插件在菜单中的显示文本
    object=compositesimpact_standard_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=icon_impact,
    #定义插件在菜单中的显示图标
    kernelInitString='import CompositesGenerateFunc',
    #初始化指令：导入内核执行文件
    applicableModules=ALL,
    #定义插件适用的模块
    version='1.0',
    #定义插件版本
    author='jly',
    #指定作者
    description='冲击损伤有限元模型的完全参数化建模',
    #插件描述
    helpUrl='N/A'
    #帮助文件路径
)   #将插件注册到【Plug-ins】菜单

toolset.registerGuiToolButton('注册工具条', 
    object=compositesimpact_standard_plugin(toolset), 
    buttonText='\t复合材料冲击损伤有限元模型参数化建模程序',
    kernelInitString='import CompositesGenerateFunc', icon=icon_impact,
    version='1.0', 
    author='jly',
    applicableModules = ['Part', 'Property', 'Assembly', 'Step', 
        'Interaction', 'Load', 'Mesh', 'Job'],
    description='冲击损伤有限元模型的完全参数化建模',
    helpUrl='N/A'
)   #将插件注册到自定义工具条，工具条名称为'注册工具条'