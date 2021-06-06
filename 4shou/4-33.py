import MeCab
with open("neko.txt.mecab", "r") as f:
    l = []
    noun = set()
    for line in f:
        if line == "EOS\n":
            continue
        else:
            l1 = line.split("\t")
            if len(l1) != 2:
                continue
            l2 = l1[1].split(",")
            d = {"surface": l1[0], "base": l2[6], "pos": l2[0], "pos1": l2[1]}
            l.append(d)
    for i in range(1, len(l)-1):
        if l[i-1]["pos"] == "名詞" and l[i]["surface"] == "の" and l[i+1]["pos"] == "名詞":
            noun.add(l[i-1]["surface"]+l[i]
                     ["surface"]+l[i+1]["surface"])
    print(noun)
