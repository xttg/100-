from collections import Counter
import MeCab
import matplotlib.pyplot as plt

with open("neko.txt.mecab", "r") as f:
    l = []
    v = set()
    for line in f:
        if line == "EOS\n" or line == " ":
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
    target = list(zip(*c.most_common(10)))
    x = list(target[0])
    y = list(target[1])
    plt.bar(x, y)
    plt.show()
