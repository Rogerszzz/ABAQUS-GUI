# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-03.28.56 126354
# Run by taishanbuzuo on Thu Dec 31 02:16:36 2015
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=161.607620239258, 
    height=119.26823425293)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
import aircraft.CtestKernel
import toolset2.impact.impactKernel
import aircraft.honeycombKernel
import aircraft.overstrethingKernel
import toolset2.impact.impactKernel
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
import aircraft.CtestKernel
import toolset2.impact.impactKernel
import aircraft.honeycombKernel
import aircraft.overstrethingKernel
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((70000.0, 0.3), ))
aircraft.honeycombKernel.honeycombkernel(celldimention='Length:', 
    celllength=1.8, celldiameter=3.2, thickness=0.05, panellength=40, 
    panelwidth=20, panelheight=20, modelName='Model-1', 
    materialName='Material-1', partName='honeycomb')
session.viewports['Viewport: 1'].view.setValues(nearPlane=63.0122, 
    farPlane=129.574, width=97.0274, height=44.2397, cameraPosition=(71.9284, 
    62.0004, 66.8496), cameraTarget=(16.3337, 6.40568, 11.2549))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.5277, 
    farPlane=127.79, cameraPosition=(68.8064, 22.8504, 90.3024), 
    cameraUpVector=(-0.29432, 0.871611, -0.392009), cameraTarget=(16.3337, 
    6.40568, 11.2549))
session.viewports['Viewport: 1'].view.setValues(nearPlane=66.9179, 
    farPlane=127.031, cameraPosition=(58.0367, 37.5684, 92.28), 
    cameraUpVector=(-0.24086, 0.783915, -0.572244), cameraTarget=(16.2377, 
    6.53685, 11.2725))
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.086, 
    farPlane=125.863, width=91.2058, height=41.5854, cameraPosition=(57.4762, 
    38.4281, 92.2399), cameraTarget=(15.6772, 7.39651, 11.2324))
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.5638, 
    farPlane=125.561, cameraPosition=(52.7665, 34.6716, 95.8086), 
    cameraUpVector=(-0.242406, 0.809587, -0.534611), cameraTarget=(15.644, 
    7.37011, 11.2575))
session.viewports['Viewport: 1'].view.setValues(nearPlane=68.8701, 
    farPlane=125.323, cameraPosition=(52.6981, 30.6975, 97.0206), 
    cameraUpVector=(-0.208761, 0.833724, -0.511198), cameraTarget=(15.6435, 
    7.3386, 11.2671))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(64.512, 
    32.2433, 91.4947), cameraTarget=(27.4574, 8.88443, 5.74118))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['honeycomb']
a.Instance(name='honeycomb-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=73.6364, 
    farPlane=134.012, width=78.0469, height=35.5856, viewOffsetX=1.43779, 
    viewOffsetY=-0.0620303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=72.804, 
    farPlane=128.869, width=77.1647, height=35.1833, cameraPosition=(-26.497, 
    42.773, 94.3905), cameraUpVector=(0.261923, 0.764434, -0.589099), 
    cameraTarget=(17.3866, 6.19948, 7.69544), viewOffsetX=1.42154, 
    viewOffsetY=-0.0613291)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.8782, 
    farPlane=112.708, width=65.6839, height=29.9486, viewOffsetX=3.35375, 
    viewOffsetY=-1.31259)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].view.setValues(nearPlane=77.7706, 
    farPlane=114.815, width=87.1378, height=39.7306, viewOffsetX=4.89089, 
    viewOffsetY=-0.545086)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['honeycomb']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['honeycomb']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['honeycomb']
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['honeycomb']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.4224, 
    farPlane=113.163, width=70.3988, height=32.2219, cameraPosition=(17.0275, 
    5.31504, 106.293), cameraTarget=(17.0275, 5.31504, 10))
