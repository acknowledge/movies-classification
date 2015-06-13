import heapq
from MovieCategories import MovieCategories
from loadData import  readFile, extractArrays
from sklearn.metrics.pairwise import pairwise_distances
import sys

#Print "numClosest" closest films to film with id "idxFilm" in relation of the matrix of words tfidf 
#The similariti it's caculated with the "cosine" metric
def printClosest(idxFilm, numclosest, matrix, titles):
    #compute the distance matrix with "cosine" metric
    distanceMatrix =pairwise_distances(matrix, metric='cosine')
    print titles[idxFilm]+":"
    #Get id of smallest films on the distanceMatrx
    cloasest= heapq.nsmallest(numclosest,range(len(distanceMatrix[idxFilm])),distanceMatrix[idxFilm].take)
    #print closest films
    for idx, val in enumerate(cloasest):
        print  "\t"+str(idx)+" "+titles[val]

      
if __name__ == '__main__':
    if(len(sys.argv)<2):
        print "Usage: python ./printClosest.py index_film num_closest_film"
    else:
        #read data of films name, matrix of tfidf of words, and list of words
        fname = 'data5/data50.json'
        infos = readFile(fname)
        titles, words, matrix = extractArrays(infos)
        #Get category of films
        cat=MovieCategories()
        cat.getCategory(titles[2])
        titlesCat=[None] * len(titles)
        category=[None] * len(titles)
        for idx, val in enumerate(titles):
            titlesCat[idx]=titles[idx]+":"+cat.getCategory(titles[idx])
            category[idx]=cat.getCategory(titles[idx]) 
        #print closest cluster to the film with id on argument 1    
        printClosest(int(sys.argv[1]),int(sys.argv[2]),matrix,titlesCat)
        
