# -*- coding: utf-8 -*-
import json
import numpy as np

def readFile(fname):
    file = open(fname, 'r')
    array =  file.read()
    data  = json.loads(array)
    return data

def extractArrays(data):
    titles = data['titles']
    words = data['words']
    matrix = data['matrix']
    matrix = np.array(matrix)

    return titles, words, matrix


if __name__ == '__main__':

    # THIS CODE LOAD 3 ARRAYS FROM A FILE FROM THE FOLDER 'data3'
    # The arrays are 'titles', 'words' and 'matrix'
    # They are used as input for the Self-Organizing Map

    fname = 'data3/data5-2-100.json'

    infos = readFile(fname)
    titles, words, matrix = extractArrays(infos)

    print titles
    print words
    print matrix
    