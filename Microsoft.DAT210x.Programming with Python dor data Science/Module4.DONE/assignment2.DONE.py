import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper
import os
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
scaleFeatures = False


# TODO: Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)
#
# QUESTION: Should the id column be included as a
# feature?
#
# .. your code here ..

df = pd.read_csv('Datasets/kidney_disease.csv',header=0,index_col=0,delimiter=',')
print(df.head())
print(df.shape)

df.dropna(axis=0,how='any',inplace=True)
print(df.shape)
# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# You're only labeling by color so you can see the effects of PCA
labels = ['red' if i=='ckd' else 'green' for i in df.classification]


# TODO: Use an indexer to select only the following columns:
#       ['bgr','wc','rc']
#
# .. your code here ..
brw = df.loc[:,['bgr','rc','wc']]


# TODO: Print out and check your dataframe's dtypes. You'll might
# want to set a breakpoint after you print it out so you can stop the
# program's execution.
#
# You can either take a look at the dataset webpage in the attribute info
# section: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
# or you can actually peek through the dataframe by printing a few rows.
# What kind of data type should these three columns be? If Pandas didn't
# properly detect and convert them to that data type for you, then use
# an appropriate command to coerce these features into the right type.
#
# .. your code here ..
print(df.head())
print(df.dtypes)
for col in ['pcv','wc','rc']:
    print('========================')
    print([str(x) + ' ' + str(type(x)) for x in df[col].unique() if type(x)
             not in ('float32','float64','int')])
for col in ['pcv','wc','rc']:
    df[[col]] = pd.to_numeric(df.loc[:,col],errors='coerce')
print(df.dtypes)
brw = df.loc[:,['bgr','rc','wc']]
# TODO: PCA Operates based on variance. The variable with the greatest
# variance will dominate. Go ahead and peek into your data using a
# command that will check the variance of every feature in your dataset.
# Print out the results. Also print out the results of running .describe
# on your dataset.
#
# Hint: If you don't see all three variables: 'bgr','wc' and 'rc', then
# you probably didn't complete the previous step properly.
#
# .. your code here ..
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(brw)
new_brw = pca.transform(brw)

print(brw.describe())
print(pd.DataFrame(new_brw).describe())
# TODO: This method assumes your dataframe is called df. If it isn't,
# make the appropriate changes. Don't alter the code in scaleFeatures()
# just yet though!
#
# .. your code adjustment here ..
df = brw
if scaleFeatures: df = helper.scaleFeatures(df)



# TODO: Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#
# .. your code here ..
pca = PCA(n_components=2)
pca.fit(df)
T = pca.transform(df)
# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:
ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()


