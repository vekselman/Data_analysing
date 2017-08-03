import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import os
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')
df = pd.read_csv(os.curdir + '/Datasets/wheat.data',header=0,index_col=0,delimiter=',')

#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..



fig = plt.figure()
plt.suptitle('Area X Perimeter X Asymmetry')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Asymmetry')
ax.scatter(df.area,df.perimeter,df.asymmetry,c='red')
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..


fig = plt.figure()
plt.suptitle('Width X Groove X Length')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Width')
ax.set_ylabel('Groove')
ax.set_zlabel('Length')
ax.scatter(df.width,df.groove,df.length,c='red')
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..


plt.show()


