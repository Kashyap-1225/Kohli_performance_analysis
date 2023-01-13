#kohli

import pandas as pd

df=pd.read_csv("Virat_Kohli.csv") 

#first ten values
# print(df.head(10))

#last ten values
# print(df.tail(10))

df.info()
print(df.shape)

print(df.describe())

print(df["SR"].describe())
print(df["Opposition"].describe())

# run_frequency=df["Runs"].value_counts()
# print(run_frequency)

run_frequency=df["Opposition"].value_counts()
print(run_frequency)


new_df=df[["Runs","SR","Opposition"]]
print(new_df)

print(df["Opposition"]=="v Australia")#boolean indexing

vs_ausies=df[df["Opposition"]=="v Australia"]
print(vs_ausies)