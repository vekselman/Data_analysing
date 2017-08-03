import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from pandas.tools.plotting import parallel_coordinates

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv(os.curdir + '/Datasets/wheat.data',header=0,index_col=0,delimiter=',')
df.columns

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
# .. your code here ..
df.drop(['area','perimeter'],axis=1,inplace=True)
print(df.columns)
parallel_coordinates(df,'wheat_type',alpha=0.4)
#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..



plt.show()


