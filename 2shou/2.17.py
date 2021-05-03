import pandas as pd

df=pd.read_csv("popular-names.txt",sep="\t",header=None)
df1=df.iloc[:,0].unique()
df1.sort()
print(df1)
