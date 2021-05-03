import pandas as pd
df=pd.read_csv("popular-names.txt",sep="\t",header=None)
def sentou(N):
    print(df.head(N))

sentou(5)
