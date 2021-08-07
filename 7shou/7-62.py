import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(
    'Dataset/GoogleNews-vectors-negative300.bin', binary=True)
print(model.most_similar('United_States', topn=10))
