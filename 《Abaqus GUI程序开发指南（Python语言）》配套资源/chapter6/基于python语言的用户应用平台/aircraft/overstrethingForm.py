#-*-coding: UTF-8-*-
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class overstrethingForm(AFXForm):
    [
        ID_WARNING,
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='overstrethingkernel',
            objectName='aircraft.overstrethingKernel', registerQuery=False)
        pickedDefault = ''
        self.celllengthKw = AFXFloatKeyword(self.cmd, 'celllength', True, 5)
        self.cellwidthKw = AFXFloatKeyword(self.cmd, 'cellwidth', True, 2)
        self.thicknessKw = AFXFloatKeyword(self.cmd, 'thickness', True, 0.05)
        self.panellengthKw = AFXFloatKeyword(self.cmd, 'panellength', True, 100)
        self.panelwidthKw = AFXFloatKeyword(self.cmd, 'panelwidth', True, 100)
        self.panelheightKw = AFXFloatKeyword(self.cmd, 'panelheight', True, 20)
        self.modelNameKw = AFXStringKeyword(self.cmd, 'modelName', True)
        self.materialNameKw = AFXStringKeyword(self.cmd, 'materialName', True)
        self.partNameKw = AFXStringKeyword(self.cmd, 'partName', True, 'honeycomb')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import overstrethingDB
        return overstrethingDB.overstrethingDB(self)

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
    def onCmdWarning(self, sender, sel, ptr):

        if sender.getPressedButtonId() == \
            AFXDialog.ID_CLICKED_YES:
                self.issueCommands()
        elif sender.getPressedButtonId() == \
            AFXDialog.ID_CLICKED_NO:
                self.deactivate() 
