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

def removeLonelyWords(words, matrix):

	word_counts = matrix.sum(axis=0)
	word_mask = word_counts > 1

	# convert words to numpy array
	words = np.array(words)

	print 'Taille matrix avant : ' + str(matrix.shape)
	print 'Taille words avant : ' + str(words.shape)
	
	matrix = matrix[:,word_mask]
	words = words[word_mask]

	print 'Taille matrix avant : ' + str(matrix.shape)
	print 'Taille words avant : ' + str(words.shape)

	return words.tolist(), matrix

if __name__ == '__main__':

    # THIS CODE LOAD 3 ARRAYS FROM A FILE FROM THE FOLDER 'data3'
    # The arrays are 'titles', 'words' and 'matrix'
    # They are filtered and saved in the folder 'data4'
    

    #dataset = [1, 3, 5, 10, 50, 100]#, 3393]
    #dataset = [3393]
    dataset = [3]

    for n in dataset:
        fname = 'data3/data' + str(n) + '.json'
        infos = readFile(fname)
    	titles, words, matrix = extractArrays(infos)

    	# apply filter
    	words, matrix = removeLonelyWords(words, matrix)

    	matrix = matrix.tolist()
        
        output_fname = 'data4/data' + str(n) + '.json'
        saveToFile(titles, words, matrix, output_fname)

        print 'File \'' + output_fname + '\' saved.' 
        