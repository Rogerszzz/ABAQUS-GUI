del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v1, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidExtrude(sketch=s, depth=1.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v1, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
#* NameError: name 'STANDALONE' is not defined
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v1, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
#* NameError: name 'THREE_D' is not defined
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v1, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Part-2']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=1.0)""")
#: mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Part-2']""")
cliCommand("""session.viewports['Viewport: 1'].setValues(displayedObject=p)""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""from abaqus import *                           #导入abaqus核心模块""")
cliCommand("""from abaqusConstants import *	                   #导入abaqus内部常量 """)
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)                           #默认草图平面""")
cliCommand("""g, v1, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints   #几何特征""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)         #设置当前视图窗口的主对象""")
cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))     #绘制矩形框""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)                #指定新零件名称及属性""")
cliCommand("""p = mdb.models['Model-1'].parts['Part-2']            #指向新零件""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=1.0)            #通过拉伸方法创建几何体""")
#: mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()                           #取消当前视图主对象设置""")
cliCommand("""p = mdb.models['Model-1'].parts['Part-2']""")
cliCommand("""session.viewports['Viewport: 1'].setValues(displayedObject=p)   #在视图中显示新零件""")
session.viewports['Viewport: 1'].view.setValues(width=13.593, height=10.9118, 
    viewOffsetX=0.0056217, viewOffsetY=0.231354)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.8947, 
    farPlane=37.2128, width=12.5528, height=10.0769, cameraPosition=(-13.4436, 
    -12.3295, 14.7723), cameraUpVector=(0.492733, 0.577677, 0.650771), 
    viewOffsetX=0.00519152, viewOffsetY=0.21365)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.3789, 
    farPlane=36.146, width=13.4445, height=10.7927, cameraPosition=(10.1733, 
    -18.6587, 16.9292), cameraUpVector=(-0.427446, 0.715075, 0.553135), 
    viewOffsetX=0.00556029, viewOffsetY=0.228826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.3524, 
    farPlane=37.4096, width=12.8279, height=10.2977, cameraPosition=(23.6909, 
    -11.2753, 16.2839), cameraUpVector=(-0.453345, 0.668704, 0.589333), 
    viewOffsetX=0.00530525, viewOffsetY=0.21833)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.7467, 
    farPlane=38.1747, width=12.464, height=10.0056, cameraPosition=(24.9924, 
    -15.1971, 8.27265), cameraUpVector=(-0.324224, 0.488944, 0.809823), 
    viewOffsetX=0.00515475, viewOffsetY=0.212136)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.069, 
    farPlane=37.7694, width=12.6576, height=10.161, cameraPosition=(24.368, 
    -13.561, 12.5818), cameraUpVector=(-0.527364, 0.458977, 0.715001), 
    viewOffsetX=0.00523482, viewOffsetY=0.215431)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.0487, 
    farPlane=37.7895, width=12.6455, height=10.1512, viewOffsetX=0.139328, 
    viewOffsetY=0.52365)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.0486, 
    farPlane=37.7897, width=12.6454, height=10.1512, viewOffsetX=0.434343, 
    viewOffsetY=1.77076)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.0486, 
    farPlane=37.7897, width=12.6454, height=10.1512, viewOffsetX=0.487982, 
    viewOffsetY=1.91827)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.9373, 
    farPlane=37.901, width=14.2356, height=11.4277, viewOffsetX=0.458165, 
    viewOffsetY=2.32018)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.8394, 
    farPlane=37.9988, width=14.169, height=11.3743, viewOffsetX=0.786584, 
    viewOffsetY=2.35442)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.5634, 
    farPlane=39.2748, width=24.6958, height=19.8247, viewOffsetX=1.01726, 
    viewOffsetY=4.84342)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4175, 
    farPlane=39.4208, width=24.5115, height=19.6768, viewOffsetX=4.38878, 
    viewOffsetY=6.88674)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
