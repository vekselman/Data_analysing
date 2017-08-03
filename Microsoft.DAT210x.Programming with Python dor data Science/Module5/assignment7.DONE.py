# If you'd like to try this lab with PCA instead of Isomap,
# as the dimensionality reduction technique:
#Test_PCA = True
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import pandas as pd
import numpy as np

def plotDecisionBoundary(model, X, y,title = ''):
  print "Plotting..."
  import matplotlib.pyplot as plt
  import matplotlib
  matplotlib.style.use('ggplot') # Look Pretty

  fig = plt.figure()
  ax = fig.add_subplot(111)

  padding = 0.1
  resolution = 0.1

  #(2 for benign, 4 for malignant)
  colors = {2:'royalblue',4:'lightsalmon'} 

  
  # Calculate the boundaris
  x_min, x_max = X[:, 0].min(), X[:, 0].max()
  y_min, y_max = X[:, 1].min(), X[:, 1].max()
  x_range = x_max - x_min
  y_range = y_max - y_min
  x_min -= x_range * padding
  y_min -= y_range * padding
  x_max += x_range * padding
  y_max += y_range * padding

  # Create a 2D Grid Matrix. The values stored in the matrix
  # are the predictions of the class at at said location
  import numpy as np
  xx, yy = np.meshgrid(np.arange(x_min, x_max, resolution),
                       np.arange(y_min, y_max, resolution))

  # What class does the classifier say?
  Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)

  # Plot the contour map
  plt.contourf(xx, yy, Z, cmap=plt.cm.seismic)
  plt.axis('tight')

  # Plot your testing points as well...
  for label in np.unique(y):
    indices = np.where(y == label)
    plt.scatter(X[indices, 0], X[indices, 1], c=colors[label], alpha=0.8)

  p = model.get_params()
  plt.title(title + 'K = ' + str(p['n_neighbors']))
  plt.show()


# 
# TODO: Load in the dataset, identify nans, and set proper headers.
# Be sure to verify the rows line up by looking at the file in a text editor.
#
# .. your code here ..
df = pd.read_csv('Datasets/breast-cancer-wisconsin.data',header=None,delimiter=',')
columns = ['sample', 'thickness', 'size', 'shape', 'adhesion', 'epithelial', 
           'nuclei', 'chromatin', 'nucleoli', 'mitoses', 'status']
df.columns = columns
df.set_index('sample',inplace=True)

#copy Status and drop from dataframe
y = df['status'].copy()
df.drop(['status'],axis=1,inplace=True)

#Check Df column types. If object, convert to numerical and coerce missing vals to Nan
for col in df.columns:
    if df[col].dtypes == 'object':
        df[col] = pd.to_numeric(df[col],errors='coerce')

# 
# TODO: Copy out the status column into a slice, then drop it from the main
# dataframe. Always verify you properly executed the drop by double checking
# (printing out the resulting operating)! Many people forget to set the right
# axis here.
#
# If you goofed up on loading the dataset and notice you have a `sample` column,
# this would be a good place to drop that too if you haven't already.
#
# .. your code here ..



#
# TODO: With the labels safely extracted from the dataset, replace any nan values
# with the mean feature / column value
#
# .. your code here ..

#Check if has nans. If so, calcualte mean and replace
if df.isnull().any().any():
    for col in df.loc[:,df.isnull().any()].columns:
        mean = df[col].mean()
        df.loc[df[col].isnull(),col] = mean
        
#
# TODO: Do train_test_split. Use the same variable names as on the EdX platform in
# the reading material, but set the random_state=7 for reproduceability, and keep
# the test_size at 0.5 (50%).
#
# .. your code here ..
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df,y, test_size=0.5,
                                                 random_state=7)


#
# TODO: Experiment with the basic SKLearn preprocessing scalers. We know that
# the features consist of different units mixed in together, so it might be
# reasonable to assume feature scaling is necessary. Print out a description
# of the dataset, post transformation. Recall: when you do pre-processing,
# which portion of the dataset is your model trained upon? Also which portion(s)
# of your dataset actually get transformed?
#
# .. your code here ..

#ckeate variables with different parameters
#score all data,score and models
score_column = ['Scaler','Reductor','Reductor neigbors',
                      'Knn k','knn weight','Model ID','Score']
