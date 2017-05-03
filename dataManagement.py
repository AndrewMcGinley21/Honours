# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:01:19 2017

@author: Keith
"""
import numpy 

def _normalizeData(data):
    dataArray = numpy.asarray(data, dtype=numpy.float32)
    standardDeviation = dataArray.std(axis=0)
    average = dataArray.mean(axis=0)
    normalizedData = (dataArray - average)/ (standardDeviation)
    print(normalizedData)
    return normalizedData, standardDeviation, average

def _precomputedDataNormalize(data, standardDeviation, average):
    dataArray = numpy.asarray(data, dtype=numpy.float32)
    normalizedData = (dataArray - average)/ (standardDeviation)
    return normalizedData

def _oneHotData(data, dataSize):
    numpyDataArray = numpy.array(data).astype(dtype=numpy.uint8)
    oneHotData = (numpy.arange(dataSize) == numpyDataArray[:, None]).astype(numpy.float32)
    return oneHotData