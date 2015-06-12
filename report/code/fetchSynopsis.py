# -*- coding: utf-8 -*-
import requests
import json
import BeautifulSoup
import re
import os.path

def extractFromFile(fname):
    file = open(fname, 'r')
    array =  file.read()
    data  = json.loads(array)
    
    # remove element that doesn't have the Title or imdbID fields
    data = [item for item in data if 'Title' in item and 'imdbID' in item]

    return data

def extractSynopsis(imdbId):
    url = 'http://www.imdb.com/title/' + imdbId + '/synopsis'
    r = requests.get(url)

    soup = BeautifulSoup.BeautifulSoup(r.text)
    div = soup.find("div", {"id": "swiki.2.1"})
    if div :
        synopsis = re.sub('<[^<]+?>', '', div.text)
        if synopsis:
            return synopsis

    return None

if __name__ == '__main__':
    
    # n --> 1, 3, 5, 10, 50, 100, 3393
    n = 3393

    fname = 'data2/moviedescriptions' + str(n) + '.json'
    movies_data = extractFromFile(fname)

    i = 0
    emptyQty = 0
    for movie in movies_data:
        i = i + 1
        imdbId = movie['imdbID']
        fname = 'data2/synopsis/' + imdbId + '.txt'
        if not os.path.isfile(fname):
            print str(i) + '/' + str(n) + ' : ' + imdbId
            synopsis = extractSynopsis(imdbId)
            if synopsis:
                f = open(fname,"w")
                f.write(synopsis.encode('utf8'))
                f.close()
            else:
                emptyQty = emptyQty + 1
                print imdbId + ' synopsis is empty (' + str(emptyQty) + ')'

    print 'Total empty synopsis : ' + str(emptyQty)
    print 'Total synopsis : ' + str(n - emptyQty)