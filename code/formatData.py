# -*- coding: utf-8 -*-
import json
import numpy as np

def extractFromFile():
    fname = 'data/moviedescriptions3.json'
    file = open(fname, 'r')
    array =  file.read()
    data  = json.loads(array)
    
    # remove element that doesn't have the Title or Plot fields
    data = [item for item in data if 'Title' in item and 'Plot' in item]

    return data

def formatTitle(data):
    titles = []
    for movie in data:
        titles.append(movie['Title'])
    return titles

def formatWords(data, minOccurence, maxOccurence):
    words = []
    for movie in data:
        word_list = movie['Plot'].split()
        for word in word_list:
            if word not in words:
                words.append(word)

    print 'There is ', len(words), ' words in the initial list.'

    # filter the words that have to much or not enough occurences 
    lowQuantity = 0
    highQuantity = 0
    for w in words[:]:
        count = 0

        for movie in data:
            movie_words = movie['Plot'].split()
            for word in movie_words:
                if w == word:
                    count = count + 1
        print w, count
        if count < minOccurence or count > maxOccurence:
            if count < minOccurence:
                lowQuantity = lowQuantity + 1
                print 'the word is ', w
            else:
                highQuantity = highQuantity + 1
            words.remove(w)


    print 'Words with less occurrences than ', minOccurence, ' : ', lowQuantity
    print 'Words with more occurrences than ', maxOccurence, ' : ', highQuantity
    print 'There is ', len(words), ' words in the final list.'

    # TODO : enlever les '.', '"', '?'
    return words

def generateMatrix(data, words):
    matrix = []
    for word in words:
        line = []
        for movie in data:
            count = 0
            word_list = movie['Plot'].split()
            for w in word_list:
                if w == word:
                    count = count + 1
            line.append(count)
        matrix.append(line)
    return matrix


if __name__ == '__main__':

    movies_data = extractFromFile()

    movies_title = formatTitle(movies_data)
    #print movies_title
    # format : movies = ["asdf", "asdfsadf", ...]

    minOccurence = 2
    maxOccurence = 100
    movies_words = formatWords(movies_data, minOccurence, maxOccurence)
    #print movies_words
    # format : words = ["le", "caca"]
    #for m in movies_words:
    #    print m

    movies_matrix = generateMatrix(movies_data, movies_words)
    matrix = np.array(movies_matrix)
    #for m in matrix:
    #    print m
    #print matrix

    # format : matrix = np.array([
            #    [0,0,0,12,2,0],  # valeurs pour le 1er mot
            #    [0,0,0,12,2,0],  # valeurs pour le 2e mot
            #    [0,0,0,12,2,0]
            #    ])
                  # valeur pour un film