session.viewports['Viewport: 1'].view.setProjection(projection=PERSPECTIVE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=79.0273, 
    farPlane=113.558, width=74.0009, height=33.8706, viewOffsetX=-3.31206, 
    viewOffsetY=0.00286222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=75.3436, 
    farPlane=117.062, width=70.5515, height=32.2917, cameraPosition=(7.80498, 
    20.8581, 104.975), cameraUpVector=(-0.00997014, 0.986736, -0.162029), 
    cameraTarget=(17.0089, 5.41712, 10.3747), viewOffsetX=-3.15767, 
    viewOffsetY=0.0027288)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.6197, 
    farPlane=115.671, width=71.7465, height=32.8387, cameraPosition=(11.8606, 
    17.8038, 105.559), cameraUpVector=(-0.00663612, 0.99154, -0.129635), 
    cameraTarget=(17.0179, 5.37248, 10.2107), viewOffsetX=-3.21115, 
    viewOffsetY=0.00277502)
session.viewports['Viewport: 1'].view.setValues(nearPlane=76.0611, 
    farPlane=116.23, width=80.6059, height=36.8937, viewOffsetX=-3.74708, 
    viewOffsetY=0.282434)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
aircraft.honeycombKernel.honeycombkernel(celldimention='Length:', 
    celllength=1.8, celldiameter=3.2, thickness=0.05, panellength=40, 
    panelwidth=40, panelheight=20, modelName='Model-1', 
    materialName='Material-1', partName='honeycomb')
session.viewports['Viewport: 1'].view.setValues(nearPlane=97.2986, 
    farPlane=141.953, width=92.0913, height=41.9891, viewOffsetX=1.4197, 
    viewOffsetY=0.836897)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=92.8521, 
    farPlane=139.28, width=111.884, height=51.0137, viewOffsetX=3.66342, 
    viewOffsetY=0.266159)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(83.9794998168945, 
    -19.0546875))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.0494, 
    farPlane=141.083, width=59.0925, height=40.4953, viewOffsetX=1.52117, 
    viewOffsetY=-1.92401)
session.viewports['Viewport: 1'].setValues(width=192.65885925293, height=135.5)
session.viewports['Viewport: 1'].setValues(origin=(59.6325035095215, 
    -48.6953125), width=216.65299987793, height=165.140625)
session.viewports['Viewport: 1'].view.setValues(nearPlane=95.6913, 
    farPlane=136.441, width=54.8762, height=39.7045, viewOffsetX=0.168292, 
    viewOffsetY=-1.13683)
session.graphicsOptions.setValues(backgroundStyle=GRADIENT, 
    backgroundColor='#1B2D46')
session.viewports['Viewport: 1'].view.setValues(width=58.7234, height=42.4881, 
    viewOffsetX=-0.174889, viewOffsetY=-1.50231)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.graphicsOptions.setValues(backgroundStyle=SOLID)
session.graphicsOptions.setValues(backgroundStyle=GRADIENT)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#FF0000', 'Default', 
    '#FF0000')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#800080', 'Default', 
    '#800080')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#008080', 'Default', 
    '#008080')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness1':(True, '#008000', 'Default', 
    '#008000')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness1':(True, '#FFD700', 'Default', 
    '#FFD700')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#FF0000', 'Default', 
    '#FF0000')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#0000FF', 'Default', 
    '#0000FF')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#008080', 'Default', 
    '#008080')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness1':(True, '#808000', 'Default', 
    '#808000')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness1':(True, '#A8A800', 'Default', 
    '#A8A800')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness1':(True, '#FF0000', 'Default', 
    '#FF0000')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness1':(True, '#FFFF00', 'Default', 
    '#FFFF00'), 'honeythickness2':(True, '#FF0000', 'Default', '#FF0000')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap = session.viewports['Viewport: 1'].colorMappings['Section']
cmap.updateOverrides(overrides={'honeythickness2':(True, '#008080', 'Default', 
    '#008080')})
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part geometry']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['honeycomb']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['honeycomb']
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=100.163, 
    farPlane=131.97, width=35.0138, height=25.3335, viewOffsetX=-6.86503, 
    viewOffsetY=7.23085)
session.viewports['Viewport: 1'].view.setValues(nearPlane=81.6139, 
    farPlane=142.427, width=28.5298, height=20.6421, cameraPosition=(-11.353, 
    -62.6222, 83.8284), cameraUpVector=(0.200549, 0.658213, 0.725627), 
    cameraTarget=(14.1593, 17.6446, 3.96765), viewOffsetX=-5.59372, 
    viewOffsetY=5.8918)
