# -* - coding:UTF-8 -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os
class testwarningdialog_standard_plugin(AFXForm):
    [
        ID_WARNING,
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_WARNING,
            testwarningdialog_standard_plugin.onCmdWarning)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='testoptionbutton',
            objectName='testModul', registerQuery=False)
        pickedDefault = ''
        self.partnameKw = AFXStringKeyword(self.cmd, 'partname', True, 'pp')
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True, 50)
        self.heightKw = AFXFloatKeyword(self.cmd, 'height', True, 50)
        self.radiusKw = AFXFloatKeyword(self.cmd, 'radius', True, 2)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import testwarningdialog_standardDB
        return testwarningdialog_standardDB.testwarningdialog_standardDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing. 
#        if self.radiusKw.getValue()<0:
#            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
#                 'radius must be lager than zero.')
#            return False
#        else:
#            return True
        
        if self.radiusKw.getValue()<0:
            showAFXWarningDialog( self.getCurrentDialog(),
               '您输入的半径值为负数，确定继续吗？',
                AFXDialog.YES | AFXDialog.NO | AFXDialog.CANCEL,
                self, self.ID_WARNING)
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
        print 'haha'
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
    buttonText='testwarningdialog_standard', 
    object=testwarningdialog_standard_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import testModul',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
