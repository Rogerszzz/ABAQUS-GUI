# -* - coding:UTF-8 -*-
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
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

        if not self.radioButtonGroups.has_key('radiobutton'):
            self.radiobuttonKw1 = AFXIntKeyword(None, 'radiobuttonDummy', True)
            self.radiobuttonKw2 = AFXStringKeyword(self.cmd, 'radiobutton', True)
            self.radioButtonGroups['radiobutton'] =(self.radiobuttonKw1, self.radiobuttonKw2, {})
        self.radioButtonGroups['radiobutton'][2][27] = 'YES'
        if not self.radioButtonGroups.has_key('radiobutton'):
            self.radiobuttonKw1 = AFXIntKeyword(None, 'radiobuttonDummy', True)
            self.radiobuttonKw2 = AFXStringKeyword(self.cmd, 'radiobutton', True)
            self.radioButtonGroups['radiobutton'] =(self.radiobuttonKw1, self.radiobuttonKw2, {})
        self.radioButtonGroups['radiobutton'][2][28] = 'NO'
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import createPlateWithholeDB
        return createPlateWithholeDB.createPlateWithholeDB(self)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
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
        if self.radiobuttonKw1.getValue()!=27 and self.radiobuttonKw1.getValue()!=28 :
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                '单选按钮未被选中.')

        else:
            return True
            
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
