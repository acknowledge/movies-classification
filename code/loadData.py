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
