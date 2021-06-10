from collections import Counter
import MeCab
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'

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
    surface = [x["surface"] for x in l]
    c = Counter(surface)
    print(max(c.values()))
    plt.hist(c.values(),  range=(1, 100))
    plt.show()