cliCommand("""from abaqus import *                           #导入abaqus核心模块""")
cliCommand("""from abaqusConstants import *	                   #导入abaqus内部常量 """)
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(                       
    name='__profile__', sheetSize=200.0,transform=(   
    0.0, 1.0, 0.0,
    0.0, 0.0, 1.0,
    1.0, 0.0, 0.0,
    0.0 ,0.0, 8.0
))                                            #重新指定草图平面""")
cliCommand("""g, v1, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints   #几何特征""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)         #设置当前视图窗口的主对象""")
cliCommand("""s.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))     #绘制矩形框""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)                #指定新零件名称及属性""")
cliCommand("""p = mdb.models['Model-1'].parts['Part-2']            #指向新零件""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=1.0)            #通过拉伸方法创建几何体""")
#: mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()                           #取消当前视图主对象设置""")
cliCommand("""p = mdb.models['Model-1'].parts['Part-2']""")
cliCommand("""session.viewports['Viewport: 1'].setValues(displayedObject=p)   #在视图中显示新零件""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']             #删除草图""")
session.viewports['Viewport: 1'].view.setValues(nearPlane=24.2569, 
    farPlane=35.1671, width=12.8887, height=10.3465, cameraPosition=(26.626, 
    -5.59947, 3.62004), cameraUpVector=(-0.12736, -0.222707, 0.966531))
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.9776, 
    farPlane=37.3067, width=11.6776, height=9.37428, cameraPosition=(17.7731, 
    17.7165, -7.4619), cameraUpVector=(0.567866, -0.394614, 0.722363))
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.3823, 
    farPlane=37.8766, width=11.3613, height=9.12034, cameraPosition=(12.5291, 
    21.8465, -8.20152), cameraUpVector=(0.724246, -0.4188, 0.54779))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.902, 
    farPlane=39.3569, width=23.7346, height=19.0531, viewOffsetX=0.11862, 
    viewOffsetY=3.35624)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7595, 
    farPlane=39.4994, width=23.5646, height=18.9166, viewOffsetX=2.81658, 
    viewOffsetY=5.25635)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7556, 
    farPlane=39.5033, width=23.56, height=18.9129, viewOffsetX=2.96593, 
    viewOffsetY=5.35525)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7555, 
    farPlane=39.5034, width=23.5599, height=18.9129, viewOffsetX=2.96592, 
    viewOffsetY=6.42953)
