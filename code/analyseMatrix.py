# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pl
from matplotlib import cm
from loadData import  readFile, extractArrays

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

# faire TF-IDF