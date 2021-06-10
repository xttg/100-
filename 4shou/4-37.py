from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'

with open('neko.txt.mecab', "r") as f:
    text = f.read().split('\n')
result = []
tmp_cooccurrence = []
cooccurrence = []
inCat = False

for line in text[::-1]:
    if line == 'EOS':
        if inCat:
            cooccurrence.extend(tmp_cooccurrence)
        else:
            pass
        tmp_cooccurrence = []
        inCat = False
        continue

    ls = line.split('\t')
    d = {}
    if len(ls) != 2:
        continue
    tmp = ls[1].split(',')
    d = {'surface': ls[0], 'base': tmp[6], 'pos': tmp[0], 'pos1': tmp[1]}
    result.append(d)
    if ls[0] != '猫':
        tmp_cooccurrence.append(ls[0])
    else:
        inCat = True


c = Counter(cooccurrence)
target = list(zip(*c.most_common(10)))
plt.bar(*target)
plt.show()
