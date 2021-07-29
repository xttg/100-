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
            # 係り先に対する係り元の配列に文節の番号を追加。例えば、chunk_id=1,dst=3のときsrcs[3]に1が追加される
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
    for morph in chunk.morphs:
        chunk.surfaces += morph.surface
        if morph.pos == '動詞':
            if chunk.has_verb == False:  # ２つのif文で最左の動詞を見つけ、それをfirst_verbに入れる
                chunk.first_verb = morph.base
            chunk.has_verb = True
        elif morph.pos == '名詞':
            chunk.has_noun = True
        elif morph.pos == '助詞':
            chunk.has_particle = True
            chunk.particle.append(morph.surface)  # 助詞は最後に表示させるために配列に格納

    # sentences[3]には4番目の文章中の各文節のchunkクラスが格納されている。２次元配列
    sentences[chunk.sentence_id].append(chunk)

dsts = [[] for _ in range(len(chunks))]
for chunk in chunks:
    dst = sentences[chunk.sentence_id][chunk.dst]  # ある文節の係り先の文節のchunkクラス
    # dsts[i][3]ではi番目の文章の4番目の文節の係り先の文節のchunkクラスが格納されている。２次元配列
    dsts[chunk.sentence_id].append(dst)

with open('46.txt', mode='w') as f:
    for i, (sentence, dst) in enumerate(zip(sentences, dsts)):  # sentence,dstは１つの文中の文節のchunkクラスが入った配列
        dic = {}
        for s, d in zip(sentence, dst):  # s,dは文章中の文節のchunkクラス
            if s.particle and d.first_verb:  # sが係り元、dが係り先のchunkクラス。係り元が助詞で係り先が最左の動詞かどうか確認
                old = dic.get(d.first_verb, [])  # valueが存在しない場合は[]を返す
                surfaces = re.sub('、|。|・', '', s.surfaces)
                for p in s.particle:
                    dic[d.first_verb] = old + [[p, surfaces]]

        for k, v in dic.items():  # dict.items()にループを行うことでkeyとvalueを取得できる
            ls = sorted(v)  # vは2次元配列。２次元配列の場合は先頭要素でソートされる
            print(*ls)
            # lsをアンパックして[[p,surfaces]]->[(p),(surfaces)]->[[p],[surfaces]]
            ls = list(zip(*ls))
            output = k+'\t'+" ".join(ls[0])+'\t' + \
                " ".join(ls[1])+'\n'  # 述語 格の集合　項の集合
            f.write(output)