scores = []
models = {}
model_id = 1
#All stuff to iterate
from_i_k,to_i_k = 5,10
weights = ['uniform','distance']
iso_k = range(from_i_k,to_i_k+1)
knn_k = range(1,16)

from sklearn import preprocessing
scalers = {'no scaling': None,
           'MaxAbsScaler':preprocessing.MaxAbsScaler(),
           'MinMaxScaler':preprocessing.MinMaxScaler(),
           'StandardScaler':preprocessing.StandardScaler(),
           'Normalizer':preprocessing.Normalizer(),
           'RobustScaler':preprocessing.RobustScaler()}
no_scaling = 'no scaling'

reductors= ['PCA','Isomap']

#all models
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap
from sklearn.neighbors import KNeighborsClassifier


for scaler in scalers.items():
    
    train,test = None,None
    if scaler[0] != no_scaling:
        #print scaler[0]
        scaler[1].fit(X_train)
        train = scaler[1].transform(X_train)
        test = scaler[1].transform(X_test)
    else:
        train,test = X_train,X_test
    
    for reductor in reductors:
        
        if reductor == 'Isomap':
            kk = iso_k
        else:
            kk = [1]
            
        red = None    
        red = PCA(n_components = 2)# If Iso, it will be change below  
        for k in kk:# Neigbors in reductors
            if reductor == 'Isomap':
                red = Isomap(n_components=2, n_neighbors=k)
            red.fit(train)
            
            
            for weight in weights:#wieght method of knn
                for kn in knn_k:#Avary neighbor of Knn clasifaer
                    model = None
                    row = None
                    score = None
                    model = KNeighborsClassifier(n_neighbors=kn,weights=weight)
                    
                    model.fit(red.transform(train),y_train)
                    models[model_id] = [model,red.transform(test)]
                    score = model.score(red.transform(test),y_test)
                    
                    row= [scaler[0],reductor,k,kn,weight,model_id,score]
                    scores.append(row)
                    
                    model_id += 1
                    
                    
sc_df = pd.DataFrame(scores,columns = score_column)
sc_df.sort(['Score'],ascending=False).head()

#print for avery scaler Knn with best parameters

for sc in sc_df.Scaler.unique():
    buff = None
    mod = None
    buff = sc_df.loc[sc_df.Scaler == sc ,:].sort(['Score'],ascending=False).iloc[0,:]
    mod = models[buff['Model ID']]
    title = 'Scaler: ' + buff.Scaler+ '; Score:' + str(buff.Score) + ' ;' 
    print buff
    plotDecisionBoundary(mod[0], mod[1], y_test,title)
    
##
## PCA and Isomap are your new best friends
#
#if Test_PCA:
#  print "Computing 2D Principle Components"
#  #
#  # TODO: Implement PCA here. Save your model into the variable 'model'.
#  # You should reduce down to two dimensions.
#  #
#  # .. your code here ..
#
#  
#
#else:
#  print "Computing 2D Isomap Manifold"
#  #
#  # TODO: Implement Isomap here. Save your model into the variable 'model'
#  # Experiment with K values from 5-10.
#  # You should reduce down to two dimensions.
#  #
#  # .. your code here ..
#  



#
# TODO: Train your model against data_train, then transform both
# data_train and data_test using your model. You can save the results right
# back into the variables themselves.
#
# .. your code here ..



# 
# TODO: Implement and train KNeighborsClassifier on your projected 2D
# training data here. You can use any K value from 1 - 15, so play around
# with it and see what results you can come up. Your goal is to find a
# good balance where you aren't too specific (low-K), nor are you too
# general (high-K). You should also experiment with how changing the weights
# parameter affects the results.
#
# .. your code here ..



#
# INFO: Be sure to always keep the domain of the problem in mind! It's
# WAY more important to errantly classify a benign tumor as malignant,
# and have it removed, than to incorrectly leave a malignant tumor, believing
# it to be benign, and then having the patient progress in cancer. Since the UDF
# weights don't give you any class information, the only way to introduce this
# data into SKLearn's KNN Classifier is by "baking" it into your data. For
# example, randomly reducing the ratio of benign samples compared to malignant
# samples from the training set.



#
# TODO: Calculate + Print the accuracy of the testing set
#
# .. your code here ..


#plotDecisionBoundary(knmodel, X_test, y_test)