session.viewports['Viewport: 1'].view.setValues(width=22.1463, height=17.7781, 
    viewOffsetX=2.6084, viewOffsetY=5.9281)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9203, 
    farPlane=39.3386, width=22.3311, height=17.9264, cameraPosition=(12.5291, 
    21.8465, -8.20152), cameraUpVector=(0.724131, -0.45504, 0.51824), 
    viewOffsetX=2.63016, viewOffsetY=5.97755)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9242, 
    farPlane=39.3347, width=22.3355, height=17.93, cameraPosition=(12.5291, 
    21.8465, -8.20152), cameraUpVector=(0.689676, -0.631019, 0.355193), 
    viewOffsetX=2.63068, viewOffsetY=5.97873)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9243, 
    farPlane=39.3346, width=22.3357, height=17.9301, cameraPosition=(12.5291, 
    21.8465, -8.20152), cameraUpVector=(0.675774, -0.663771, 0.320527), 
    viewOffsetX=2.6307, viewOffsetY=5.97877)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9243, 
    farPlane=39.3346, width=22.3357, height=17.9302, cameraPosition=(12.5291, 
    21.8465, -8.20152), cameraUpVector=(0.722321, -0.382932, 0.575861), 
    viewOffsetX=2.6307, viewOffsetY=5.97878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.8888, 
    farPlane=39.5254, width=22.2959, height=17.8982, cameraPosition=(5.80106, 
    18.4244, -12.9672), cameraUpVector=(0.729129, 0.21497, 0.649737), 
    viewOffsetX=2.62601, viewOffsetY=5.96812)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.0393, 
    farPlane=38.4659, width=23.5857, height=18.9336, cameraPosition=(12.7488, 
    10.6567, -13.5193), cameraUpVector=(0.378888, 0.615869, 0.69076), 
    viewOffsetX=2.77792, viewOffsetY=6.31337)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.5035, 
    farPlane=36.9685, width=25.2271, height=20.2513, cameraPosition=(22.8746, 
    2.48022, -6.42558), cameraUpVector=(0.0629667, 0.873117, 0.483427), 
    viewOffsetX=2.97125, viewOffsetY=6.75275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.359, 
    farPlane=39.3397, width=22.8231, height=18.3214, cameraPosition=(15.6489, 
    -17.7199, 0.943537), cameraUpVector=(0.634254, 0.720199, 0.281132), 
    viewOffsetX=2.6881, viewOffsetY=6.10924)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.9104, 
    farPlane=38.7376, width=23.4412, height=18.8176, cameraPosition=(19.0647, 
    -14.1871, -0.294456), cameraUpVector=(0.50025, 0.553203, 0.66612), 
    viewOffsetX=2.7609, viewOffsetY=6.27469)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.2669, 
    farPlane=39.4636, width=22.7198, height=18.2385, cameraPosition=(15.1764, 
    -14.3968, -4.33056), cameraUpVector=(0.594633, 0.310872, 0.741465), 
    viewOffsetX=2.67593, viewOffsetY=6.08159)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.5955, 
    farPlane=37.9721, width=24.2092, height=19.4341, cameraPosition=(22.2656, 
    -6.08496, -4.0451), cameraUpVector=(0.375908, 0.315572, 0.871268), 
    viewOffsetX=2.85135, viewOffsetY=6.48026)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.6156, 
    farPlane=39.0775, width=23.1107, height=18.5523, cameraPosition=(14.8328, 
    -4.82976, -11.2656), cameraUpVector=(0.640922, 0.0778501, 0.763648), 
    viewOffsetX=2.72197, viewOffsetY=6.18621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.7759, 
    farPlane=38.9537, width=23.2905, height=18.6966, cameraPosition=(8.54009, 
    -1.4671, -15.0266), cameraUpVector=(0.815353, 0.108792, 0.568651), 
    viewOffsetX=2.74314, viewOffsetY=6.23432)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.7325, 
    farPlane=38.9968, width=23.2419, height=18.6576, cameraPosition=(9.13217, 
    -1.92018, -14.7406), cameraUpVector=(0.802475, 0.179751, 0.568967), 
    viewOffsetX=2.73741, viewOffsetY=6.22131)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.5992, 
    farPlane=39.1329, width=23.0925, height=18.5376, cameraPosition=(10.6316, 
    -3.58666, -13.7516), cameraUpVector=(0.763181, 0.305183, 0.569578), 
    viewOffsetX=2.71981, viewOffsetY=6.18131)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.8091, 
    farPlane=38.8712, width=23.3278, height=18.7266, cameraPosition=(15.7329, 
    -4.83984, -10.6988), cameraUpVector=(0.627875, 0.407742, 0.662963), 
    viewOffsetX=2.74752, viewOffsetY=6.2443)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.662, 
    farPlane=40.1924, width=22.0419, height=17.6943, cameraPosition=(5.19271, 
    -14.9634, -8.79661), cameraUpVector=(0.871719, 0.397448, 0.286603), 
    viewOffsetX=2.59606, viewOffsetY=5.90007)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.1307, 
    farPlane=39.6527, width=22.5674, height=18.1161, cameraPosition=(11.3885, 
    -11.8846, -9.13365), cameraUpVector=(0.752627, 0.397027, 0.525283), 
    viewOffsetX=2.65795, viewOffsetY=6.04072)
