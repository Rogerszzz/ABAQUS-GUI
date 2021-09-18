# -* - coding:UTF-8 -*-
from abaqus import *
from abaqusConstants import *
def testoptionbutton(partname, width, height, radius):
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
        point2=(width, height))
    mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
        width/2, height/2), point1=(width/2+radius, height/2))
    mdb.models['Model-1'].Part(dimensionality=THREE_D, name=partname, type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts[partname].BaseShell(sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    p = mdb.models['Model-1'].parts[partname]
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']