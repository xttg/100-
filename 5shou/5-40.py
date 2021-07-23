class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show(self):
        print(self.surface, self.base, self.pos, self.pos1)


with open("ai.ja.txt.parsed") as f:
    result = []
    morphs = []
    for line in f:
        if line == 'EOS\n':
            result.append(morphs)
            morphs = []
            continue
        elif line[0] == "*":
            continue
        else:
            l1 = line.split('\t')
            if len(l1) != 2:
                continue
            else:
                tmp = l1[1].split(',')
                morph = Morph(l1[0], tmp[6], tmp[0], tmp[1])
                morphs.append(morph)
    result1 = [x for x in result if len(x) != 0]
    for x in result1[1]:
        x.show()
