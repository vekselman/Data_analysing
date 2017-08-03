import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2',header=None)
print(df[0])
col_names = ['RK','PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G',
             'SOG','PCT','GWG','G','A','G','A']
len(col_names)
# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..
df_pd = pd.DataFrame(data=df[0])
df_pd.columns = col_names#, columns=col_names)
print(df_pd.head())
# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..
df_pd.dropna(axis = 0,thresh=4,inplace=True)
df_pd = df_pd[df_pd['RK'] != 'RK']
df_pd.drop('RK', axis = 1, inplace = True)
print(df_pd)
# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df_pd.reset_index(drop=True,inplace=True)
print(df_pd)
# TODO: Get rid of the 'RK' column
#
# .. your code here ..


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
print(df_pd.dtypes)
col_obj = ['PLAYER','TEAM']

for idx, val in enumerate(df_pd.columns):
    if val not in col_obj:
        df_pd[[idx]] = pd.to_numeric(df_pd.iloc[:,idx],errors = 'coerce')

print(df_pd.dtypes)

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..

#1 answer
print('Rows remain %i' % df_pd.shape[0])
#2 answer
print('There are %i unique values in PCT' % len(df_pd.PCT.unique()))
#3 answer
print('Sum of GP value in 15 and 16 indexis: %f' % (df_pd.GP[15]+df_pd.GP[16]))
