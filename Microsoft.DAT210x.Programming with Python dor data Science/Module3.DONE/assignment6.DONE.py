import pandas as pd
import matplotlib.pyplot as plt
import os

#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv(os.curdir + '/Datasets/wheat.data',header=0,index_col=0,delimiter=',')

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..


#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
print(df.corr())

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(df.corr(),cmap= plt.cm.Blues, interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(df.columns)),df.columns,rotation=45)
plt.yticks(range(len(df.columns)),df.columns)
plt.show()


