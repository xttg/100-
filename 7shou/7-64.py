import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(
    'Dataset/GoogleNews-vectors-negative300.bin', binary=True)
with open('Dataset/questions-words.txt') as f:
    lines = f.readlines()
with open('Dataset/64.txt', 'w') as f:
    for i, line in enumerate(lines):
        words = line.split()
        if len(words) == 4:
            ans = model.most_similar(
                positive=[words[0], words[2]], negative=[words[1]], topn=1)[0]
            words.extend([ans[0], str(ans[1])])
            output = ' '.join(words)+'\n'
            f.write(output)

        else:
            f.write(' '.join(words)+'\n')
