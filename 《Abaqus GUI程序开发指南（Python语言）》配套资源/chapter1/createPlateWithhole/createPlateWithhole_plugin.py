# -* - coding:UTF-8 -*-
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
###########################################################################
# Class definition
###########################################################################

class createPlateWithhole_plugin(AFXForm):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='createPlateFunction',
            objectName='createPlateModul', registerQuery=False)
        pickedDefault = ''
        self.partnameKw = AFXStringKeyword(self.cmd, 'partname', True, 'part-1')
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True,100)
        self.heightKw = AFXFloatKeyword(self.cmd, 'height', True,100)
        self.radiusKw = AFXFloatKeyword(self.cmd, 'radius', True,5)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import createPlateWithholeDB
        return createPlateWithholeDB.createPlateWithholeDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        #对输入数据格式进行检查，不满足要求时提示警告
        if self.widthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 '宽度必须为正数')
            return False
        elif self.heightKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 '高度必须为正数')
            return False
        elif self.radiusKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 '孔半径必须是正数.')
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

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='创建带孔板', 
    object=createPlateWithhole_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import createPlateModul',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
