# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:51:17 2015

@author: simo
"""

import numpy as np
import matplotlib.pyplot as pl
from matplotlib import cm
from loadData import  readFile, extractArrays

fname = 'data3/data100-2-100.json'

infos = readFile(fname)
titles, words, matrix = extractArrays(infos)
matrix = np.transpose(matrix)

pl.figure(figsize=(5,5))
pl.xticks(np.arange(matrix.shape[1]), words, rotation=45)
pl.yticks(np.arange(matrix.shape[0]), titles)
pl.title("titles")
pl.imshow(matrix, interpolation='nearest', cmap=cm.binary)
_ = pl.savefig('titles.png')


import kohonen
from Utils import computeUMatrix, constructSamplesForNeurons, ExponentialTimeseries as ET
from random import shuffle

## Initializes the Kohonen map as a rectangular map of len(titles) x len(titles)*2
def cosine_metric(x, y):
    '''Returns the cosine distance between x and y.'''
    nx = numpy.sqrt(numpy.sum(x * x, axis=-1))
    ny = numpy.sqrt(numpy.sum(y * y, axis=-1))
    # the cosine metric returns 1 when the args are equal, 0 when they are
    # orthogonal, and -1 when they are opposite. we want the opposite effect,
    # and we want to make sure the results are always nonnegative.
    return 1 - numpy.sum(x * y, axis=-1) / nx / ny

side = len(titles)
params = kohonen.Parameters(dimension=len(words), shape=(side,side*2), metric=cosine_metric)
kmap = kohonen.Map(params)

## Learns the dataset n_iter times in a randomly defined order
## The learning rate decreases exponentially from 1 to 0.2
n_iter = 20
kmap._learning_rate = ET(1, 0.2, n_iter*matrix.shape[0])
kmap._neighborhood_size = ET(4./3*side, 1, n_iter*matrix.shape[0])
for i in range(0,n_iter):
    order = np.arange(0, matrix.shape[0], 1)
    shuffle(order)
    for j in order:
        kmap.learn(matrix[j])

## Computes distance between neurons and creates a U-Matrix (of 2*len(titles) x len(titles)*4)
u_matrix = computeUMatrix(kmap)

# Creates a colormap for the U-Matrix
colors = cm.Spectral_r
colors.set_bad('w',1.)

## Gets winning neuron for each sample (1-nn)
animalDict = constructSamplesForNeurons(kmap, matrix)

## Prints U-Matrix
fig = pl.figure(figsize=(40,80))

pl.imshow(u_matrix, cmap=colors, interpolation="nearest")
pl.colorbar(shrink=0.2)

## Prints titles on map
for neuron in animalDict:
    neuronx, neurony = neuron.split(",")
    neuronx = int(neuronx) * 2
    neurony = int(neurony) * 2
    pl.scatter(neurony, neuronx)
    animalNames = ""
    for animalID in animalDict[neuron]:
        animalNames += titles[animalID] + "\n"
    pl.annotate(animalNames, (neurony, neuronx), size=10)

pl.axis('off')

_ = pl.savefig("Results_Films.png", bbox_inches = 'tight')