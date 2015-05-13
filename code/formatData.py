# -*- coding: utf-8 -*-
import json

def extractFromFile():
    fname = 'moviedescriptions101.json'
    file = open(fname, 'r')
    array =  file.read()
    data  = json.loads(array)
    
    # remove element that doesn't have the Title or Plot fields
    data = [item for item in data if 'Title' in item and 'Plot' in item]

    return data

def formatTitle(data):
    titles = []
    for movie in data:
        #if 'Title' in movie:
        titles.append(movie['Title'])
    return titles

def formatWords(data):
    words = []
    for movie in data:
        #if 'Plot' in movie :
        word_list = movie['Plot'].split()
        for word in word_list:
            if word not in words:
                words.append(word)

    # filter the words that have to much or not enough occurences 
    for w in word_list:
        asdf

    return words

def generateMatrix(data, words):
    matrix = []
    for word in words:
        line = []
        for movie in data:
            count = 0
            #if 'Plot' in movie:
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
    print movies_title
    # format : movies = ["asdf", "asdfsadf", ...]
    movies_words = formatWords(movies_data)
    print movies_words
    # format : words = ["le", "caca"]
    movies_matrix = generateMatrix(movies_data, movies_words)
    for m in movies_matrix:
        print m
    #print movies_matrix
    # format : matrix = np.array([
            #    [0,0,0,12,2,0],  # valeurs pour le 1er mot
            #    [0,0,0,12,2,0],  # valeurs pour le 2e mot
            #    [0,0,0,12,2,0]
            #    ])
                  # valeur pour un film
