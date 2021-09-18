#! /user/bin/python
#-*-coding: UTF-8-*-
from abaqusConstants import *  
from caeModules import *       
from abaqus import *
import sys
###########################################################################
#�ں�ִ���ļ����ļ���Ϊ��honeycomb_fun.py
###########################################################################
def honeycomfun(modelName,materialName,partName,celldimention,celllength,\
             celldiameter,thickness,panellength,panelwidth,panelheight):                                            

    if celldimention=='Diameter:':
        celllength=celldiameter/sqrt(3)
    # ���ݾ�������Բֱ��������Ѿ���߳�
    l=celllength
    lhalf=0.5*celllength
    lsqrt=0.5*sqrt(3)*celllength   
    NX=int(panellength/3/celllength) 
    NY=int(panelwidth/sqrt(3)/celllength) 

    spacingX=3*l
    spacingY=sqrt(3)*celllength
    #�������β�ͼ
    s = mdb.models[modelName].ConstrainedSketch(name='__profile__', 
       sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(-lhalf, 0.0), point2=(lhalf, 0.0))
    
    s.Line(point1=(-lhalf, 0.0), point2=(-l, lsqrt))
    s.Line(point1=(-l, lsqrt), point2=(-2.0*l, lsqrt))
    s.Line(point1=(lhalf, 0.0), point2=(l, lsqrt))
    s.Line(point1=(l, lsqrt), point2=(2.0*celllength, lsqrt))
  
    s.Line(point1=(-lhalf, 0.0), point2=(-l, -lsqrt))
    s.Line(point1=(-l, -lsqrt), point2=(-2.0*celllength, -lsqrt))
    s.Line(point1=(lhalf, 0.0), point2=(l, -lsqrt))
    s.Line(point1=(l, -lsqrt), point2=(2.0*celllength, -lsqrt))
  
    #���г�ʼ��ͼ
    s.linearPattern(geomList=(g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10]), 
        vertexList=(), number1=NX, spacing1=spacingX, angle1=0.0, number2=NY, 
        spacing2=spacingY , angle2=90.0)
    session.viewports['Viewport: 1'].view.fitView()
    #������ά���Ѽ�����	
    p = mdb.models[modelName].Part(name=partName, dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)  
    p.BaseShellExtrude(sketch=s, depth=panelheight)
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[modelName].sketches['__profile__']
    #  ������
    mdb.models[modelName].HomogeneousShellSection(name='honeythickness1',             
        preIntegrate=OFF, material=materialName, thicknessType=UNIFORM,          
        thickness=thickness, thicknessField='', idealization=NO_IDEALIZATION,        
        poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
        useDensity=OFF, integrationRule=SIMPSON, numIntPts=5) 
    mdb.models[modelName].HomogeneousShellSection(name='honeythickness2',                         
        preIntegrate=OFF, material=materialName, thicknessType=UNIFORM,         
        thickness=2*thickness, thicknessField='', idealization=NO_IDEALIZATION,   
        poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
        useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)   
    p = mdb.models[modelName].parts[partName]                                            
    f = p.faces                                                             
    facethick1=f[0:0] 
    facethick2=f[0:0]
    #������Ҫ��˫���ȵ��沢������
    NX2=2*NX
    NY2=2*NY
    for  i in range(0,NX+1) :
        for  j in range(0,NY+1) :
            f1=f.findAt((1.5*l*(2*i-1),lsqrt*(2*j-1),0.5*panelheight),)             
            facethick2=facethick2+ f[f1.index:f1.index+1]
        milestone('                                      ˫������������:', 'zones', i, NX2)
        #���������½���ʾ������		
    for  i in range(0,NX) :
        for  j in range(0,NY) :
            f1=f.findAt((3*l*i,2*lsqrt*j,0.5*panelheight),)             
            facethick2=facethick2+ f[f1.index:f1.index+1]                
        milestone('                                      ˫������������:', 'zones', i+NX, NX2)
        #���������½���ʾ������
    region = regionToolset.Region(faces=facethick2)                              
    p.SectionAssignment(region=region, sectionName='honeythickness2', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='',                          
        thicknessAssignment=FROM_SECTION) 
    #������Ҫ�������ȵ��沢������
    for  j in range(0,2*NY) :
        for  i in range(0,2*NX) :        
            f1=f.findAt((0.75*l*(2*i-1),0.5*lsqrt*(2*j-1),0.5*panelheight),)             
            facethick1=facethick1+ f[f1.index:f1.index+1]
        milestone('                                      ��������������:', 'zones', j, NY2)
        #���������½���ʾ������
    region = regionToolset.Region(faces=facethick1)                              
    p.SectionAssignment(region=region, sectionName='honeythickness1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='',                          
        thicknessAssignment=FROM_SECTION)         
    #������		