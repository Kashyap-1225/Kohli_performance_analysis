import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("Virat_Kohli.csv") 

run_at_pos=df.groupby("Pos")["6s"].sum()
rap_values=run_at_pos.values
rap_index=run_at_pos.index

fig= plt.figure(figsize=(10,7))
# plt.bar(
#     rap_index,
#     rap_values,
#     color="green",
#     width=0.3
# )
# plt.show()


run_at_pos=df.groupby("Opposition")["Runs"].sum()
rap_values=run_at_pos.values
rap_index=run_at_pos.index
fig= plt.figure(figsize=(15,7))
# plt.bar(
#     rap_index,
#     rap_values,
#     color="#123456",
#     width=0.3
# )
# plt.show()

cen=df.query("Runs>=100")

innings=cen["Inns"].value_counts()
# run=cen["Runs"]
plt.pie(
    innings.values,labels=innings.index
)
plt.show()