from hcluster import linkage, dendrogram
from sklearn.metrics.pairwise import pairwise_distances
from MovieCategories import MovieCategories
from loadData import  readFile, extractArrays
import pylab
## Function to perform hierarchical clustering on the matrix with titles of films
def performHierarchicalClusterin(matrix, titlesCat):
    #compute the distance matrix with "cosine" metric
    distanceMatrix =pairwise_distances(matrix, metric='cosine')
    #Computer the hierarchical clutering, similaritiy with cluster
    #is caclulated with the average of element similarities
    Z=linkage(distanceMatrix,method='average')
    #Create a dendogram image
    image=dendrogram(Z,labels=titlesCat, distance_sort='descendent',
                     leaf_font_size=2, orientation='left', show_contracted=False)
    #Save generated dendogram image
    pylab.savefig("images/clusteringImage.png",dpi=300,bbox_inches='tight')
## Function to print most similar cluastering of unique films    
def printMostSimilarCluster(matrix, titlesCat): 
    #compute the distance matrix with "cosine" metric
    distanceMatrix =pairwise_distances(matrix, metric='cosine')
    #Computer the hierarchical clutering, similaritiy with cluster
    #is caclulated with the average of element similarities
    Z=linkage(distanceMatrix,method='average')#,method='centroid')
    print "first closest cluster\n"
    for idx in range(10):
        lenTitle=len(titlesCat)
        if (int(Z[idx,0])<lenTitle) & (int(Z[idx,1])<lenTitle):
            print "itr "+str(idx)+":\n"+titlesCat[int(Z[idx,0])]+" "+titlesCat[int(Z[idx,1])]
            
if __name__ == '__main__':
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
        
    #perform hierarchical clustteing and print most similar clusters
    performHierarchicalClusterin(matrix,titlesCat)
    printMostSimilarCluster(matrix,titlesCat)
        