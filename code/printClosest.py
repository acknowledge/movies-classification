import heapq


def printClosest(idxFilm, numclosest, distanceMatrix, titles):
    print titles[idxFilm]+":"
    cloasest= heapq.nsmallest(numclosest,range(len(distanceMatrix[idxFilm])),distanceMatrix[idxFilm].take)
    for idx, val in enumerate(cloasest):
        print  "\t"+str(idx)+" "+titles[val]