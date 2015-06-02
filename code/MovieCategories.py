# -*- coding: utf-8 -*-

class MovieCategories:

    def __init__(self):

        print 'Extract movie categories from file...'
        fname = 'data1/movielist.txt'
        with open(fname) as f:
            content = f.readlines()

        self.movieCategories = {}

        for line in content:
            infos = line.split('  ')
            #title.append(infos[0].replace('"',''))
            #year.append(infos[1])
            #grade.append(infos[3])
            #genre.append(infos[4])
            self.movieCategories[infos[0].replace('"','')] = infos[4];

        print 'Done.'

    def getCategory(self, movieTitle):
        return self.movieCategories[movieTitle]

if __name__ == '__main__':

    # THIS HOW TO USE THIS CLASS :

    cat = MovieCategories()

    print 'Fever Pitch﻿ : ', cat.getCategory('Fever Pitch﻿')
    print 'Star Trek : ', cat.getCategory('Star Trek﻿')
    print 'Outlander﻿ : ', cat.getCategory('Outlander﻿')
    print 'The Emperor\'s New Groove﻿ : ', cat.getCategory('The Emperor\'s New Groove﻿')
    print 'Roger & Me﻿ : ', cat.getCategory('Roger & Me﻿')