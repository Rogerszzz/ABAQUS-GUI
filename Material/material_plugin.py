from abaqusGui import getAFXApp, Activator, AFXMode
from abaqusConstants import ALL
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Material', 
    object=Activator(os.path.join(thisDir, 'material01DB.py')),
    kernelInitString='import materialfunc',
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    applicableModules=ALL,
    version='2.0',
    author='Rogers',
    description='N/A',
    helpUrl='N/A'
)
