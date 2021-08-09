import pandas as pd
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(
    'Dataset/GoogleNews-vectors-negative300.bin', binary=True)
df = pd.read_csv('Dataset/wordsim353/combined.csv')
sim = []
for i in range(len(df)):
    line = df.iloc[i]
    sim.append(model.similarity(line['Word 1'], line['Word 2']))
df['w2v'] = sim
df[['Human (mean)', 'w2v']].corr(method='spearman')
