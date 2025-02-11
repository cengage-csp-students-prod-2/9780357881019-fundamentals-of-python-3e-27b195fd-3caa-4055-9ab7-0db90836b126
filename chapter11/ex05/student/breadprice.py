import pandas as pd
import os
from matplotlib import pyplot as plt
os.chdir('11')    
print(os.getcwd())
bp=pd.read_csv('breadprice.csv')
print(bp)
for col in bp.columns:
    if "Bread" in col:
        breadtable=bp[["Month",col]]
        bindex=col
if bindex is None:
    print("Bread not found")
    pass
breadtable.rename(columns={bindex:"Price"},inplace=True)
breadtable[["Month","Year"]]=breadtable["Month"].str.split("-",expand=True)
breadtable.dropna(inplace=True)
breadtable["Year"]=breadtable["Year"].apply(lambda x: int(x)+2000)
years=sorted(set(breadtable["Year"]))

means=breadtable.groupby("Year")["Price"].mean().reset_index(name="Mean price")

plot=means.plot.line(x="Year",y="Mean price",)
plt.gca().set_xticks(years)
plt.gca().set_title("Bread prices in the US $ per lb")
print(years)
plt.show()
