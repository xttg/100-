import itertools
import re


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
        self.has_noun = False
        self.has_verb = False
        self.has_particle = False
        self.surfaces = ''
        self.first_verb = None
        self.particle = []
        self.sahen_wo = False

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


path = 'ai.ja.txt.parsed'
with open(path) as f:
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
            chunks.append(chunk)  # 文節を表すchunkクラスの集合
        dst = int(line.split()[2][:-1])
        diff = dst + 1 - len(srcs)
        ex = [[] for _ in range(diff)]
        srcs.extend(ex)  # 係り先のインデックス番号が格納できるように配列を拡張
        if dst != -1:
            # 係り先の文節番号に係り元の文節の番号を追加。例えば、chunk_id=1,dst=3のときsrcs[3]に1が追加される
            srcs[dst].append(chunk_id)
        chunk = Chunk(sentence_id, chunk_id, dst, srcs)
        chunk_id += 1

    else:
        ls = line.split('\t')
        d = {}
        if len(ls) != 2:
            continue
        tmp = ls[1].split(',')
        morph = Morph(ls[0], tmp[6], tmp[0], tmp[1])
        morphs.append(morph)
        chunk.morphs.append(morph)  # 文節中の各単語のmorphクラスの集合

chunks.append(chunk)

sentences = [[] for _ in range(len(chunks))]

for chunk in chunks:  # 文節を表すchunkクラスの集合
    morphs = ''
    for morph in chunk.morphs:
        morphs += morph.surface  # 出力用の文節の表層系
        if morph.pos == '名詞':
            chunk.has_noun = True
    # 2次元配列。sentences[2][3]は３文目の4番目の文節の[表層系、係り先の文節番号、名詞を持つかの有無]を表す。
    sentences[chunk.sentence_id].append([morphs, chunk.dst, chunk.has_noun])


def rec(sentence, d, ans):
    if d == -1:
        return ans
    else:
        return rec(sentence, sentence[d][1], ans+'->'+sentence[d][0])


with open('48.txt', mode='w') as f:
    for i, sentence in enumerate(sentences):
        for s, d, has_noun in sentence:
            if has_noun:
                ans = rec(sentence, d, s)
                ans = re.sub('、|。|・', '', ans)
                print(ans)
                f.write(ans+'\n')
