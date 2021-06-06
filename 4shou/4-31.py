import MeCab
with open("neko.txt.mecab", "r") as f:
    l = []
    v = set()
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
    for x in l:
        if x["pos"] == "動詞":
            v.add(x["surface"])
    print(v)
