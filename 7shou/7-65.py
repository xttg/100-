import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(
    'Dataset/GoogleNews-vectors-negative300.bin', binary=True)
cnt = 0
ok = 0
with open('Dataset/64.txt', 'r') as f:
    questions = f.readlines()
for question in questions:
    words = question.split()
    if len(words) == 6:
        cnt += 1
        if (words[3] == words[4]):
            ok += 1
print(ok/cnt)
