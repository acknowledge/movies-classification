from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.neighbors import KNeighborsClassifier

examples = range(meta.shape[0]) # list with all the images
data = []
target = []

# extraction of the features for each image
for i, idx in enumerate(examples): 
    img = load_img(meta.iloc[idx]['basename'])
    
    # curvature hist values (1st feature list)
    c = curvature_hist(img, step=10, plot=False)
    # hull ratio value (2nd feature)
    h = hull_ratio(img)
    
    features = np.array([h])
    features = np.append(features, c)
    data.append(features)
    
    target.append(meta.iloc[idx]['classid']) # row vector

data = np.array(data) # conversion to numpy array

lencoder = preprocessing.LabelEncoder()
lencoder.fit(target)
target = lencoder.transform(target) # transform classids from string to int
target = target.reshape(-1,1) # transform to colummn vector

# split datas to train and test
X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, target, test_size=0.4, random_state=0)

#print 'data : ', data.shape
#print 'train : ', X_train.shape, y_train.shape
#print 'target : ', target.shape
#print 'test : ', X_test.shape, y_test.shape

# normalizing the datas
#  --> useless in our case (all values are already between 0 and 1)
#min_max_scaler = preprocessing.MinMaxScaler()
#X_train_minmax = min_max_scaler.fit_transform(X_train)

# building the classifier and train the dataset 
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train.ravel()) 
print 'DONE'