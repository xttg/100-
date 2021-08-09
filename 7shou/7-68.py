from sklearn.cluster import KMeans
import gensim
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
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
plt.figure(figsize=(32.0, 24.0))
link = linkage(vec, method='ward')
dendrogram(link, labels=target_countries, leaf_rotation=90, leaf_font_size=10)
plt.show()