session.viewports['Viewport: 1'].view.setValues(nearPlane=82.2912, 
    farPlane=131.604, width=28.7666, height=20.8134, cameraPosition=(11.5099, 
    -89.5949, 2.45181), cameraUpVector=(0.0231629, -0.0173072, 0.999582), 
    cameraTarget=(15.1741, 26.3975, 4.37525), viewOffsetX=-5.64014, 
    viewOffsetY=5.94069)
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.124, 
    farPlane=143.008, width=48.7514, height=35.2731, viewOffsetX=0.300843, 
    viewOffsetY=-0.592855)
p = mdb.models['Model-1'].parts['honeycomb']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=(
    '[#1254924a #25484952 #54849521 #a8495212 #44094484 #44094409:2 #a2425409', 
    ' #a204a204:2 #2a04a204 #51025121 #51025102:2 #28909502 #28812881:2 #4a812881', 
    ' #94409448 #94409440:2 #4a242540 #4a204a20:2 #12a04a20 #25102512 #25102510:2', 
    ' #12890950 #12881288:2 #84a81288 #9440944:3 #4a24254 #4a204a2:2 #512a04a2', 
    ' #128944a2 #84804a25 #20100804 #10848040 #84210842 #9210 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=2.0, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
p = mdb.models['Model-1'].parts['honeycomb']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=95.4774, 
    farPlane=136.655, width=62.5979, height=45.2914, viewOffsetX=-0.681688, 
    viewOffsetY=-0.465833)
session.viewports['Viewport: 1'].view.setValues(nearPlane=81.8146, 
    farPlane=148.604, width=53.6402, height=38.8102, cameraPosition=(130.07, 
    24.7393, 25.8093), cameraUpVector=(-0.00517297, 0.916642, -0.399675), 
    cameraTarget=(15.501, 16.7738, 9.02356), viewOffsetX=-0.584139, 
    viewOffsetY=-0.399172)
session.viewports['Viewport: 1'].view.setValues(nearPlane=77.8251, 
    farPlane=152.026, width=51.0246, height=36.9178, cameraPosition=(90.6394, 
    67.9511, -61.3176), cameraUpVector=(-0.331225, 0.897359, 0.291611), 
    cameraTarget=(14.9122, 16.7563, 10.2069), viewOffsetX=-0.555655, 
    viewOffsetY=-0.379708)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.5998, 
    farPlane=142.533, width=46.071, height=33.3337, viewOffsetX=-1.13718, 
    viewOffsetY=-2.5781)
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=84.515, 
    farPlane=147.617, width=76.4389, height=55.3058, cameraPosition=(13.4808, 
    -98.9189, 5.54541), cameraTarget=(13.4808, 17.1473, 5.54541))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['honeycomb-1'].edges
edges1 = e1.getSequenceFromMask(mask=(
    '[#a4892491 #48929224 #8929224a #129224a4 #29522929 #29522952:2 #14948952', 
    ' #14a914a9:2 #44a914a9 #8a548a4a #8a548a54:2 #45252254 #452a452a:2 #912a452a', 
    ' #22952292 #22952295:2 #91494895 #914a914a:2 #a44a914a #48a548a4 #48a548a5:2', 
    ' #a4525225 #a452a452:2 #2912a452 #52295229:3 #a9149489 #a914a914:2 #8a44a914', 
    ' #a4522914 #292a9148 #4aa552a9 #a5292a95 #294a5294 #24a5 ]', ), )
v1 = a.instances['honeycomb-1'].vertices
verts1 = v1.getSequenceFromMask(mask=(
    '[#4d54d553 #d54d54d5 #d5354d54 #d4d4d4d4 #5354d4d4 #53535353 #4d4d5353', 
    ' #4d4d4d4d #3535354d #35353535 #d4d4d4d5 #54d4d4d4 #53535353 #4d535353', 
    ' #4d4d4d4d #35354d4d #35353535 #d4d4d535 #d4d4d4d4 #53535354 #d3535353', 
    ' #34d34d34 #55555555 #5555 ]', ), )
