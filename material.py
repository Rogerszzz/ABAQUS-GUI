# -*- coding: utf-8 -*-
'''
Created on Tue Mar 30 00:46:01 2021

@author: 36351
'''
import csv
from part import *
from material import *
from section import *
from optimization import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# read csv
with open('D:\\reliability\\material\\material_simple_data.csv', 'r') as myfile:
    for num, row in enumerate(myfile):
        if num >= 103:
            templist = row.split(',')
            templist = [data.replace('\n', '') for data in templist]
            jobname = str(templist[0])
            Xsigma = float(templist[1])
            Xepsilon = float(templist[2])
            b0 = float(templist[3])
            c0 = float(templist[4])
            fai = float(templist[5])
            temp_n1 = float(templist[6])
            wfcrit = float(templist[7])
            Density = float(templist[8])
            Creep_temp360 = float(templist[9])
            Creep_temp480 = float(templist[10])
            Creep_temp500 = float(templist[11])
            Creep_temp550 = float(templist[12])
            Creep_temp650 = float(templist[13])
            Creep_temp800 = float(templist[14])
            E_temp20 = float(templist[15])
            E_temp360 = float(templist[16])
            E_temp550 = float(templist[17])
            E_temp650 = float(templist[18])
            C1_temp20 = float(templist[19])
            C1_temp360 = float(templist[20])
            C1_temp550 = float(templist[21])
            C1_temp650 = float(templist[22])
            C2_temp20 = float(templist[23])
            C2_temp360 = float(templist[24])
            C2_temp550 = float(templist[25])
            C2_temp650 = float(templist[26])
            C3_temp20 = float(templist[27])
            C3_temp360 = float(templist[28])
            C3_temp550 = float(templist[29])
            C3_temp650 = float(templist[30])
            # change material properties
            mdb.models['Model-1'].materials['GH4169'].density.setValues(table=((Density,),))
            mdb.models['Model-1'].materials['GH4169'].elastic.setValues(table=((E_temp20, 0.3, 20.0),
                                                                               (E_temp360, 0.3, 360.0),
                                                                               (E_temp550, 0.3, 550.0),
                                                                               (E_temp650, 0.3, 650.0)))
            mdb.models['Model-1'].materials['GH4169'].plastic.setValues(
                table=((900.0, C1_temp20, 2500.0, C2_temp20, 60.0, C3_temp20, 1.0, 20.0),
                       (750.0, C1_temp360, 1700.0, C2_temp360, 55.0, C3_temp360, 1.0, 360.0),
                       (650.0, C1_temp550, 1700.0, C2_temp550, 55.0, C3_temp550, 1.0, 550.0),
                       (480.0, C1_temp650, 1800.0, C2_temp650, 55.0, C3_temp650, 1.0, 650.0)))
            mdb.models['Model-1'].materials['GH4169'].creep.setValues(table=((Creep_temp360, 5.77, -0.72, 360.0),
                                                                             (Creep_temp480, 5.77, -0.72, 480.0),
                                                                             (Creep_temp500, 5.77, -0.72, 500.0),
                                                                             (Creep_temp550, 5.77, -0.72, 550.0),
                                                                             (Creep_temp650, 5.77, -0.72, 650.0),
                                                                             (Creep_temp800, 5.77, -0.72, 800.0)))
            # change subroutain data
            with open('D:\\reliability\\material\\SEDE.for', 'r') as myuvarm:
                flist = myuvarm.readlines()
                flist[90] = '      Xsigma=%.4f\n' % Xsigma
                flist[91] = '      Xepsilon=%.4f\n' % Xepsilon
                flist[92] = '      b0=%.4f\n' % b0
                flist[93] = '      c0=%.4f\n' % c0
                flist[94] = '      fai=%.4f\n' % fai
                flist[95] = '      temp_n1=%.4f\n' % temp_n1
                flist[96] = '      wfcrit=%.4f\n' % wfcrit
            with open('SEDE%s.for' % jobname[3:], 'w') as newuvarm:
                newuvarm.writelines(flist)
            # creat job
            mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
                    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
                    memory=90, model='Model-1', modelPrint=OFF,
                    multiprocessingMode=DEFAULT, name=jobname, nodalOutputPrecision=FULL,
                    numCpus=20, numDomains=20, numGPUs=0, queue=None, scratch=
                    '', userSubroutine='SEDE%s.for' % jobname[3:], waitHours=0, waitMinutes=0)
            # write input
            mdb.jobs[jobname].writeInput(consistencyChecking=OFF)
            # submit

            mdb.jobs[jobname].submit(consistencyChecking=OFF)
            mdb.jobs[jobname].waitForCompletion()