cliCommand("""p = mdb.models['Model-1'].parts['Part-1']                #指向零件""")
cliCommand("""e =p.elements                                             #指向零件的所有单元""")
cliCommand("""e1=e[0:]                                                 #[0:]表示索引号从0开始的所有单元""")
cliCommand("""p.Set(elements=e1, name='all_plate_elems')                     #创建单元集合                                     """)
#: mdb.models['Model-1'].parts['Part-1'].sets['all_plate_elems']
cliCommand("""p.Surface(face2Elements=e1, face3Elements=e2,name='plate_interior_surf')""")
#* NameError: name 'e2' is not defined
cliCommand("""p = mdb.models['Model-1'].parts['Part-1']                #指向零件""")
cliCommand("""e =p.elements                                             #指向零件的所有单元""")
cliCommand("""e1=e[0:]                                                 #[0:]表示索引号从0开始的所有单元""")
cliCommand("""p.Set(elements=e1, name='all_plate_elems')                     #创建单元集合                                     """)
#: mdb.models['Model-1'].parts['Part-1'].sets['all_plate_elems']
cliCommand("""p.Surface(face2Elements=e1, face3Elements=e1,name='plate_interior_surf')""")
#: mdb.models['Model-1'].parts['Part-1'].surfaces['plate_interior_surf']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.4998, 
    farPlane=82.6114, width=27.8695, height=22.3725, viewOffsetX=1.42792, 
    viewOffsetY=0.172739)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.2875, 
    farPlane=81.3002, width=28.941, height=23.2326, cameraPosition=(-4.36008, 
    13.698, 72.5956), cameraUpVector=(0.0834063, 0.880742, -0.466195), 
    viewOffsetX=1.48281, viewOffsetY=0.17938)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.567, 
    farPlane=83.7931, width=27.9098, height=22.4048, cameraPosition=(51.2036, 
    12.8686, 59.9026), cameraUpVector=(0.0220297, 0.799752, -0.599927), 
    viewOffsetX=1.42998, viewOffsetY=0.172988)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.7899, 
    farPlane=82.5179, width=28.0434, height=22.512, cameraPosition=(33.9798, 
    35.5098, 61.7312), cameraUpVector=(-0.326601, 0.658474, -0.678044), 
    viewOffsetX=1.43682, viewOffsetY=0.173816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.0815, 
    farPlane=83.3554, width=27.6188, height=22.1712, cameraPosition=(46.9371, 
    34.508, 54.2183), cameraUpVector=(-0.421055, 0.66963, -0.611807), 
    viewOffsetX=1.41507, viewOffsetY=0.171185)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#584 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.5233, 
    farPlane=82.5861, width=27.8836, height=22.3838, cameraPosition=(-34.0798, 
    4.92352, 57.1821), cameraUpVector=(0.161264, 0.930824, -0.327965), 
    viewOffsetX=1.42864, viewOffsetY=0.172826)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.7932, 
    farPlane=81.7299, width=27.446, height=22.0325, cameraPosition=(-36.2209, 
    39.5623, 37.1268), cameraUpVector=(0.638193, 0.596254, -0.487021), 
    viewOffsetX=1.40622, viewOffsetY=0.170114)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#279 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.0541, 
    farPlane=81.0275, width=28.2017, height=22.6391, cameraPosition=(-8.73792, 
    46.2692, 55.2613), cameraUpVector=(0.722218, 0.409206, -0.557631), 
    viewOffsetX=1.44494, viewOffsetY=0.174798)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.9629, 
    farPlane=81.1188, width=28.147, height=22.5952, viewOffsetX=0.48699, 
    viewOffsetY=-0.959779)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromGeometry(cellSeq=cells)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.8215, 
    farPlane=83.0877, width=31.059, height=24.9328, cameraPosition=(-33.4697, 
    30.7538, 49.3755), cameraUpVector=(0.536752, 0.718226, -0.442774), 
    viewOffsetX=0.537372, viewOffsetY=-1.05907)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.9994, 
    farPlane=77.1602, width=27.5695, height=22.1316, cameraPosition=(56.1822, 
    16.4798, 54.4605), cameraUpVector=(-0.196727, 0.82893, -0.523616), 
    viewOffsetX=0.476999, viewOffsetY=-0.940084)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.6957, 
    farPlane=72.9781, width=28.5862, height=22.9477, cameraPosition=(66.3697, 
    32.975, 24.9191), cameraUpVector=(-0.555781, 0.606908, -0.568129), 
    viewOffsetX=0.494589, viewOffsetY=-0.974751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.9514, 
    farPlane=77.3198, width=27.5408, height=22.1086, cameraPosition=(50.7312, 
    33.4287, 51.5547), cameraUpVector=(-0.503926, 0.685651, -0.525302), 
    viewOffsetX=0.476501, viewOffsetY=-0.939104)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
