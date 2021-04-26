s=list(input())
def cipher(b):
    for i in range(len(b)):
        if b[i].islower():
            a=219-ord(b[i])
            b[i]=chr(a)
        else:
            continue
    return b

print("".join(cipher(s)))
