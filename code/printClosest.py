import heapq
from MovieCategories import MovieCategories
from loadData import  readFile, extractArrays
from sklearn.metrics.pairwise import pairwise_distances
import sys

def printClosest(idxFilm, numclosest, distanceMatrix, titles):
    print titles[idxFilm]+":"
    cloasest= heapq.nsmallest(numclosest,range(len(distanceMatrix[idxFilm])),distanceMatrix[idxFilm].take)
    for idx, val in enumerate(cloasest):
        print  "\t"+str(idx)+" "+titles[val]

      
if __name__ == '__main__':
    if(len(sys.argv)<2):
        print "Usage: python ./printClosest.py index_film num_closest_film"
    else:
        fname = 'data5/data50.json'
        infos = readFile(fname)
        titles, words, matrix = extractArrays(infos)
        cat=MovieCategories()
        cat.getCategory(titles[2])
        titlesCat=[None] * len(titles)
        category=[None] * len(titles)
        for idx, val in enumerate(titles):
            titlesCat[idx]=titles[idx]+":"+cat.getCategory(titles[idx])
            category[idx]=cat.getCategory(titles[idx])
        distanceMatrix =pairwise_distances(matrix, metric='cosine')
        printClosest(int(sys.argv[1]),int(sys.argv[2]),distanceMatrix,titlesCat)
        
