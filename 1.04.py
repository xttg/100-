import re

s=input()
t=re.sub("[.]","",s)
data=t.split()
key=[]
for i in range(len(data)):
    list(data[i])
    if i in [0,4,5,6,7,8,14,15,18]:
        key.append(data[i][0])
    else:
        key.append(data[i][0:2])
print(key)
print(dict(zip(key,data)))
