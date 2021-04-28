import re
import random

s=input()
t=re.sub("[.\:]","",s)
data=t.split()

length=[]
for i in range(len(data)):
    length.append(len(list(data[i])))
for j in range(len(data)):
    a=list(data[j])
    if length[j]>4:
        x=a[1:len(a)-1]
        random.shuffle(x)
        a[1:len(a)-1]=x
        data[j]="".join(a)
print(" ".join(data))
