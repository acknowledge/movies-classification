# -*- coding: utf-8 -*-
import requests, json

def extractMovieList(fname):

    with open(fname) as f:
        content = f.readlines()
    
    title = []
    year = []
    grade = []
    genre = []

    for line in content:
        infos = line.split('  ')
        title.append(infos[0].replace('"',''))
        year.append(infos[1])
        grade.append(infos[3])
        genre.append(infos[4])

    return [title, year, grade, genre]

def getMovieDescriptions(movieTitles, fname):

    movieInfos = []
    base_url = "http://www.omdbapi.com/?plot=full&r=json&t="
    
    count = 0
    for title in movieTitles:
        print 'fetching ' + title
        url = base_url + title
        r = requests.get(url)
        movieInfos.append(r.json())
        count = count+1
        if count >= 50:
            break

    with open(fname, 'wb') as outfile:
        json.dump(movieInfos, outfile)

    print 'DONE : ', count, ' entries downloaded'

if __name__ == '__main__':

    movieList = extractMovieList('data1/movielist.txt')

    getMovieDescriptions(movieList[0], 'data2/moviedescriptions.json')
