import pandas as pd
import os
os.chdir('D:\Microsoft Professional Program Data Science\Microsoft.DAT210x.Programming with Python dor data Science\Module2\Datasets')
# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
os.listdir(os.curdir)
df = pd.read_csv('tutorial.csv',delimiter=',',header=0)


# TODO: Print the results of the .describe() method
#
# .. your code here ..
print(df)
print(df.describe())

# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print(df.loc[2:4,'col3'])
