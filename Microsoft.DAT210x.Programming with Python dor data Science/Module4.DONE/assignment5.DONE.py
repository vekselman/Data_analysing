import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import random, math
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

import os
pics = []
picsi = []
directory = os.getcwd() + '\\Datasets\\ALOI\\32'
directoryi = os.getcwd() + '\\Datasets\\ALOI\\32i'
def Plot2D(T, title, x, y, num_to_plot=40,img_show=True):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  if img_show:
      x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
      y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
      for i in range(num_to_plot):
        img_num = int(random.random() * img_c)
        x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
        x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
        img = df_pics.iloc[img_num,:].reshape(rows, colls)
        ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7)
def Plot3D(T, title, x, y, z, num_to_plot=40):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  ax.set_zlabel('Component: {0}'.format(z))
  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y],T[:,z], marker='.',alpha=0.7)
#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for pic_ in os.listdir(directory):
    buff = misc.imread(directory+'\\'+ pic_)
    pics.append(buff)
print(len(pics[0]))
df_pics = pd.DataFrame(np.array(pics).reshape(72,144*192))
print(df_pics.iloc[0,0])
plt.imshow(pics[0],cmap='gray')
plt.imshow(df_pics.iloc[0,:].reshape(144,192),cmap='gray')


from sklearn.manifold import Isomap
iso = Isomap(n_neighbors=2,n_components=3)
df_iso = iso.fit_transform(df_pics)


Plot2D(df_iso,'Isomap 2 dimens', 0, 1)
Plot2D(df_iso,'Isomap 2 dimens', 0, 2)
Plot2D(df_iso,'Isomap 2 dimens', 1, 2)
Plot3D(df_iso,'Isomap 3 dimens', 0, 1,2)

for pic_ in os.listdir(directoryi):
    buff = misc.imread(directoryi+'\\'+ pic_)
    pics.append(buff)
img_c, rows, colls = np.array(pics).shape
print(img_c,rows,colls)
df_pics_i = pd.DataFrame(np.array(pics).reshape(img_c,rows*colls))

iso_i = Isomap(n_neighbors=6, n_components=3)
df_iso_i = iso_i.fit_transform(df_pics_i)


Plot2D(df_iso_i,'Isomap with i 2 dimens', 0, 1,False)
Plot2D(df_iso_i,'Isomap with i 2 dimens', 0, 2,False)
Plot2D(df_iso_i,'Isomap with i 2 dimens', 1, 2,False)
Plot3D(df_iso_i,'Isomap with i 3 dimens', 0, 1,2)
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 


#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 



#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

