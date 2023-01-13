import pandas as pd

data={
    "Apples":[4,3,6,2],
    "Oranges":[1,2,3,4]
}


index_titles=[
    "a","b","c","d"
]
#df=pd.DataFrame(data,index=index_titles) both work
df=pd.DataFrame(data,index_titles)

# print(df)
# print(type(df))


print(df.loc["a"])#row wise access-indexing with index list is a must
print(df["Oranges"].iloc[0:])#column wise access