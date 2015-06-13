# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pl
from matplotlib import cm
from loadData import readFile, extractArrays


def whatever():
    fname = 'data3/data10.json'

        #matrix = np.array([
        #    [0,0,0,12,2,0],  # valeurs pour le 1er film
        #    [0,0,0,12,2,0],  # valeurs pour le 2e film
        #    [0,0,0,12,2,0]
        #    ])
              # valeur pour un mot

    infos = readFile(fname)
    titles, words, matrix = extractArrays(infos)

    print titles

    #words=['d', 's', 'a']
    #np.histogram(['a','a','s'])
    '''x = np.array([[1,0],[4,0]])
    print x.sum(axis=0)
    print x.sum(axis=1)
    pl.hist(x.sum(axis=0))
    pl.show()

    pl.hist(x.sum(axis=1))
    pl.show()'''

    pl.hist(matrix.sum(axis=0), bins=140)
    pl.show()

    word_counts = matrix.sum(axis=0)
    word_mask = word_counts > 1

    words = np.array(words)
    matrix[:,word_mask]
    words[word_mask]

    print matrix.shape
    print words
    print matrix[:,word_mask].shape
    print words[word_mask].shape

def printSizeOfMatrix(fname):
    infos = readFile(fname)
    titles, words, matrix = extractArrays(infos)

    print matrix.shape

def displayHistoOfMatrix(fname):
    infos = readFile(fname)
    titles, words, matrix = extractArrays(infos)

    #pl.hist(matrix.sum(axis=0), bins=120, range=(0, 120))
    pl.hist(matrix.sum(axis=0), bins=120)
    pl.show()

    #x = matrix.sum(axis=0)
    #print 'min : ', x.min()
    #print 'max : ', x.max()

if __name__ == '__main__':

    #whatever()

    #printSizeOfMatrix('data4/data1.json')
    #printSizeOfMatrix('data4/data3.json')
    #printSizeOfMatrix('data4/data5.json')
    #printSizeOfMatrix('data4/data10.json')
    #printSizeOfMatrix('data4/data50.json')
    #printSizeOfMatrix('data4/data100.json')
    #printSizeOfMatrix('data4/data500.json')

    #printSizeOfMatrix('data4/data3393.json')
    #printSizeOfMatrix('data3/data3393.json')
    
    #displayHistoOfMatrix('data5/data3393.json')
    #displayHistoOfMatrix('data4/data3393.json')
    #displayHistoOfMatrix('data3/data3393.json')