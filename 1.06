str1="paraparaparadise"
str2="paragraph"

def bigram(a):
    s=set()
    for i in range(len(a)-1):
        s.add("".join(a[i]+a[i+1]))
    return s
X=bigram(str1)
Y=bigram(str2)
Z=set()
Z.add("".join("s"+"e"))
print(X|Y)
print(X&Y)
print(X-Y)
print(Z,Z<=X,Z<=Y)
