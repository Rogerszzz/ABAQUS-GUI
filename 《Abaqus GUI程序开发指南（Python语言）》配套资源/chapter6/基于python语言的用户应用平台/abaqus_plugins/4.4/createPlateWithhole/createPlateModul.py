# -* - coding:UTF-8 -*-
from abaqus import *
from abaqusConstants import *
def createPlateFunction(partname, width, height, radius,radiobutton):
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
    #几何创建完成
    mdb.models['Model-1'].Material(name='AL')
    mdb.models['Model-1'].materials['AL'].Elastic(table=((70000.0, 0.3), ))
    mdb.models['Model-1'].HomogeneousShellSection(name='al', preIntegrate=OFF, 
    material='AL', thicknessType=UNIFORM, thickness=1.0, thicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-2')
    p.SectionAssignment(region=region, sectionName='al', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    #建立材料并赋予属性
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    #切换到mesh模块
    p = mdb.models['Model-1'].parts[partname]
    p.seedPart(size=4.0, deviationFactor=0.1, minSizeFactor=0.1)
               
    f = p.faces                                               
    pickedRegions = f.findAt(((width/2, 0.0, 0.0), ))
    p.setMeshControls(regions=pickedRegions, elemShape=QUAD,algorithm=MEDIAL_AXIS)
    #设定网格划分格式
    p.generateMesh()   
    #网格划分   
    a = mdb.models['Model-1'].rootAssembly                                          
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(  
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    #切换到装配模块
    a = mdb.models['Model-1'].rootAssembly   
    a.DatumCsysByDefault(CARTESIAN)          
    p = mdb.models['Model-1'].parts[partname]
    a.Instance(name=partname+'-1', part=p, dependent=ON)
    #创建装配实例
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')  
    #创建分析步
    session.viewports['Viewport: 1'].view.setValues(nearPlane=335.564,            
        farPlane=385.546, width=212.48, height=142.547, viewOffsetX=13.3712,   
        viewOffsetY=-7.13345)                                                  
    a = mdb.models['Model-1'].rootAssembly                                     
    e1 = a.instances[partname+'-1'].edges                                         
    edges1 = e1.findAt(((0.0, height/2, 0.0), ))                                   
    region = a.Set(edges=edges1, name='Set-1')                                 
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,      
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',    
        localCsys=None)   
    #施加边界条件    
    edges1 = e1.findAt(((width, height/2, 0.0), ))                                      
    region = a.Set(edges=edges1, name='Set-2')                                      
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1',      
        region=region, u1=2.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',         
        localCsys=None) 
    #施加位移载荷
    mdb.Job(name='Job-hole', model='Model-1', description='', type=ANALYSIS,                                                               
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=50,        
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,                    
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,  
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0) 
    #创建job        