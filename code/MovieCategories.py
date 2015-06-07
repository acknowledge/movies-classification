# -*- coding: utf-8 -*-
import codecs
from loadData import readFile, extractArrays

class MovieCategories:

    def __init__(self):

        print 'Extract movie categories from file...'
        fname = 'data1/movielist.txt'
        with codecs.open(fname,'r') as f:
            content = f.readlines()

        self.movieCategories = {}

        for line in content:
            infos = line.split('  ')
            #title.append(infos[0].replace('"',''))
            #year.append(infos[1])
            #grade.append(infos[3])
            #genre.append(infos[4])
            self.movieCategories[infos[0].replace('"','').replace('\xef\xbb\xbf','')] = infos[4];

        print 'Done.'

    def getCategory(self, movieTitle):
        if movieTitle in self.movieCategories:
            return self.movieCategories[movieTitle]
        else:
            return ''

if __name__ == '__main__':

    # THIS HOW TO USE THIS CLASS :

    cat = MovieCategories()

    fname = 'data4/data50.json'
    infos = readFile(fname)
    titles, words, matrix = extractArrays(infos)

    for t in titles:
        print t, cat.getCategory(t)

    #for x in cat.movieCategories:
    #    print x, cat.getCategory(x)

    #print 'Fever Pitch﻿ : ', cat.getCategory('Fever Pitch﻿')
    #print 'Star Trek : ', cat.getCategory('Star Trek﻿')
    #print 'Outlander﻿ : ', cat.getCategory('Outlander﻿')
    #print 'The Emperor\'s New Groove﻿ : ', cat.getCategory('The Emperor\'s New Groove﻿')
    #print 'Roger & Me﻿ : ', cat.getCategory('Roger & Me﻿')

