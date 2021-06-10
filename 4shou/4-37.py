from collections import Counter
import MeCab
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'

with open("neko.txt.mecab", "r") as f:
    l = []
    v = set()
    tmp = []
    kyouki = []
    cat = False

    for line in f:
        if line == "EOS\n":
            if cat:
                kyouki.extend(tmp)
            else:
                pass
            tmp = []
            cat = False
            continue
        else:
            l1 = line.split("\t")
            if len(l1) != 2:
                continue
            l2 = l1[1].split(",")
            d = {"surface": l1[0], "base": l2[6], "pos": l2[0], "pos1": l2[1]}
            l.append(d)

        if l1[0] != "猫":
            tmp.append(l1[0])
        else:
            cat = True

    c = Counter(kyouki)
    target = list(zip(*c.most_common(10)))
    x = list(target[0])
    y = list(target[1])
    plt.bar(x, y)
    plt.show()