cliCommand("""e""")
#: mdb.models['Model-1'].parts['Part-1'].elements
cliCommand("""print e""")
#: ['MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object', 'MeshElement object']
cliCommand("""e""")
#: mdb.models['Model-1'].parts['Part-1'].elements
cliCommand("""e1=e[0:3]""")
cliCommand("""print e1""")
#: ['MeshElement object', 'MeshElement object', 'MeshElement object']
cliCommand("""e1.__members__""")
#* AttributeError: 'MeshSequence' object has no attribute '__members__'
cliCommand("""e1[0].__members__""")
#: ['connectivity', 'instanceName', 'label', 'type']
execfile('D:/hh.py', __main__.__dict__)
#* SyntaxError: ("Non-ASCII character '\\xb6' in file D:/hh.py on line 2, but 
#* no encoding declared; see http://www.python.org/peps/pep-0263.html for 
#* details", ('D:/hh.py', 2, 0, None))
execfile('D:/hh.py', __main__.__dict__)
#* Error: Renumbering can be applied to orphan mesh parts only.
#* File "D:/hh.py", line 2, in <module>
#*     p.renumberElement(startLabel=100, increment=1)
execfile('D:/hh.py', __main__.__dict__)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.7607, 
    farPlane=38.0634, width=21.4378, height=17.2094, viewOffsetX=1.01591, 
    viewOffsetY=0.535815)
execfile(
    'F:/原E盘数据/学习总结/abaqus分类总结/国防工业出版社约稿/随书光盘/chapter3/3.3/highlight.py', 
    __main__.__dict__)
#* SyntaxError: ("Non-ASCII character '\\xd6' in file 
#* F:/\xd4\xadE\xc5\xcc\xca\xfd\xbe\xdd/\xd1\xa7\xcf\xb0\xd7\xdc\xbd\xe1/abaqus\xb7\xd6\xc0\xe0\xd7\xdc\xbd\xe1/\xb9\xfa\xb7\xc0\xb9\xa4\xd2\xb5\xb3\xf6\xb0\xe6\xc9\xe7\xd4\xbc\xb8\xe5/\xcb\xe6\xca\xe9\xb9\xe2\xc5\xcc/chapter3/3.3/highlight.py 
#* on line 1, but no encoding declared; see 
#* http://www.python.org/peps/pep-0263.html for details", 
#* ('F:/\xd4\xadE\xc5\xcc\xca\xfd\xbe\xdd/\xd1\xa7\xcf\xb0\xd7\xdc\xbd\xe1/abaqus\xb7\xd6\xc0\xe0\xd7\xdc\xbd\xe1/\xb9\xfa\xb7\xc0\xb9\xa4\xd2\xb5\xb3\xf6\xb0\xe6\xc9\xe7\xd4\xbc\xb8\xe5/\xcb\xe6\xca\xe9\xb9\xe2\xc5\xcc/chapter3/3.3/highlight.py', 
#* 1, 0, None))
execfile(
    'F:/原E盘数据/学习总结/abaqus分类总结/国防工业出版社约稿/随书光盘/chapter3/3.3/highlight.py', 
    __main__.__dict__)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.5423, 
    farPlane=38.2817, width=25.5516, height=20.5117, viewOffsetX=1.99957, 
    viewOffsetY=0.776032)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.6076, 
    farPlane=83.0775, width=29.7379, height=23.8723, viewOffsetX=1.50321, 
    viewOffsetY=-0.408462)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
execfile(
    'F:/原E盘数据/学习总结/abaqus分类总结/国防工业出版社约稿/随书光盘/chapter3/3.3/highlight.py', 
    __main__.__dict__)
execfile(
    'F:/原E盘数据/学习总结/abaqus分类总结/国防工业出版社约稿/随书光盘/chapter3/3.3/highlight.py', 
    __main__.__dict__)
p1 = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].parts['Part-1'].sets['all_plate_elems']
del mdb.models['Model-1'].parts['Part-1'].surfaces['plate_interior_surf']
mdb.save()
#: The model database has been saved to "F:\原E盘数据\学习总结\abaqus分类总结\国防工业出版社约稿\随书光盘\chapter3\3.3\highlight.cae".
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
cliCommand("""p""")
#* AccessError: mdb.models['Model-1'].parts['Part-1'] no longer exists
cliCommand("""-start""")
#* NameError: name 'start' is not defined
