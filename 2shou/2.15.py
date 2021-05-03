import pandas as pd
df=pd.read_csv("popular-names.txt",sep="\t",header=None)
def matubi(N):
    print(df.tail(N))
    
matubi(N)
