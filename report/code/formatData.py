# -*- coding: utf-8 -*-
import json
import numpy as np
import re
from nltk.corpus import stopwords
import os.path


def extractFromFile(fname):
    file = open(fname, 'r')
    array =  file.read()
    data  = json.loads(array)
    # remove element that doesn't have the Title or imdbID fields
    data = [item for item in data if 'Title' in item and 'imdbID' in item]
    return data

def formatTitle(data):
    print 'Generating title list...'
    titles = []
    i = 0;
    for movie in data:
        fname = 'data2/synopsis/' + movie['imdbID'] + '.txt'
        # if synopsis file exists
        if os.path.isfile(fname):
            titles.append(movie['Title'])
            i = i + 1
    print 'There is ' + str(i) + ' movies.'
    return titles

def formatWords(data):
    print 'Generating word list...'
    words = []
    for movie in data:
        fname = 'data2/synopsis/' + movie['imdbID'] + '.txt'
        # if synopsis file exists
        if os.path.isfile(fname):
            synopsis = ''
            with open(fname, 'r') as thefile:
                synopsis = thefile.read().replace('\n', '')

            synopsis = synopsis.lower()
            # clean words
            word_list = re.findall(r'\w+', synopsis, flags = re.UNICODE | re.LOCALE) 
            # remove the stopwords
            word_list = filter(lambda x: x not in stopwords.words('english'), word_list)
            for word in word_list:
                #word = clean(word)
                if word not in words:
                    words.append(word)
    print 'There is ', len(words), ' words in the list.'
    return words

def generateMatrix(data, words):
    print 'Generating matrix...'
    matrix = []
    i = 0
    
    for movie in data:
        i = i + 1
        fname = 'data2/synopsis/' + movie['imdbID'] + '.txt'
        # if synopsis file exists
        if os.path.isfile(fname):
            print 'movie ' + str(i) + ' on ' + str(len(data))
            line = []
            synopsis = ''
            with open(fname, 'r') as thefile:
                synopsis = thefile.read().replace('\n', '')

            synopsis = synopsis.lower()
            word_list = re.findall(r'\w+', synopsis, flags = re.UNICODE | re.LOCALE) 
            word_list = filter(lambda x: x not in stopwords.words('english'), word_list)
            for word in words:
                count = 0

                for w in word_list:
                    if w == word:
                        count = count + 1
                line.append(count)

            matrix.append(line)
        else :
            print 'movie ' + str(i) + ' has no synopsis'
    print 'Done.'
    return matrix

def saveToFile(titles, words, matrix, fname):
    print 'Saving data to file...'
    output = {}
    output['titles'] = titles
    output['words'] = words
    output['matrix'] = matrix
    
    #output_fname = 'data3/datatest.json'
    with open(fname, 'w') as outfile:
        json.dump(output, outfile)
    print 'Done.'

if __name__ == '__main__':

    #dataset = [1, 3, 5, 10, 50, 100]#, 500, 3393]
    dataset = [3393]

    for n in dataset:
        fname = 'data2/moviedescriptions' + str(n) + '.json'
        movies_data = extractFromFile(fname)

        # creation of the array with movies titles
        movies_titles = formatTitle(movies_data)
        # format : movies = ["asdf", "asdfsadf", ...]

        # creation of the array with all the words
        movies_words = formatWords(movies_data)
        # format : words = ["a word", "another word", ...]

        # creation of the matrix (occurrence of words in each movie)
        movies_matrix = generateMatrix(movies_data, movies_words)
        # format : matrix = np.array([
                #    [0,0,0,12,2,0],  # values for the first movie
                #    [0,0,0,12,2,0],  # values for the second movie
                #    [0,0,0,12,2,0]
                #    ])
                      # values for a word

        output_fname = 'data3/data' + str(n) + '.json'
        saveToFile(movies_titles, movies_words, movies_matrix, output_fname)
        
        