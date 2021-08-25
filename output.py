from odbAccess import *
import csv


def datatodic(data, dic):
    for value in data:
        dic.update({value.elementLabel: value.data})
    return dic


def nodedatatodic(data, dic):
    for value in data:
        dic.update({value.nodeLabel: value.data})
    return dic


def findmax(dic):
    maxdata = max(dic.values())
    return maxdata


def getmean(dic):
    sum = 0
    for node in dic:
        sum = sum + dic[node]
    average = sum / len(dic)
    return average


myoutput = open('output.csv', 'a+', )
myWriter = csv.writer(myoutput)
myWriter.writerow(['creepmax1', 'creepmax2', 'creepmax3', 'fatiguemax1', 'fatiguemax2', 'fatiguemax3', 'totalmax1', 'totalmax2', 'totalmax3'])
for i in range(1, 231):
    odb = openOdb(path='D:\\reliability\\material\\CAE\\job%d.odb' % i)
    # myAssembly=odb.rootAssmebly
    # print odb.rootAssembly.elementSets.keys()
    # Choose the step and frame
    datastep = odb.steps['Step-6']
    dataframe = datastep.frames[1]
    # get element and node sets
    groove1 = odb.rootAssembly.instances['TURBINE-'].elementSets['GROOVE-1']
    groove2 = odb.rootAssembly.instances['TURBINE-'].elementSets['GROOVE-2']
    groove3 = odb.rootAssembly.instances['TURBINE-'].elementSets['GROOVE-3']
    # choose the fieldoutput
    creepdamage = dataframe.fieldOutputs['UVARM33']
    fatiguedamage = dataframe.fieldOutputs['UVARM35']
    totaldamage = dataframe.fieldOutputs['UVARM38']
    groove1creepdamage = creepdamage.getSubset(region=groove1).values
    groove2creepdamage = creepdamage.getSubset(region=groove2).values
    groove3creepdamage = creepdamage.getSubset(region=groove3).values
    groove1fatiguedamage = fatiguedamage.getSubset(region=groove1).values
    groove2fatiguedamage = fatiguedamage.getSubset(region=groove2).values
    groove3fatiguedamage = fatiguedamage.getSubset(region=groove3).values
    groove1totaldamage = totaldamage.getSubset(region=groove1).values
    groove2totaldamage = totaldamage.getSubset(region=groove2).values
    groove3totaldamage = totaldamage.getSubset(region=groove3).values
    # print groove1damage
    # print groove1damage.__getattribute__
    # creat datadic
    dic_groove1creepdamage = {}
    dic_groove2creepdamage = {}
    dic_groove3creepdamage = {}
    dic_groove1fatiguedamage = {}
    dic_groove2fatiguedamage = {}
    dic_groove3fatiguedamage = {}
    dic_groove1totaldamage = {}
    dic_groove2totaldamage = {}
    dic_groove3totaldamage = {}

    dic_groove1creepdamage = datatodic(groove1creepdamage, dic_groove1creepdamage)
    dic_groove2creepdamage = datatodic(groove2creepdamage, dic_groove2creepdamage)
    dic_groove3creepdamage = datatodic(groove3creepdamage, dic_groove3creepdamage)
    dic_groove1fatiguedamage = datatodic(groove1fatiguedamage, dic_groove1fatiguedamage)
    dic_groove2fatiguedamage = datatodic(groove2fatiguedamage, dic_groove3fatiguedamage)
    dic_groove3fatiguedamage = datatodic(groove3fatiguedamage, dic_groove3fatiguedamage)
    dic_groove1totaldamage = datatodic(groove1totaldamage, dic_groove1totaldamage)
    dic_groove2totaldamage = datatodic(groove2totaldamage, dic_groove2totaldamage)
    dic_groove3totaldamage = datatodic(groove3totaldamage, dic_groove3totaldamage)

    creepmax1 = findmax(dic_groove1creepdamage)
    creepmax2 = findmax(dic_groove2creepdamage)
    creepmax3 = findmax(dic_groove3creepdamage)

    fatiguemax1 = findmax(dic_groove1fatiguedamage)
    fatiguemax2 = findmax(dic_groove2fatiguedamage)
    fatiguemax3 = findmax(dic_groove3fatiguedamage)

    totalmax1 = findmax(dic_groove1totaldamage)
    totalmax2 = findmax(dic_groove2totaldamage)
    totalmax3 = findmax(dic_groove3totaldamage)

    myWriter.writerow(
        [creepmax1, creepmax2, creepmax3, fatiguemax1, fatiguemax2, fatiguemax3, totalmax1, totalmax2, totalmax3])

    # for d in groove1creepdamage:
    #    dic_groove1creepdamage.updata({d.elementLabel:d.data})

    odb.close()
# print type(groove1damage)
