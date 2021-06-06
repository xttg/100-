import MeCab
with open("neko.txt.mecab", "r") as f:
    l = []
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
    s = set()
    noun = ""
    num = 0
    for x in l:
        if x["pos"] == "名詞":
            noun = "".join(noun, x["surface"])
            num += 1
        elif num >= 2:
            s.add(noun)
            noun = ""
            num = 0
        else:
            noun = ""
            num = 0
    if num >= 2:
        s.add(noun)
    print(s)
