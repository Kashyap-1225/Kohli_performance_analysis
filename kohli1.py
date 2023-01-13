
import pandas as pd

df=pd.read_csv("Virat_Kohli.csv") 

century=df[df["Runs"]>=100]
print(century)

strike=df[df["SR"]>=100]
print(strike)

sl=df[df["Opposition"]=="v Sri Lanka"]
fin=sl[sl["Runs"]>=100]
print(fin)

sl=df[(df["Opposition"]=="v Sri Lanka") & (df["Runs"]>=100)]#working on a query within pandas we use & rather than and
print(sl)

