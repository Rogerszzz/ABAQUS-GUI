# -* - coding:UTF-8 -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

class test_addtransition_plugin(AFXForm):
    [
        ID_WARNING,
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_WARNING,
            test_addtransition_plugin.onCmdWarning)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='',
            objectName='', registerQuery=False)
        pickedDefault = ''
        self.radiusKw = AFXFloatKeyword(self.cmd, 'radius', True)
        self.yesnoKw = AFXBoolKeyword(self.cmd, 'yesno', 
            AFXBoolKeyword.TRUE_FALSE, True, True)
        self.lengthKw = AFXFloatKeyword(self.cmd, 'length', True)
        if not self.radioButtonGroups.has_key('yesno'):
            self.yesnoKw1 = AFXIntKeyword(None, 'yesnoDummy', True)
            self.yesnoKw2 = AFXStringKeyword(self.cmd, 'yesno', True)
            self.radioButtonGroups['yesno'] =(self.yesnoKw1, self.yesnoKw2, {})
        self.radioButtonGroups['yesno'][2][1] = 'YES'

        if not self.radioButtonGroups.has_key('radiobutton'):
            self.yesnoKw1 = AFXIntKeyword(None, 'yesnoDummy', True)
            self.yesnoKw2 = AFXStringKeyword(self.cmd, 'yesno', True)
            self.radioButtonGroups['yesno'] =(self.yesnoKw1, self.yesnoKw2, {})
        self.radioButtonGroups['yesno'][2][2] = 'NO'

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import test_addTransition_DB
        return test_addTransition_DB.test_addTransition_DB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

        if self.radiusKw.getValue()<= 0:    
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 '半径必须为正数。')
            return False 
        else:
            return True    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
    def onCmdWarning(self, sender, sel, ptr):

        if sender.getPressedButtonId() == \
            AFXDialog.ID_CLICKED_YES:
                self.issueCommands()
        elif sender.getPressedButtonId() == \
            AFXDialog.ID_CLICKED_NO:
                self.deactivate() 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='test_addtransition', 
    object=test_addtransition_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
