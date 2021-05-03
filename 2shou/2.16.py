N=5
import pandas as pd 
df=pd.read_csv("popular-names.txt",sep="\t",header=None)
step=len(df)//N
for i in range(N):
    df_split=df.iloc[i*step:(i+1)*step]
    df_split.to_csv(str(i)+".txt",sep="\t",header=False)
