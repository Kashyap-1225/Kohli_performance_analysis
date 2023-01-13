
import pandas as pd

df=pd.read_csv("Virat_Kohli.csv") 

run=df["Runs"].sum()
print(run)

balls=df["BF"].sum()
print(balls)

sr=df["SR"].mean()
print(sr)

#number of matches he has played at different position
#total runs scored in different position
#total six in diff positions
#no of cen in 1st and 2nd inn
#dismissals of kohli
#against which team he has scored 


print(df["Pos"].head(10))

pos=df["Pos"].unique()
print(pos)

df["Pos"]=df["Pos"].map({
    3.0:"Batting at 3",
    4.0:"Batting at 3",
    1.0:"Batting at 3",
    2.0:"Batting at 3",
    7.0:"Batting at 3",
    5.0:"Batting at 3",
    6.0:"Batting at 3",
})

print(df[["Runs","Pos"]])