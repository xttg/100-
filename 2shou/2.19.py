import pandas as pd 
df=pd.read_csv("popular-names.txt",sep="\t",header=None)
cnt=df.iloc[:,0].value_counts()
cnt=pd.DataFrame(cnt)
cnt=cnt.reset_index()
cnt.columns=["name","frequency"]
cnt=cnt.sort_values(by="frequency",ascending=False)
print(cnt)
