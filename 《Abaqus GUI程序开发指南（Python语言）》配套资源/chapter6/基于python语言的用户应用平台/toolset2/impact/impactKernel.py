# -*- coding: mbcs -*-  
# -* - coding:UTF-8 -*- 
##################################################################################
# Created by jly4553 on Tue Feb 28 14:32:31 2012 
#  
##################################################################################
# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ... 
from abaqus import *
from abaqusConstants import * 
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup

def impactKernel(length,width,radius,height,NX,NY,gthick,pthick,eletype,
    layuptable,bias,yesnocohesive,velocity,globalsize,timeperiod,friction,
    modelName,materialName,modelName2,materialName2):

        executeOnCaeStartup()
      
     
        session.viewports['Viewport: 1'].setValues(displayedObject=None)                        
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',                         
            sheetSize=200.0)                                                                    
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints                        
        s.setPrimaryObject(option=STANDALONE)                                                   
        #           
        s.rectangle(point1=(-length/2.0, -width/2.0), point2=(length/2.0, width/2.0))                                 
        p = mdb.models['Model-1'].Part(name='plate', dimensionality=THREE_D,                    
            type=DEFORMABLE_BODY)                                                               
        p = mdb.models['Model-1'].parts['plate']                                                
        p.BaseShell(sketch=s)                                                                   
        s.unsetPrimaryObject()                                                                  
        p = mdb.models['Model-1'].parts['plate']                                                
        session.viewports['Viewport: 1'].setValues(displayedObject=p)                           
        del mdb.models['Model-1'].sketches['__profile__'] 
        N=len(layuptable)
        totalthick=0 
        for i in range(1,N+1):
            totalthick=totalthick+layuptable[i-1][1]
        totalthick=totalthick+(N-1)*gthick
        offsetsketckplane=totalthick+0.0001                                   
        s = mdb.models['Model-1'].ConstrainedSketch(                       
            name='__profile__', sheetSize=200.0,transform=(   
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0,
            1.0, 0.0, 0.0,
            0.0 ,0.0, offsetsketckplane
            ))                                              
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints                        
        s.setPrimaryObject(option=STANDALONE)                                                   
        s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))                           
        s.FixedConstraint(entity=g[2])                                                          
        #: The contents of viewport "Viewport: 1" have been copied to the clipboard.            
        s.Line(point1=(0.0, 25.0), point2=(10.0, 25.0))                                         
        s.HorizontalConstraint(entity=g[3], addUndoState=False)                                 
        s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)               
        s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)                  
        s.Line(point1=(10.0, 25.0), point2=(10.0, 10.0))                                        
        s.VerticalConstraint(entity=g[4], addUndoState=False)                                   
        s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)               
        s.ArcByStartEndTangent(point1=(10.0, 10.0), point2=(0.0, 0.0), entity=g[4])             
        s.CoincidentConstraint(entity1=v[3], entity2=g[2], addUndoState=False)                  
        s.RadialDimension(curve=g[5], textPoint=(10, 10),            
            radius=10.0)                                                                        
        #: The contents of viewport "Viewport: 1" have been copied to the clipboard.            
        s.FixedConstraint(entity=v[3])                                                          
        s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(5,             
            5), value=15.0)                                                      
        s.Line(point1=(0.0, 25.0), point2=(0.0, 0.0))                                           
        s.VerticalConstraint(entity=g[6], addUndoState=False)                                   
        s.PerpendicularConstraint(entity1=g[3], entity2=g[6], addUndoState=False)
        s.Parameter(name='radius1', path='dimensions[0]', expression=radius)
        s.Parameter(name='hight1', path='dimensions[1]', expression=height, 
            previousParameter='radius1')                                                 
        #: The contents of viewport "Viewport: 1" have been copied to the clipboard.           
        p = mdb.models['Model-1'].Part(name='impactor',                      
            dimensionality=THREE_D, type=DEFORMABLE_BODY)                                       
        p = mdb.models['Model-1'].parts['impactor']                          
        p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)                     
        s.unsetPrimaryObject()                                                                  
        p = mdb.models['Model-1'].parts['impactor']                          
        session.viewports['Viewport: 1'].setValues(displayedObject=p)                           
        del mdb.models['Model-1'].sketches['__profile__']  
        p.regenerate()                
        #
        mdb.models['Model-1'].HomogeneousSolidSection(
            name='impactor', material=materialName, thickness=None)
        p = mdb.models['Model-1'].parts['impactor']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
        region = regionToolset.Region(cells=cells)
        p = mdb.models['Model-1'].parts['impactor']
        p.SectionAssignment(region=region, sectionName='impactor', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION)                       
        ####:mesh plate  
        p = mdb.models['Model-1'].parts['plate']
        f = p.faces
        pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
        p.setMeshControls(regions=pickedRegions, elemShape=QUAD, technique=STRUCTURED)    
        #p = mdb.models['Model-1'].parts['plate']
        e = p.edges
        pickedCenterEdges = e.getSequenceFromMask(mask=('[#a ]', ), )
        p.seedEdgeByBias(biasMethod=DOUBLE, centerEdges=pickedCenterEdges,\
            ratio=bias, number=NX, constraint=FIXED)
        e = p.edges
        pickedCenterEdges = e.getSequenceFromMask(mask=('[#5 ]', ), )
        
        #p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
        p.seedEdgeByBias(biasMethod=DOUBLE, centerEdges=pickedCenterEdges, ratio=bias, number=NY, constraint=FIXED)
        p.generateMesh()
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        ####generate mesh
        NE= len(p.elements)
        p.PartFromMesh(name='plate-mesh')
        p = mdb.models['Model-1'].parts['plate-mesh'] 
        session.viewports['Viewport: 1'].setValues(displayedObject=p)   
        p.DatumCsysByThreePoints(name='layupsys', coordSysType=CARTESIAN, origin=(0.0,0.0, 0.0), line1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
        ####:generate orphan mensh 
        p = mdb.models['Model-1'].parts['plate-mesh']
        elements =p.elements
        p.Set(elements=elements, name='quad_mesh')
        ####:all elements in a set
        mdb.models['Model-1'].parts['plate-mesh'].Surface(name='Surf-0', 
            side1Elements=mdb.models['Model-1'].parts['plate-mesh'].elements)
        ########################################################
        #offset to generate element
        ########################################################
        p = mdb.models['Model-1'].parts['plate-mesh'] 
        if eletype=='Continuum Shell':
            elemType_contiuum_shell = mesh.ElemType(elemCode=SC8R, elemLibrary=STANDARD,     
                secondOrderAccuracy=OFF, hourglassControl=DEFAULT)
            plateeletype= elemType_contiuum_shell
        else:
            elemType_Solid = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
                kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,     
                hourglassControl=DEFAULT, distortionControl=DEFAULT)
            plateeletype =elemType_Solid        
        elemType_cohesive = mesh.ElemType(elemCode=COH3D8, elemLibrary=STANDARD, 
            elemDeletion=ON) 
        #######################judgment  of  element type
        if  yesnocohesive==False:
        ####:neglect cohesive 
            for i in range(1,N+1):
        
                p = mdb.models['Model-1'].parts['plate-mesh']
                sur1=p.surfaces['Surf-0']
                p.generateMeshByOffset(region=p.surfaces['Surf-0'], deleteBaseElements=False,meshType=SOLID, 
                    totalThickness=layuptable[i-1][1], numLayers=1, shareNodes=True)
                p = mdb.models['Model-1'].parts['plate-mesh']
                e = p.elements
                e1=e[NE*(i):NE*(i+1)+1]
                p.Set(elements=e1,name='eleset'+str(i))
                face2Elements = e1
                p.Surface(face2Elements=face2Elements, name='Surf-0')
                pickedRegions =(e1, )
                p.setElementType(regions=pickedRegions, elemTypes=(plateeletype, ))     
        if  yesnocohesive==True: 
        ####:consider cohesive elements  
            mdb.models['Model-1'].CohesiveSection(name='cohesive', material=materialName2, 
                response=TRACTION_SEPARATION, initialThicknessType=SPECIFY, 
                initialThickness=pthick, outOfPlaneThickness=None)
            for i in range(1,N+1):                                                                                         
                p = mdb.models['Model-1'].parts['plate-mesh']                                                           
                sur1=p.surfaces['Surf-0']                                                                                  
                p.generateMeshByOffset(region=p.surfaces['Surf-0'], deleteBaseElements=False,meshType=SOLID,               
                    totalThickness=layuptable[i-1][1], numLayers=1, shareNodes=True)                                                      
                p = mdb.models['Model-1'].parts['plate-mesh']                                                            
                e = p.elements                                                                                             
                e1=e[NE*(2*i-1):NE*(2*i)+1]                                                                                    
                p.Set(elements=e1,name='eleset'+str(i))                                                                    
                face2Elements = e1                                                                                         
                p.Surface(face2Elements=face2Elements, name='Surf-0')
                pickedRegions =(e1, )
                p.setElementType(regions=pickedRegions, elemTypes=(plateeletype , ))     
        #
                if i!=N:
                    ####:if there is cohesive on the top 
                    sur1=p.surfaces['Surf-0']                                                                                  
                    p.generateMeshByOffset(region=p.surfaces['Surf-0'], deleteBaseElements=False,meshType=SOLID,               
                        totalThickness=gthick, numLayers=1, shareNodes=True)                                                      
                    p = mdb.models['Model-1'].parts['plate-mesh']                                                                                
                    e = p.elements                                                                                             
                    e1=e[NE*(2*i):NE*(2*i+1)+1]                                                                                    
                    p.Set(elements=e1,name='cohesive'+str(i))                                                                    
                    face2Elements = e1                                                                                         
                    p.Surface(face2Elements=face2Elements, name='Surf-0') 
                    region = p.sets['cohesive'+str(i)]
                    p.SectionAssignment(region=region, sectionName='cohesive', offset=0.0, 
                        offsetType=MIDDLE_SURFACE, offsetField='',thicknessAssignment=FROM_SECTION) 
                    pickedRegions =(e1, )
                    p.setElementType(regions=pickedRegions, elemTypes=(elemType_cohesive, ))                                                             
        p.deleteElement(elements=p.sets['quad_mesh'])
        del mdb.models['Model-1'].parts['plate-mesh'].sets['quad_mesh']
        del mdb.models['Model-1'].parts['plate-mesh'].surfaces['Surf-0']
        #delete useless elements
        #
        e =p.elements
        e1=e[0:]
        p.Set(elements=e1, name='all_plate_elems')
        faceElements = e1
        p.Surface(face1Elements=faceElements, face2Elements=faceElements,face3Elements=faceElements,face4Elements=faceElements, face5Elements=faceElements,face6Elements=faceElements,name='plate_interior_surf')
        #generate all internal surface
        #made all elements in a set used for contact defination                                                                                  
        #p = mdb.models['Model-1'].parts['plate-mesh']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        session.viewports['Viewport: 1'].view.setValues(nearPlane=221.459,          
            farPlane=357.8, width=160.181, height=126.041, cameraPosition=(1.98816, 
            -265.194, 117.096), cameraUpVector=(0.00902812, 0.690104, 0.723654),    
            viewOffsetX=-5.38, viewOffsetY=-8.5296) 
        #
        layupOrientation = mdb.models['Model-1'].parts['plate-mesh'].datums[2]
        #select layup sys
        p = mdb.models['Model-1'].parts['plate-mesh']
        if  eletype=='Continuum Shell':
            compositeLayup = mdb.models['Model-1'].parts['plate-mesh'].CompositeLayup(
                name='CompositeLayup-1', description='', elementType=CONTINUUM_SHELL, 
                symmetric=False)
            compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
                poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
                useDensity=OFF)
            compositeLayup.ReferenceOrientation(orientationType=SYSTEM, 
                localCsys=layupOrientation, fieldName='', 
                additionalRotationType=ROTATION_NONE, angle=0.0, 
                additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3)
            for i in range(1,N+1):
                region1=p.sets['eleset'+str(i)]
                compositeLayup.CompositePly(suppressed=False, plyName='Ply-'+str(i), region=region1, 
                    material=layuptable[i-1][0], thicknessType=SPECIFY_THICKNESS, thickness=layuptable[i-1][1], 
                    orientationType=SPECIFY_ORIENT, orientationValue=layuptable[i-1][2], 
                    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
                    axis=AXIS_3, angle=0.0, numIntPoints=3)
        else:
            orientation = mdb.models['Model-1'].parts['plate-mesh'].datums[2]                                                
            for i in range(1,N+1):                                                                                           
                                                                                                                             
                mdb.models['Model-1'].HomogeneousSolidSection(name=str(layuptable[i-1][0])+str(layuptable[i-1][2]),          
                    material=layuptable[i-1][0], thickness=None)                                                             
                p = mdb.models['Model-1'].parts['plate-mesh']                                                                
                region = p.sets['eleset'+str(i)]                                                                             
                p.SectionAssignment(region=region, sectionName=str(layuptable[i-1][0])+str(layuptable[i-1][2]), offset=0.0,  
                    offsetType=MIDDLE_SURFACE, offsetField='',                                                               
                    thicknessAssignment=FROM_SECTION)                                                                        
                mdb.models['Model-1'].parts['plate-mesh'].MaterialOrientation(region=region,                                 
                    orientationType=SYSTEM, axis=AXIS_3, localCsys=orientation, fieldName='',                                
                    additionalRotationType=ROTATION_ANGLE, additionalRotationField='',                                       
                    angle=layuptable[i-1][2], stackDirection=STACK_3)                                                        
        # assign layup parameter to each ply.
        p = mdb.models['Model-1'].parts['impactor']
        p.seedPart(size=globalsize, deviationFactor=0.25)
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
        v1, e, d1 = p.vertices, p.edges, p.datums
        p.PartitionCellByPlaneThreePoints(point1=v1[2], point2=v1[1], point3=v1[0], 
            cells=pickedCells)
        pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
        v2, e1, d2 = p.vertices, p.edges, p.datums
        p.PartitionCellByPlaneThreePoints(point3=v2[3], cells=pickedCells, 
            point1=p.InterestingPoint(edge=e1[7], rule=MIDDLE), 
            point2=p.InterestingPoint(edge=e1[8], rule=MIDDLE))
        pickedCells = c.getSequenceFromMask(mask=('[#f ]', ), )
        e, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[5], normal=e[5], cells=pickedCells)
        p.generateMesh()
        ####:construct assembly
        a1 = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['impactor']
        a1.Instance(name='impactor-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['plate-mesh']
        a1.Instance(name='plate-mesh-1', part=p, dependent=ON)
        a1.Instance(name='plate-mesh-1', part=p, dependent=ON)
        #######################
        #######################
        mdb.models['Model-1'].ContactProperty('IntProp-1')
        if friction>0 :
           mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
               formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
               pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
               friction, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
               fraction=0.005, elasticSlipStiffness=None)
        if friction==0: 
           mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
               formulation=FRICTIONLESS)
        mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
            pressureOverclosure=HARD, allowSeparation=ON, 
            constraintEnforcementMethod=DEFAULT)
        #: The interaction property "IntProp-1" has been created.
        mdb.models['Model-1'].ContactExp(name='generalcontact', 
            createStepName='Initial')
        r22=mdb.models['Model-1'].rootAssembly.instances['plate-mesh-1'].surfaces['plate_interior_surf']
        r31=mdb.models['Model-1'].rootAssembly.instances['plate-mesh-1'].surfaces['plate_interior_surf']
        mdb.models['Model-1'].interactions['generalcontact'].includedPairs.setValuesInStep(
            stepName='Initial', useAllstar=OFF, addPairs=((ALLSTAR, SELF), (ALLSTAR, 
            r22), (r31, SELF)))
        mdb.models['Model-1'].interactions['generalcontact'].contactPropertyAssignments.appendInStep(
            stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
        #:creat the contact
        a = mdb.models['Model-1'].rootAssembly
        a.ReferencePoint(point=(0.0, 0.0, 50.0))
        a2 = mdb.models['Model-1'].rootAssembly
        c1 = a2.instances['impactor-1'].cells
        cells1 = c1[0:]
        region2=regionToolset.Region(cells=cells1)
        a2 = mdb.models['Model-1'].rootAssembly
        r1 = a2.referencePoints
        refPoints1=(r1[7], )
        region1=regionToolset.Region(referencePoints=refPoints1)
        mdb.models['Model-1'].RigidBody(name='rigidbody', refPointRegion=region1, 
            bodyRegion=region2, refPointAtCOM=ON)
        a2.Set(referencePoints=refPoints1, name='RF')
        #creat rigidbody
        ##########
        #########creat step
        mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
            timePeriod=timeperiod, timeIncrementationMethod=AUTOMATIC_EBE, scaleFactor=1.0, 
            maxIncrement=None)
        ################# 
        a = mdb.models['Model-1'].rootAssembly
        r1 = a.referencePoints
        refPoints1=(r1[7], )
        region = regionToolset.Region(referencePoints=refPoints1)
        mdb.models['Model-1'].Velocity(name='Predefined Field-1', region=region, 
            field='', distributionType=MAGNITUDE, velocity1=0.0, velocity2=0.0, 
            velocity3=-velocity, omega=0.0)
        #: Creat a  field as initial velocity
        ###############creat job
        mdb.Job(name='Job-impact', model='Model-1', description='', type=ANALYSIS, 
            atTime=None, waitMinutes=0, waitHours=0, queue=None, 
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, scratch='', 
            parallelizationMethodExplicit=DOMAIN, numDomains=2, 
            activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=2)
        p = mdb.models['Model-1'].parts['plate-mesh']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)