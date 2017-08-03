import pandas as pd
import os
os.chdir('D:\Microsoft Professional Program Data Science\Microsoft.DAT210x.Programming with Python dor data Science\Module2\Datasets')
# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
os.listdir(os.curdir)

col_names = ['motor','screw','pgain','vgain','class']

df = pd.read_csv('servo.data',delimiter=',',header=None,names=col_names)
print(df.head())
print(df.dtypes)
# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
print(df[df.vgain == 5].shape[0])

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
print(df[(df.motor == 'E') & (df.screw=='E')].shape[0])


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
df[df.pgain == 4].vgain.mean()


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



