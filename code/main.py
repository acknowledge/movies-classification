# -*- coding: utf-8 -*-
import requests, json

def extractMovieList():

    fname = 'movielist.txt'
    with open(fname) as f:
        content = f.readlines()
    
    title = []
    year = []
    grade = []
    genre = []

    for line in content:
        infos = line.split('  ')
        title.append(infos[0])
        year.append(infos[1])
        grade.append(infos[3])
        genre.append(infos[4])

    return [title, year, grade, genre]

def getMovieDescriptions(movieList):

    base_url = "http://www.omdbapi.com/?plot=full&r=json&t=Just Like Heaven﻿"

    #data = json.dumps({'name':'test', 'description':'some test repo'}) 
    #r = requests.post(github_url, data, auth=('user', '*****'))
    r = requests.get(base_url)

    print r.json()['Plot']
    return




if __name__ == '__main__':

    movieList = extractMovieList()

    getMovieDescriptions(movieList[0])


    #for t in movieList[0]:
     #   print t