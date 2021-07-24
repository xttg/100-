import itertools
import pydot


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
        self.noun = False
        self.verb = False
        self.surfaces = ""

    def show_morphs(self):
        morphs = ''
        for morph in self.morphs:
            morphs += morph.surface
        print("morphs:", morphs)

    def show_chunk_id(self):
        print("chunk_id:", self.chunk_id)

    def show_sentence_id(self):
        if (self.chunk_id == 0):
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
    if line == 'EOS' and text[i-1] != 'EOS':  # 文の区切り
        result.append(morphs)
        morphs = []
        sentence_id += 1
        chunk_id = 0
        srcs = [[]]

    elif line[0] == '*':  # 文節の区切り
        if chunk:
            chunks.append(chunk)
        dst = int(line.split()[2][:-1])
        ind = dst + 1 - len(srcs)
        ex = [[] for _ in range(ind)]
        srcs.extend(ex)  # 係り先のインデックスと現在ある配列のインデックスから足りない個数分の空リストをextendする
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
for chunk in chunks:  # chunksは文節の配列
    for morph in chunk.morphs:  # 文節中の各単語のmorphクラスについて調べている
        chunk.surfaces += morph.surface
    # sentencesは文章の配列。対応する文番号の箱に文節（chunk)を入れている
    sentences[chunk.sentence_id].append(chunk)
graph = pydot.Dot(graph_type='digraph')  # 無向グラフを指定したければ(graph_type='graph')とする
nodes = []
for chunk in sentences[7]:  # 例として8番目の文章を使う
    node = pydot.Node(chunk.surfaces)
    graph.add_node(node)
    nodes.append((node, chunk.dst))
for node, dst in nodes:
    if dst != -1:
        graph.add_edge(pydot.Edge(node, nodes[dst][0]))
graph.write_png('output44.png')  # 実験
