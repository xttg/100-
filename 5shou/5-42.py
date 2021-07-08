import itertools


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show(self):
        print(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self, sentence_id, chunk_id, dst, srcs):
        self.sentence_id = sentence_id
        self.chunk_id = chunk_id
        self.morphs = []
        self.dst = dst
        self.srcs = srcs

    def show_morphs(self):
        morphs = ''
        for morph in self.morphs:
            morphs += morph.surface
        print("morphs:", morphs)

    def show_chunk_id(self):
        print("==========")
        print("chunk_id:", self.chunk_id)

    def show_sentence_id(self):
        if (self.chunk_id == 0):
            print("====================")
            print("sentence_id:", self.sentence_id)

    def show_dst(self):
        print("dst:", self.dst)

    def show_srcs(self):
        print("srcs:", self.srcs[self.chunk_id])


with open('ai.ja.txt.parsed') as f:
    text = f.read().split('\n')
result = []
morphs = []
chunks = []
srcs = [[]]
chunk = None
sentence_id = 0
chunk_id = 0

for i, line in enumerate(text[:-1]):
    if line == 'EOS' and text[i-1] != 'EOS':
        result.append(morphs)
        morphs = []
        sentence_id += 1
        chunk_id = 0
        srcs = [[]]

    elif line[0] == '*':
        if chunk:
            chunks.append(chunk)
        dst = int(line.split()[2][:-1])
        ind = dst + 1 - len(srcs)
        ex = [[] for _ in range(ind)]
        srcs.extend(ex)
        if dst != -1:
            srcs[dst].append(chunk_id)
        chunk = Chunk(sentence_id, chunk_id, dst, srcs)
        chunk_id += 1

    else:
        ls = line.split('\t')
        if len(ls) != 2:
            continue
        tmp = ls[1].split(',')
        morph = Morph(ls[0], tmp[6], tmp[0], tmp[1])
        morphs.append(morph)
        chunk.morphs.append(morph)
chunks.append(chunk)

sentences = [[] for _ in range(len(chunks))]
for chunk in chunks:
    morphs = ''
    for morph in chunk.morphs:
        morphs += morph.surface
    sentences[chunk.sentence_id].append(morphs)

dsts = [[] for _ in range(len(chunks))]
for chunk in chunks:
    dst = sentences[chunk.sentence_id][chunk.dst]
    dsts[chunk.sentence_id].append(dst)
sentences = list(itertools.chain.from_iterable(sentences))
dsts = list(itertools.chain.from_iterable(dsts))
for i, (s, d) in enumerate(zip(sentences, dsts)):
    s = s.replace("　", "").replace("。", "").replace("、", "")
    d = d.replace("　", "").replace("。", "").replace("、", "")
    if s == d:
        continue
    x = [s, d]
    print("\t".join(x))
