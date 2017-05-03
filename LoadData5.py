# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:44:39 2017

@author: Keith
"""

import numpy as np
import pandas as pd

def loadData2(filename):
    #labels = []
    
    dataset = pd.read_csv('KDDTrainOne.csv', names = ['duration',
                                                      'protocol_type',
                                                      'service',
                                                      'flag',
                                                      'src_bytes',
                                                      'dst_bytes',
                                                      'land',
                                                      'wrong_fragment',
                                                      'urgent',
                                                      'hot',
                                                      'num_failed_logins',
                                                      'logged_in',
                                                      'num_compromised',
                                                      'root_shell',
                                                      'su_attempted',
                                                      'num_root',
                                                      'num_file_creations',
                                                      'num_shells',
                                                      'num_access_files',
                                                      'num_outbound_cmds',
                                                      'is_host_login',
                                                      'is_guest_login',
                                                      'count',
                                                      'srv_count',
                                                      'serror_rate',
                                                      'srv_serror_rate',
                                                      'rerror_rate',
                                                      'srv_rerror_rate',
                                                      'same_srv_rate',
                                                      'diff_srv_rate',
                                                      'srv_diff_host_rate',
                                                      'dst_host_count',
                                                      'dst_host_srv_count',
                                                      'dst_host_same_srv_rate',
                                                      'dst_host_diff_srv_rate',
                                                      'dst_host_same_src_port_rate',
                                                      'dst_host_srv_diff_host_rate',
                                                      'dst_host_serror_rate',
                                                      'dst_host_srv_serror_rate',
                                                      'dst_host_rerror_rate',
                                                      'dst_host_srv_rerror_rate',
                                                      'class',
                                                      'class2'])


    trackedTypes = {}
    typeID = 0
    
    typeLabels = []
    length = int(len(dataset.index))
    print(length)

    features = dataset[['src_bytes','dst_bytes', 'logged_in','rerror_rate', 'same_srv_rate', 'dst_host_srv_diff_host_rate', 'dst_host_srv_serror_rate', 'dst_host_srv_rerror_rate']]
    output = dataset['class']

    #print(features)
    #print(output)
    print()
    record = []
    output = []
    #print(record)
    i  = 0
    for i in range(length):
        record.append(features.iloc[:i])
        #labels.append(output.iloc[:i])
        #print(record)
        #print(labels)
        i = i + 1
    for line in open(filename):
        stats = line.split(',') 
        
        Type1 = stats[41]
        if stats[41] == 'normal':
            output.append(0)
        if stats[41] != 'normal':
            output.append(1)
    
        if Type1 not in trackedTypes: 
            trackedTypes[Type1] = typeID
            typeID = typeID + 1
   
 
    length = length + 1
    #typeLabels.append(trackedTypes[Type1])
        
    fvecs_np = np.matrix(record).astype(np.float)
    type_np = np.matrix(typeLabels).astype(dtype=np.uint8)
    labels_np = np.array(output).astype(dtype=np.uint8)
    print(fvecs_np)    
    return fvecs_np, labels_np, type_np, length

def loadData5(filename):
    dataset = pd.read_csv('KDDTrainOne.csv', names = ['duration',
                                                      'protocol_type',
                                                      'service',
                                                      'flag',
                                                      'src_bytes',
                                                      'dst_bytes',
                                                      'land',
                                                      'wrong_fragment',
                                                      'urgent',
                                                      'hot',
                                                      'num_failed_logins',
                                                      'logged_in',
                                                      'num_compromised',
                                                      'root_shell',
                                                      'su_attempted',
                                                      'num_root',
                                                      'num_file_creations',
                                                      'num_shells',
                                                      'num_access_files',
                                                      'num_outbound_cmds',
                                                      'is_host_login',
                                                      'is_guest_login',
                                                      'count',
                                                      'srv_count',
                                                      'serror_rate',
                                                      'srv_serror_rate',
                                                      'rerror_rate',
                                                      'srv_rerror_rate',
                                                      'same_srv_rate',
                                                      'diff_srv_rate',
                                                      'srv_diff_host_rate',
                                                      'dst_host_count',
                                                      'dst_host_srv_count',
                                                      'dst_host_same_srv_rate',
                                                      'dst_host_diff_srv_rate',
                                                      'dst_host_same_src_port_rate',
                                                      'dst_host_srv_diff_host_rate',
                                                      'dst_host_serror_rate',
                                                      'dst_host_srv_serror_rate',
                                                      'dst_host_rerror_rate',
                                                      'dst_host_srv_rerror_rate',
                                                      'class',
                                                      'class2'])


    trackedTypes = {}
    typeID = 0
    
    typeLabels = []
    length = int(len(dataset.index))
    print(length)

    features = dataset[['src_bytes','dst_bytes', 'logged_in','rerror_rate', 'same_srv_rate', 'dst_host_srv_diff_host_rate', 'dst_host_srv_serror_rate', 'dst_host_srv_rerror_rate']]
    output = dataset['class']

    #print(features)
    #print(output)
    print()
    record = []
    labels = []
    #print(record)
    i  = 0
    for i in range(length):
        record.append(features.iloc[:i])
        #labels.append(output.iloc[:i])
        print(record)
        #print(labels)
        i = i + 1
    for line in open(filename):
        stats = line.split(',') 

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
    
