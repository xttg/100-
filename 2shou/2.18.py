import pandas as pd

df=pd.read_csv("popular-names.txt",sep="\t",header=None)
df1=df.sort_values(by=2,ascending=False)
df1.to_csv("sorted.txt",sep="\t",header=None)
