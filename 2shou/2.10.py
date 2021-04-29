f=open("popular-names.txt","r")
x=f.read().split("\n")
print(len(x))
f.close()

#readlinesを使えば以下でも可能
#print(len(f.readlines()))
