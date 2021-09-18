from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class test1DB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Example',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')           

        FXButton(p=self, text='TEST', ic=None, tgt=None, sel=0,opts=BUTTON_NORMAL|LAYOUT_FILL_X , x=0, y=0, w=0, h=0, pl=0)
        GroupBox_1 = FXGroupBox(p=self, text='Test', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='L:', tgt=form.keyword01Kw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='W:', tgt=form.keyword02Kw, sel=0)
        slider = AFXSlider(GroupBox_1, form.keyword05Kw, 0, 
            AFXSLIDER_INSIDE_BAR|AFXSLIDER_SHOW_VALUE|LAYOUT_FIX_WIDTH, 0,0,200,0)
        slider.setTitleLabelText('Slider')
        slider.setTitleLabelJustify(JUSTIFY_CENTER_X)
        slider.setMinLabelText('Min')
        slider.setMaxLabelText('Max')
        slider.setRange(1, 10)

        FXButton(p=GroupBox_1, text='RUN', ic=None, tgt=None, sel=0)

