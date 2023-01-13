import pandas as pd

df=pd.read_csv("Virat_Kohli.csv") 

def find_century(x):
    if x>=100:
        return "OG"
    else :
        return "NOOB"

df["Centuries"]=df["Runs"].apply(find_century)
print(df.tail(10))