from collections import Counter
import MeCab
import matplotlib.pyplot as plt
import numpy as np
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
    v = [kv[1] for kv in c.most_common()]
    print(range(len(v)))
    plt.scatter(np.log(range(len(v))), np.log(v))
    plt.show()
