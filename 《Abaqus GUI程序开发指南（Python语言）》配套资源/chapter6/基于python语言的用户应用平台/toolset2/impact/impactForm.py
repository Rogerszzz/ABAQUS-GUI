# -* - coding:UTF-8 -*- 
from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

###########################################################################
# Class definition
###########################################################################

class impactForm(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
 
        AFXForm.__init__(self, owner)

        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='impactKernel',
            objectName='toolset2.impact.impactKernel', registerQuery=False)
        pickedDefault = ''
        self.lengthKw = AFXFloatKeyword(self.cmd, 'length', True, 100)
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True, 100)
        if not self.radioButtonGroups.has_key('eletype'):
            self.eletypeKw1 = AFXIntKeyword(None, 'eletypeDummy', True)
            self.eletypeKw2 = AFXStringKeyword(self.cmd, 'eletype', True)
            self.radioButtonGroups['eletype'] = (self.eletypeKw1, self.eletypeKw2, {})
        self.radioButtonGroups['eletype'][2][53] = 'Solid'
        if not self.radioButtonGroups.has_key('eletype'):
            self.eletypeKw1 = AFXIntKeyword(None, 'eletypeDummy', True)
            self.eletypeKw2 = AFXStringKeyword(self.cmd, 'eletype', True)
            self.radioButtonGroups['eletype'] = (self.eletypeKw1, self.eletypeKw2, {})
        self.radioButtonGroups['eletype'][2][54] = 'Continuum Shell'
        self.NXKw = AFXIntKeyword(self.cmd, 'NX', True, 10)
        self.NYKw = AFXIntKeyword(self.cmd, 'NY', True, 10)
        self.biasKw = AFXFloatKeyword(self.cmd, 'bias', True, 1)
        self.layuptableKw = AFXTableKeyword(self.cmd, 'layuptable', True)
        self.layuptableKw.setColumnType(0, AFXTABLE_TYPE_STRING)
        self.layuptableKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.layuptableKw.setColumnType(2, AFXTABLE_TYPE_INT)
        self.yesnocohesiveKw = AFXBoolKeyword(self.cmd, 'yesnocohesive', AFXBoolKeyword.TRUE_FALSE, True, True)
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

        import impactDB
        return impactDB.impactDB(self)

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
        if self.lengthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'L MUST BE POSITIVE NUMBER.')
            return False
        elif self.widthKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'W MUST BE POSITIVE NUMBER.')
            return False
        elif self.radiusKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'R MUST BE POSITIVE NUMBER.')
            return False
        elif self.heightKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'H  MUST BE POSITIVE NUMBER.')
            return False
        elif self.NXKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT NUMBER MUST BE POSITIVE NUMBER.')
            return False
        elif self.NYKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT NUMBER MUST BE POSITIVE NUMBER.')
            return False
        elif self.eletypeKw1.getValue()!=53 and self.eletypeKw1.getValue()!=54 :
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the element type is not defined.')
            return False
        elif self.velocityKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'IMPACT VELOCITY MUST BE POSITIVE NUMBER.')
            return False
        elif self.globalsizeKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'ELEMENT GLOBALSIZE MUST BE POSITIVE NUMBER.')
            return False
        elif self.materialNameKw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for impactor.')
            return False
        elif self.materialName2Kw.getValue()=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'please import or creat a material for cohesive.')
            return False
        elif self.frictionKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'FRICTION MUST BE POSITIVE NUMBER.')
            return False
        elif self.biasKw.getValue()<0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'BIAS MUST BE POSITIVE NUMBER OR ZERO.')
            return False
        elif self.timeperiodKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'TIME PERIOD MUST BE POSITIVE NUMBER.')
            return False
        elif self.gthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'GEOMETRY THICKNESS OF COHESIVE MUST BE POSITIVE.')
            return False
        elif self.pthickKw.getValue()<=0:
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'PHYSICAL THICKNESS OF COHESIVE MUST BE POSITIVE .')
            return False
        elif self.layuptableKw.getValue(0,0)=='':
            showAFXErrorDialog(getAFXApp().getAFXMainWindow(),
                 'the layup material is not giving.')
            return False
        else:
            return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
