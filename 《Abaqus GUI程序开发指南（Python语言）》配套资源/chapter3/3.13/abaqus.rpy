# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.10-1 replay file
# Internal Version: 2010_04_29-14.17.36 102575
# Run by jly4553 on Sat Aug 30 09:44:11 2014
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=234.375, 
    height=216.796875)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('byangle.cae')
#: The model database "F:\原E盘数据\学习总结\abaqus分类总结\国防工业出版社约稿\随书光盘\chapter3\3.13\byangle.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.038, 
    farPlane=103.365, width=31.3433, height=30.076, viewOffsetX=0.889963, 
    viewOffsetY=-0.309766)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
p = mdb.models['Model-1'].parts['Part-1']
e = p.elements
elements = e.getSequenceFromMask(mask=('[#0:13 #40 ]', ), )
p.Set(elements=elements, name='Set-1')
#: The set 'Set-1' has been created (1 element).
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.9349, 
    farPlane=103.468, width=44.8261, height=33.9776, viewOffsetX=0.966673, 
    viewOffsetY=-0.751184)
session.viewports['Viewport: 1'].view.setValues(nearPlane=65.1113, 
    farPlane=96.8312, width=50.3787, height=38.1863, cameraPosition=(15.3264, 
    5.08631, 90.9907), cameraUpVector=(-0.348112, 0.868496, -0.352891), 
    viewOffsetX=1.08641, viewOffsetY=-0.844233)
session.viewports['Viewport: 1'].view.setValues(nearPlane=56.2682, 
    farPlane=104.536, width=43.5365, height=33.0001, cameraPosition=(-35.9572, 
    -7.00333, 71.0481), cameraUpVector=(-0.113569, 0.917935, -0.380129), 
    viewOffsetX=0.938858, viewOffsetY=-0.729573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=57.2269, 
    farPlane=103.011, width=44.2783, height=33.5624, cameraPosition=(-29.6716, 
    15.0871, 75.7636), cameraUpVector=(0.126741, 0.870676, -0.475246), 
    viewOffsetX=0.954854, viewOffsetY=-0.742003)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.2519, 
    farPlane=102.536, width=45.8452, height=34.75, cameraPosition=(47.1877, 
    31.9023, 79.1933), cameraUpVector=(-0.259774, 0.765932, -0.588104), 
    viewOffsetX=0.988642, viewOffsetY=-0.768259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.5579, 
    farPlane=100.88, width=46.082, height=34.9295, cameraPosition=(48.9213, 
    65.4436, 50.4356), cameraUpVector=(-0.562734, 0.349587, -0.749079), 
    viewOffsetX=0.993749, viewOffsetY=-0.772227)
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.3463, 
    farPlane=101.962, width=45.9183, height=34.8054, cameraPosition=(42.8993, 
    41.5703, 76.281), cameraUpVector=(-0.509569, 0.643443, -0.571245), 
    viewOffsetX=0.990218, viewOffsetY=-0.769483)
mdb.saveAs(
    pathName='F:/原E盘数据/学习总结/abaqus分类总结/国防工业出版社约稿/随书光盘/chapter3/3.15/transform.cae')
#: The model database has been saved to "F:\原E盘数据\学习总结\abaqus分类总结\国防工业出版社约稿\随书光盘\chapter3\3.15\transform.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=58.2817, 
    farPlane=103.026, width=56.9236, height=38.6838, viewOffsetX=1.59784, 
    viewOffsetY=-0.313097)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v[1], point2=v[8], point3=v[2], 
    cells=pickedCells)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
mdb.save()
#: The model database has been saved to "F:\原E盘数据\学习总结\abaqus分类总结\国防工业出版社约稿\随书光盘\chapter3\3.15\transform.cae".
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(faces=faces, name='Set-2')
#: The set 'Set-2' has been created (1 face).
session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7445, 
    farPlane=99.5633, width=25.36, height=17.301, viewOffsetX=-0.159625, 
    viewOffsetY=-5.14163)
import os
os.chdir(
    r'F:\原E盘数据\学习总结\abaqus分类总结\国防工业出版社约稿\随书光盘\chapter3\3.15')
del mdb.models['Model-1'].parts['Part-1'].sets['Set-2']
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.Set(faces=faces, name='Set-2')
#: The set 'Set-2' has been created (1 face).
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry= COORDINATE)""")
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.findAt(((20.211912, 3.333333, 20.0), ))
p.Set(faces=faces, name='Set-3')
#: The set 'Set-3' has been created (1 face).
cliCommand("""session.journalOptions.setValues(replayGeometry=INDEX,recoverGeometry=INDEX)""")
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f[1:2]
p.Set(faces=faces, name='Set-4')
#: The set 'Set-4' has been created (1 face).
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
mdb.models['Model-1'].parts['Part-1'].deleteSets(setNames=('Set-2', 'Set-3', 
    'Set-4', ))
mdb.save()
#: The model database has been saved to "F:\原E盘数据\学习总结\abaqus分类总结\国防工业出版社约稿\随书光盘\chapter3\3.15\transform.cae".
