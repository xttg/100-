import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(
    'Dataset/GoogleNews-vectors-negative300.bin', binary=True)
