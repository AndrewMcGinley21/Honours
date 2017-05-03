# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:09:16 2017

@author: Keith
"""

#import pandas as pd

#import numpy as np 
#import matplotlib.pyplot as plt 
import tensorflow as tf 
import LoadData3
import dataManagement


data, labels, recordType , length = LoadData3.loadData2('KDDTrainThree.csv')
print('Training Data ripped')
#print(data)
print(labels)
encodedTrainLabels = dataManagement._oneHotData(labels, 5)
#print(encodedTrainLabels)
#print(recordType)
#print(length)

testData, testLabels, testRecordType , testLength = LoadData3.loadData2('KDDTestThree.csv')
print('Testing Data ripped')
#print(testData)
print(testLabels)
encodedTestLabels = dataManagement._oneHotData(testLabels, 5)
#print(encodedTestLabels)
#print(max(testRecordType))
#print(testLength)

learning_rate = 0.000001
training_epochs = 4000
display_step = 50 
n_samples = data.size/7
n_hidden_1 = 1024
n_hidden_2 = 1024 
n_hidden_3 = 1024
n_input = 7
n_classes = 5
print("Number of samples ", n_samples)

x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])

def multilayer_perceptron(x, weights, biases):
    #Hidden Layer 1
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    #Hidden Layer 2
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    #Hidden Layer 3
    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    layer_3 = tf.nn.relu(layer_3)
    #Output Layer
    out_layer = tf.matmul(layer_3, weights['out']) + biases['out']
    return out_layer

#Store weights and biases
weights = {
        'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
        'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
        'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
        'out': tf.Variable(tf.random_normal([n_hidden_3, n_classes]))
        }
biases = {
        'b1': tf.Variable(tf.random_normal([n_hidden_1])),
        'b2': tf.Variable(tf.random_normal([n_hidden_2])),
        'b3': tf.Variable(tf.random_normal([n_hidden_3])),
        'out': tf.Variable(tf.random_normal([n_classes]))
        }

pred = multilayer_perceptron(x, weights, biases)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(n_samples)
        #for i in range(total_batch):
           # batch_x, batch_y = data[i], encodedTrainLabels[i]
        _, c = sess.run([optimizer, cost], feed_dict={x: data, y: encodedTrainLabels})
        avg_cost += c / total_batch
        #print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
    print("Optimization Finished!")
    
    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(accuracy.eval(feed_dict={x: testData, y: encodedTestLabels}))



                     
