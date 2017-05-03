# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:44:39 2017

@author: Keith
"""

import numpy as np
import pandas as pd

def loadData2(filename):
    labels = []
    fvecs = []
    
    trackedTypes = {}
    typeID = 0
    output = []
    typeLabels = []
    length = 0
    for line in open(filename):
        stats = line.split(',')
        labels.append(int(stats[0]))
        fvecs.append([float(x) for x in stats[30:37]])
              
        length = length + 1 
    
        Type1 = stats[41]
        if stats[41] == 'normal':
            output.append(0)
        if stats[41] != 'normal':
            output.append(1)
    
        if Type1 not in trackedTypes: 
            trackedTypes[Type1] = typeID
            typeID = typeID + 1

    typeLabels.append(trackedTypes[Type1])
        
    fvecs_np = np.matrix(fvecs).astype(np.float)
    type_np = np.matrix(typeLabels).astype(dtype=np.uint8)
    labels_np = np.array(output).astype(dtype=np.uint8)
        
    return fvecs_np, labels_np, type_np, length

def loadData5(filename):
    labels = []
    fvecs = []
    df=pd.read_csv(filename)

    trackedTypes = {}
    typeID = 0
    output = []
    typeLabels = []
    length = 0
    for line in open(filename):
        stats = line.split(',')
        
        labels.append(int(stats[0]))
        #fvecs.append([float(x) for x in stats[30:37]])
        fvecs.append([df.loc[slice[5,6,12,27,29,37,39,42]]])

        length = length + 1

        Type1 = stats[41]
        if stats[41] == 'normal':
            output.append(0)
            
        if stats[41] == 'back':
            output.append(1)#dos
        if stats[41] == 'neptune':
            output.append(1)#dos
        if stats[41] == 'pod':
            output.append(1)#dos
        if stats[41] == 'smurf':
            output.append(1)#dos
        if stats[41] == 'teardrop':
            output.append(1)#dos
        if stats[41] == 'land':
            output.append(1)#dos
        if stats[41] == 'apache2': 
            output.append(1)#dos
        if stats[41] == 'processtable': 
            output.append(1)#dos    
        if stats[41] == 'mailbomb': 
            output.append(1)#dos
        if stats[41] == 'udpstorm':
            output.append(1)#dos
            
            
        if stats[41] == 'ipsweep': 
            output.append(2)#probe
        if stats[41] == 'nmap':
            output.append(2)#probe
        if stats[41] == 'portsweep':
            output.append(2)#probe
        if stats[41] == 'satan':
            output.append(2)#probe
        if stats[41] == 'saint':
            output.append(2)#probe
        if stats[41] == 'mscan':
            output.append(2)#probe
            
        if stats[41] == 'ftp_write':
            output.append(3)#R2l
        if stats[41] == 'guess_passwd':
            output.append(3)#R2l
        if stats[41] == 'imap':
            output.append(3)#R2l
        if stats[41] == 'multihop': 
            output.append(3)#R2l
        if stats[41] == 'phf':
            output.append(3)#R2l
        if stats[41] == 'spy':
            output.append(3)#R2l
        if stats[41] == 'warezclient':
            output.append(3)#R2l
        if stats[41] == 'warezmaster': 
            output.append(3)#R2l
        if stats[41] == 'sendmail': 
            output.append(3)#R2l
        if stats[41] == 'snmpguess': 
            output.append(3)#R2l
        if stats[41] == 'snmpgetattack': 
            output.append(3)#R2l    
        if stats[41] == 'xlock': 
            output.append(3)#R2l    
        if stats[41] == 'worm': 
            output.append(3)#R2l
        if stats[41] == 'named': 
            output.append(3)#R2l
        if stats[41] == 'xsnoop': 
            output.append(3)#R2l
            
        if stats[41] == 'buffer_overflow':
            output.append(4)#U2R
        if stats[41] == 'loadmodule':
            output.append(4)#U2R
        if stats[41] == 'perl': 
            output.append(4)#U2R
        if stats[41] == 'rootkit': 
            output.append(4)#U2R
        if stats[41] == 'httptunnel': 
            output.append(4)#U2R
        if stats[41] == 'ps': 
            output.append(4)#U2R
        if stats[41] == 'xterm': 
            output.append(4)#U2R
        if stats[41] == 'sqlattack': 
            output.append(4)#U2R
            
        if Type1 not in trackedTypes: 
            trackedTypes[Type1] = typeID
            typeID = typeID + 1

        typeLabels.append(trackedTypes[Type1])
        
        fvecs_np = np.matrix(fvecs).astype(np.float)
        type_np = np.matrix(typeLabels).astype(dtype=np.uint8)
        labels_np = np.array(output).astype(dtype=np.uint8)
        
    return fvecs_np, labels_np, type_np, length
def typeFromTrackedTypeID(ID, trackedTypes):
    for type, typeID in trackedTypes.iteritems():
        if ID == typeID:
            return type
        return "UNKNOWN TYPE"
    
