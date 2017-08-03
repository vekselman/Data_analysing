import pandas as pd
import numpy as np
import os
os.chdir('D:\Microsoft Professional Program Data Science\Microsoft.DAT210x.Programming with Python dor data Science\Module2\Datasets')

print(os.listdir(os.curdir))
#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
df = pd.read_csv('census.data',index_col = 0,header=None, delimiter = ',')
print(df.head())
cols = ['education','age','capital-gain','race','capital-loss',
        'hours-per-week','sex','classification']
df.columns = cols
print(df.head())
print(df.dtypes)

df[['capital-gain']] = pd.to_numeric(df['capital-gain'],errors='coerce')
print(df.head())
print(df.dtypes)
#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
for x in df.education.unique():
    print(x)
ordinal_edu = ['Preschool',
               '1st-4th','5th-6th','7th-8th','9th','10th','11th','12th',
               'HS-grad','Some-college','Bachelors','Masters',
               'Doctorate']
df.education = df.education.astype('category',ordered=True,categories = ordinal_edu,
                                   ).cat.codes
                                   
for x in df.classification.unique():
    print(x)                                   
ordinal_class =['<=50K','>50K']
df.classification = df.classification.astype('category',ordered=True,
                                             categories = ordinal_class,
                                             ).cat.codes
                                    
print(df.head())
print(df.dtypes)
df['race'] = df['race'].astype('category').cat.codes
df['sex'] = df['sex'].astype('category').cat.codes

print(df.head())
#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#
# .. your code here ..



#
# TODO:
# Print out your dataframe
#
# .. your code here ..


