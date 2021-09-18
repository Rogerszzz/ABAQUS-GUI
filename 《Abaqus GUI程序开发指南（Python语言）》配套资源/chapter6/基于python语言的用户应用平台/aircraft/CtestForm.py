#-*-coding: UTF-8-*-
# -*- coding: mbcs -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class CtestForm(AFXForm):
    [
        ID_WARNING,
    ] = range(AFXForm.ID_LAST, AFXForm.ID_LAST+1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_WARNING,
            CtestForm.onCmdWarning)
        self.radioButtonGroups = {}  

        self.cmd = AFXGuiCommand(mode=self, method='CtestKernel',   #×¢²á¹Ø¼ü×Ö
            objectName='aircraft.CtestKernel', registerQuery=False)
        pickedDefault = ''
        self.modelName1Kw = AFXStringKeyword(self.cmd, 'modelName1', True)
        self.partNameKw = AFXStringKeyword(self.cmd, 'partName', True)
        self.CSYSKWKw = AFXObjectKeyword(self.cmd, 'CSYSKW', TRUE, pickedDefault)   #×ø±êÏµ¹Ø¼ü×Ö
        if not self.radioButtonGroups.has_key('eletype'):
            self.eletypeKw1 = AFXIntKeyword(None, 'eletypeDummy', True)
            self.eletypeKw2 = AFXStringKeyword(self.cmd, 'eletype', True)
            self.radioButtonGroups['eletype'] = (self.eletypeKw1, self.eletypeKw2, {})
        self.radioButtonGroups['eletype'][2][1] = 'Continuum Shell'
        if not self.radioButtonGroups.has_key('eletype'):
            self.eletypeKw1 = AFXIntKeyword(None, 'eletypeDummy', True)
            self.eletypeKw2 = AFXStringKeyword(self.cmd, 'eletype', True)
            self.radioButtonGroups['eletype'] = (self.eletypeKw1, self.eletypeKw2, {})
        self.radioButtonGroups['eletype'][2][2] = 'SOLID'
        self.layuptableKw = AFXTableKeyword(self.cmd, 'layuptable', True)
        self.layuptableKw.setColumnType(0, AFXTABLE_TYPE_STRING)
        self.layuptableKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.layuptableKw.setColumnType(2, AFXTABLE_TYPE_INT)
        self.yesnocohesiveKw = AFXBoolKeyword(self.cmd, 'yesnocohesive', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.gthickKw = AFXFloatKeyword(self.cmd, 'gthick', True, 0.01)
        self.pthickKw = AFXFloatKeyword(self.cmd, 'pthick', True, 0.01)
        self.modelName2Kw = AFXStringKeyword(self.cmd, 'modelName2', True)
        self.materialNameKw = AFXStringKeyword(self.cmd, 'materialName', True)



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import CtestDB
        return CtestDB.CtestDB(self)

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
        if self.modelName1Kw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please select a model.')
            return False
        elif self.partNameKw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please select a part.')
            return False
        elif self.eletypeKw1.getValue()!=1 and self.eletypeKw1.getValue()!=2 :
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the element type is not defined.')
            return False
        elif self.layuptableKw.getValue(0,0)=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the layup material is not given.')
            return False
        if self.yesnocohesiveKw ==True and self.modelName2Kw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please select a model.')
            return False
        if self.yesnocohesiveKw ==True and self.materialNameKw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for cohesive.')
            return False        
        elif self.yesnocohesiveKw ==True and self.gthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'GEOMETRY THICKNESS OF COHESIVE MUST BE POSITIVE.')
            return False
        elif self.yesnocohesiveKw ==True and self.pthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'PHYSICAL THICKNESS OF COHESIVE MUST BE POSITIVE .')
            return False
        elif self.CSYSKWKw.getValue() =='None' or self.CSYSKWKw.getValue() =='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please pick a datum sys in the viewport .')
            return False
        elif self.materialNameKw.getValue() =='None' or self.materialNameKw.getValue() =='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the cohesive material is not given .')
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