region = a.Set(vertices=verts1, edges=edges1, name='Set-1')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.5989, 
    farPlane=149.099, cameraPosition=(12.7549, -16.2649, -105.605), 
    cameraUpVector=(0.00576801, -0.957662, 0.287838), cameraTarget=(13.4808, 
    17.1473, 5.54541))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.7403, 
    farPlane=149.434, cameraPosition=(32.2383, 0.11026, -107.823), 
    cameraUpVector=(-0.0330835, -0.988367, 0.148443), cameraTarget=(14.1742, 
    17.7301, 5.46647))
session.viewports['Viewport: 1'].view.setValues(nearPlane=86.1171, 
    farPlane=153.327, cameraPosition=(30.5355, -34.8538, -96.9226), 
    cameraUpVector=(-0.0722241, -0.896537, 0.437041), cameraTarget=(14.1172, 
    16.5593, 5.83149))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=94.3805, 
    farPlane=137.752, width=61.4457, height=44.4578, cameraPosition=(23.985, 
    16.6366, 126.066), cameraTarget=(23.985, 16.6366, 10))
session.viewports['Viewport: 1'].view.setValues(nearPlane=80.3711, 
    farPlane=145.336, cameraPosition=(-25.6551, -9.95507, 111.489), 
    cameraUpVector=(0.189635, 0.923078, 0.334612))
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.8091, 
    farPlane=141.219, cameraPosition=(32.5509, 31.6702, 124.112), 
    cameraUpVector=(0.149398, 0.977059, -0.151776), cameraTarget=(22.328, 
    15.4516, 9.64067))
session.viewports['Viewport: 1'].view.setValues(nearPlane=90.1078, 
    farPlane=141.92, width=69.5402, height=50.3144, cameraPosition=(34.1827, 
    32.699, 123.82), cameraTarget=(23.9598, 16.4804, 9.34917))
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.1521, 
    farPlane=141.981, cameraPosition=(16.7819, -4.89458, 123.2), 
    cameraUpVector=(0.0062091, 0.982712, 0.185035), cameraTarget=(23.9676, 
    16.4972, 9.34945))
session.viewports['Viewport: 1'].view.setValues(nearPlane=87.345, 
    farPlane=142.861, cameraPosition=(16.7544, -10.7271, 121.945), 
    cameraUpVector=(0.00299177, 0.971838, 0.23563), cameraTarget=(23.9678, 
    16.5478, 9.36035))
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.4964, 
    farPlane=147.157, cameraPosition=(17.109, -43.3569, 108.483), 
    cameraUpVector=(-0.0193639, 0.854975, 0.518308), cameraTarget=(23.9648, 
    16.8206, 9.47291))
session.viewports['Viewport: 1'].view.setValues(nearPlane=89.2326, 
    farPlane=141.422, width=35.2081, height=25.4741, cameraPosition=(3.77254, 
    -48.7812, 104.263), cameraTarget=(10.6283, 11.3963, 5.25262))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['honeycomb-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=(
    '[#2cb2cb24 #cb #0:12 #ccc92490 #ccccc #c00 ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, field='', magnitude=10.0, 
    amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=88.8052, 
    farPlane=141.849, width=42.3896, height=30.6701, cameraPosition=(6.66414, 
    -48.1259, 104.861), cameraTarget=(13.5199, 12.0516, 5.85113))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=83.4968, 
    farPlane=147.158, width=73.979, height=53.526, cameraPosition=(16.8486, 
    -48.5156, 105.33), cameraTarget=(23.7044, 11.6619, 6.31947))
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: Error checking out Abaqus license.
#: Job Job-1 aborted due to errors.
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: Error checking out Abaqus license.
#: Job Job-1 aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=77.9082, 
    farPlane=152.746, width=107.236, height=77.5885, cameraPosition=(8.26388, 
    -45.4529, 106.597), cameraTarget=(15.1197, 14.7246, 7.5865))
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: Error checking out Abaqus license.
#: Job Job-1 aborted due to errors.
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
mdb.saveAs(pathName='D:/temp/test11.cae')
#: The model database has been saved to "D:\temp\test11.cae".
