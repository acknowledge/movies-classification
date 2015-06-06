# -*- coding: utf-8 -*-
import json
import numpy as np
from loadData import readFile, extractArrays

def saveToFile(titles, words, matrix, fname):
    print 'Saving data to file...'
    output = {}
    output['titles'] = titles
    output['words'] = words
    output['matrix'] = matrix

    with open(fname, 'w') as outfile:
        json.dump(output, outfile)
    print 'Done.'

def applyTFIDF(matrix):

    # Information about the matrix construction : 
    # matrix = np.array([
    #    [0,0,0,12,2,0],  # valeurs pour le 1er film
    #    [0,0,0,12,2,0],  # valeurs pour le 2e film
    #    [0,0,0,12,2,0]
    #    ])
          # valeur pour un mot

    #	idf = log(N/nf)
    #	N = nombre de documents --> films
    #	nf = nombre de documents où le terme apparait --> nbr de films ou le mot apparait

    tf = matrix
    N = matrix.shape[0]
    matrix_mask = matrix > 0
    nf = matrix_mask.sum(axis=0)
    idf = np.log10(nf*(1.0/N))
    tfidf = tf * idf
    #print tfidf
    #print tfidf.shape

    # TEST WITH A TINY MATRIX
    '''
    print 'N', N
    print '1/N', 1.0/N
    mat = np.array([[1,0,0,0],[1,1,2,0],[1,0,0,1]])
    tf = mat
    print 'matrix', mat
    mask = mat > 0
    print 'mask', mask
    nf = mask.sum(axis=0)
    print 'nf', nf
    div = nf*(1.0/N)
    print 'N/nf', div
    idf = np.log10(div)
    print 'idf', idf

    print tf.shape
    print idf.shape
    tfidf = tf * idf
    print tfidf
    print tfidf.shape
    '''
    # END TEST

    return tfidf

if __name__ == '__main__':

    # THIS CODE LOAD 3 ARRAYS FROM A FILE FROM THE FOLDER 'data4'
    # The arrays are 'titles', 'words' and 'matrix'
    # The TF;IDF algorithm is applied and data is saved in the folder 'data5'
    

    #dataset = [1, 3, 5, 10, 50, 100]#, 3393]
    dataset = [3393]
    #dataset = [3]

    for n in dataset:
        fname = 'data4/data' + str(n) + '.json'
        infos = readFile(fname)
        titles, words, matrix = extractArrays(infos)



        # apply filter
        matrix = applyTFIDF(matrix)

        matrix = matrix.tolist()
        
        print 'Data loaded'
        output_fname = 'data5/data' + str(n) + '.json'
        saveToFile(titles, words, matrix, output_fname)

        print 'File \'' + output_fname + '\' saved.' 
        