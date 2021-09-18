# -* - coding:UTF-8 -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
class TESTICON_plugin(AFXForm):
    def __init__(self, owner):
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='',
            objectName='', registerQuery=False)
        pickedDefault = ''
    def getFirstDialog(self):

        import TESTICONDB
        return TESTICONDB.TESTICONDB(self)
    def doCustomChecks(self):
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True
    def okToCancel(self):
        return False

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)
icon1= afxCreateIcon( os.path.join(thisDir, 'icon1.png') )  #创建插件图标
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='测试图标', 
    object=TESTICON_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=icon1,
    kernelInitString='',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
