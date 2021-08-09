from sklearn.cluster import KMeans
import gensim
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.manifold import TSNE
model = gensim.models.KeyedVectors.load_word2vec_format(
    'Dataset/GoogleNews-vectors-negative300.bin', binary=True)
with open('Dataset/country.txt', 'r') as f:
    lines = f.readlines()
countries = []
for line in lines:
    country = line.split('　')[-1].replace('\n', '')
    countries.append(country)
dic = {'United States of America': 'United_States',
       'Russian Federation': 'Russia'}
ng = 0
vec = []
target_countries = []
for c in countries:
    for k, v in dic.items():
        c = c.replace(k, v)
    c = c.replace(' ', '_').replace('-', '_').replace('_and_', '_')
    try:

        vec.append(model[c])
        target_countries.append(c)
    except:
        ng += 1
vec_embedded = TSNE(n_components=2).fit_transform(vec)
vec_embedded_t = list(zip(*vec_embedded))  # 転置
fig, ax = plt.subplots(figsize=(16, 12))
plt.scatter(*vec_embedded_t)
for i, c in enumerate(target_countries):
    ax.annotate(c, (vec_embedded[i][0], vec_embedded[i][1]))
